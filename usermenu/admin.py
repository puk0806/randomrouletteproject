from django.contrib import admin
from .models import UserAlbum, UserMenu, UserArea, UserStar, UserComment

# Register your models here.
class UserMenuInline(admin.StackedInline):
    model = UserMenu
    extra = 0

class UserCommentInline(admin.StackedInline):
    model = UserComment
    extra = 0

class UserAlbumAdmin(admin.ModelAdmin):
    inlines = [UserMenuInline]
    list_display = ('name', 'description')

class UserAreaAdmin(admin.ModelAdmin):
    inlines = [UserMenuInline]
    list_display = ('name', 'description')

class UserStarAdmin(admin.ModelAdmin):
    inlines = [UserMenuInline,UserCommentInline]
    list_display = ('name', 'description')
    

class UserMenuAdmin(admin.ModelAdmin):
    inlines = [UserCommentInline]
    list_display = ('useralbum', 'userauthor','userarea','title')

class UserCommentAdmin(admin.ModelAdmin):
    list_display = ('userauthorcomment','usermenucomment','title')


admin.site.register(UserAlbum, UserAlbumAdmin)
admin.site.register(UserArea, UserAreaAdmin)
admin.site.register(UserStar, UserStarAdmin)
admin.site.register(UserMenu, UserMenuAdmin)
admin.site.register(UserComment,UserCommentAdmin)

