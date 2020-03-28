from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.auth import get_user_model
import uuid
import os
from datetime import date
from django.urls import reverse
from django.template.defaultfilters import slugify
from unidecode import unidecode
from django.core.validators import FileExtensionValidator

# Create your models here.

class Article(models.Model):
    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        today = date.today()
        today_path = today.strftime("cover_images/%Y/%m/%d") 
        return os.path.join(today_path, filename)

    def get_file_path2(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        today = date.today()
        today_path = today.strftime("stories/%Y/%m/%d") 
        return os.path.join(today_path, filename)

    

    GRADE_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),)

    
    story_writer=models.CharField(max_length = 50,verbose_name="Yazar Adı",blank=False, null=False)
    email = models.EmailField(max_length=70,blank=False,verbose_name="E-mail", null=True)
    title = models.CharField(max_length = 50,verbose_name="Başlık")
    content = RichTextField(verbose_name="Açıklama")
    created_date = models.DateTimeField(auto_now_add = True)
    article_image = models.FileField(blank=False, null=True,verbose_name="Hikaye Kapağı Ekle",default='900x300.png',upload_to = get_file_path)
    hikaye = models.FileField(null=True, blank=False, validators=[FileExtensionValidator(['pdf'])],default='deneme.pdf',verbose_name="Hikayeyi Ekle (PDF FORMAT)",upload_to = get_file_path2)
    published = models.BooleanField(auto_created=True,default=False)
    grade = models.IntegerField(blank=False, null=False,verbose_name="Sınıf", default=1,choices=GRADE_CHOICES)
    hikaye_slug = models.SlugField(null=True,unique=True,editable=False)

    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


    def get_unique_slug(self):
        sayi=0
        slug=slugify(unidecode(self.title))
        new_slug = slug
        while Article.objects.filter(hikaye_slug=new_slug).exists():
            sayi+=1
            new_slug = "%s-%s"%(slug,sayi)
        slug=new_slug
        return slug

    def save(self,*args,**kwargs):
        if self.id is None:
            self.hikaye_slug = self.get_unique_slug()
        super(Article, self).save(*args,**kwargs)