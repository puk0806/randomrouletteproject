from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from .fields import ThumbnailImageField

# Create your models here.

class UserAlbum(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


    #def get_absolute_url(self):
    #    return reverse('usermenu:useralbum_detail', args=(self.id,))


class UserArea(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class UserStar(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    img = ThumbnailImageField(upload_to='userstar',null=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    

class UserMenu(models.Model):
    useralbum = models.ForeignKey('UserAlbum', on_delete=models.CASCADE)
    userauthor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userauthor')
    userarea = models.ForeignKey('UserArea', on_delete=models.CASCADE, related_name='userarea')
    userstar = models.ForeignKey('UserStar',on_delete=models.CASCADE, related_name='userstar')
    title = models.CharField(max_length=50)
    smallbody = models.CharField(max_length=500,null=True)
    body = models.TextField(null=True)
    visitcount = models.IntegerField(default=0)
    smallimg = ThumbnailImageField(upload_to='usermenu/%Y/%m')
    detailimg = ThumbnailImageField(upload_to='usermenu/%Y/%m')
    date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, related_name='like_post', blank=True)
    favorite = models.ManyToManyField(User, related_name='favorite_post', blank=True)
    hit = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-hit']

    def get_absolute_url(self):
        return reverse('usermenu:usermenu_detail', args=(self.id,))

    @property
    def update_counter(self):
        self.hit = self.hit +1
        self.save()

class UserComment(models.Model):
    usermenucomment = models.ForeignKey('UserMenu',on_delete=models.CASCADE, related_name='usercomments')
    userauthorcomment = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userauthorcomment')
    userstarcomment = models.ForeignKey('UserStar',on_delete=models.CASCADE, related_name='userstarcomment',null=True)
    title = models.CharField(max_length=50)
    body = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']