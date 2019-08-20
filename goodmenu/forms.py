from django import forms
from .models import Album,GoodStar,Goodmenu,GoodComment,Photo
from django.forms import ModelForm

class GoodCommentForm(forms.ModelForm):
    class Meta:
        model = GoodComment
        fields = ['goodstarcomment','title','body']
