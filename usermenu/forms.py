from django import forms
from .models import UserComment,UserMenu,UserStar,UserArea,UserAlbum
from django.forms import ModelForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ['userstarcomment','title','body']
