from django.contrib import admin
from .models import Album, Goodmenu, GoodStar, GoodComment, Photo

# Register your models here.
class GoodmenuInline(admin.StackedInline):
    model = Goodmenu
    extra = 0


class GoodCommentInline(admin.StackedInline):
    model = GoodComment
    extra = 0

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 0


class AlbumAdmin(admin.ModelAdmin):
    inlines = [GoodmenuInline]
    list_display = ('name', 'description')

class GoodStarAdmin(admin.ModelAdmin):
    inlines = [GoodmenuInline,GoodCommentInline]
    list_display = ('name', 'description')


class GoodmenuAdmin(admin.ModelAdmin):
    inlines = [GoodCommentInline,PhotoInline]
    list_display = ('album', 'author','title')

class GoodCommentAdmin(admin.ModelAdmin):
    list_display = ('goodauthorcomment','goodmenucomment','title')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title','goodmenuphoto')

admin.site.register(Album, AlbumAdmin)
admin.site.register(GoodStar, GoodStarAdmin)
admin.site.register(Goodmenu, GoodmenuAdmin)
admin.site.register(GoodComment,GoodCommentAdmin)
admin.site.register(Photo,PhotoAdmin)

