from django import  forms
from .models import Article



class ArticleForm(forms.ModelForm):
    GRADE_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),)
    grade = forms.ChoiceField(choices=GRADE_CHOICES,)
    class Meta:
        model = Article
        
        fields = ['title', 'content',"article_image","grade"]
        