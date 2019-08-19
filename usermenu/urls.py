from django.urls import path

from .views import *
from . import views
import usermenu.views


app_name = 'usermenu'

urlpatterns = [
    path('',UserAlbumList.as_view(), name='index'),
    path('date/',UserAlbumList2.as_view(), name='date'),
    path("create/", UserMenuCreate.as_view(), name='create'),
    path("delete/<int:pk>/", UserMenuDelete.as_view(), name='delete'),
    path("update/<int:pk>/", UserMenuUpdate.as_view(), name='update'),
    path("detail/<int:usermenu_id>/",views.usermenuDetail,name = 'detail'),
    path("like/<int:usermenu_id>/", UserMenuLike.as_view(), name='like'),
    path("favorite/<int:usermenu_id>/", UserMenuFavorite.as_view(), name='favorite'),
    path("like/", UserMenuLikeList.as_view(), name="like_list"),
    path("favorite/", UserMenuFavoriteList.as_view(), name="favorite_list"),
    path("mylist/",UserMenuMyList.as_view(), name='mylist'),
    path("commentcreate/", UserCommentCreate.as_view(), name = 'commentcreate'),
    path("commentdelete/<int:pk>/", UserCommentDelete.as_view(), name='commentdelete'),
    path("commentupdate/<int:pk>/", UserCommentUpdate.as_view(), name='commentupdate'),

]

