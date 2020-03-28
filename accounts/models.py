from django.db import models
# Özel kullanıcı
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import datetime
from datetime import date
import uuid
import os
 
 
class User(AbstractUser):
    #Avatar'ı ekledik.
    E = "Erkek"
    M = "Kadın"
    No = "Belirtmek İstemiyorum"
    Gender = (
        (E, 'Erkek'),
        (M, 'Kadın'),
        (No, 'Belirtmek İstemiyorum'),
    )

    Locations = (
        ("0","Belirtilmemiş"),
        ("1", 'Adana'),
        ("2", 'Adıyaman'),
        ("3", 'Afyon'),
        ("4", 'Ağrı'),
        ("5", "Amasya"),
        ("6", "Ankara"),
        ("7", "Antalya"),
        ("8", "Artvin"),
        ("9", "Aydın"),
        ("10", "Balıkesir"),
        ("11", "Bilecik"),
        ("12", "Bingöl"),
        ("13", "Bitlis"),
        ("14", "Bolu"),
        ("15", "Burdur"),
        ("16", "Bursa"),
        ("17", "Çanakkale"),
        ("18", "Çankırı"),
        ("19", "Çorum"),
        ("20", "Denizli"),
        ("21", "Diyarbakır"),
        ("22", "Edirne"),
        ("23", "Elazığ"),
        ("24", "Erzincan"),
        ("25", "Erzurum"),
        ("26", "Eskişehir"),
        ("27", "Gaziantep"),
        ("28", "Giresun"),
        ("29", "Gümüşhane"),
        ("30", "Hakkari"),
        ("31", "Hatay"),
        ("32", "Isparta"),
        ("33", "Mersin"),
        ("34", "İstanbul"),
        ("35", "İzmir"),
        ("36", "Kars"),
        ("37", "Kastamonu"),
        ("38", "Kayseri"),
        ("39", "Kırklareli"),
        ("40", "Kırşehir"),
        ("41", "Kocaeli"),
        ("42", "Konya"),
        ("43", "Kütahya"),
        ("44", "Malatya"),
        ("45", "Manisa"),
        ("46", "K.maraş"),
        ("47", "Mardin"),
        ("48", "Muğla"),
        ("49", "Muş"),
        ("50", "Nevşehir"),
        ("51", "Niğde"),
        ("52", "Ordu"),
        ("53", "Rize"),
        ("54", "Sakarya"),
        ("55", "Samsun"),
        ("56", "Siirt"),
        ("57", "Sinop"),
        ("58", "Sivas"),
        ("59", "Tekirdağ"),
        ("60", "Tokat"),
        ("61", "Trabzon"),
        ("62", "Tunceli"),
        ("63", "Şanlıurfa"),
        ("64", "Uşak"),
        ("65", "Van"),
        ("66", "Yozgat"),
        ("67", "Zonguldak"),
        ("68", "Aksaray"),
        ("69", "Bayburt"),
        ("70", "Karaman"),
        ("71", "Kırıkkale"),
        ("72", "Batman"),
        ("73", "Şırnak"),
        ("74", "Bartın"),
        ("75", "Ardahan"),
        ("76", "Iğdır"),
        ("77", "Yalova"),
        ("78", "Karabük"),
        ("79", "Kilis"),
        ("80", "Osmaniye"),
        ("81", "Düzce"),
    )
    
    def get_file_path_avatar(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        today = date.today()
        today_path = today.strftime("avatars/%Y/%m/%d") 
        return os.path.join(today_path, filename)
    
    def get_file_path_cover(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        today = date.today()
        today_path = today.strftime("covers/%Y/%m/%d") 
        return os.path.join(today_path, filename)  

    gender = models.CharField(max_length=21,choices=Gender,default=No,blank=True, null=True,verbose_name="Cinsiyet")
    Avatar = models.ImageField(default="avatars/default.png",upload_to=get_file_path_avatar,blank=True, null=True,verbose_name="Kullanıcı Fotoğrafı")
    cover = models.ImageField(default="cover/default.jpg",upload_to=get_file_path_cover,blank=True, null=True,verbose_name="Kapak Fotoğrafı")
    birth_date = models.DateTimeField(default=datetime.date.today, blank=True,verbose_name="Doğum Günü")
    register_date = models.DateTimeField(default=datetime.date.today, blank=True)
    location = models.CharField(max_length=2,choices=Locations,default=0,blank=True, null=True,verbose_name="Konum")
    is_active = models.BooleanField(default=True)
