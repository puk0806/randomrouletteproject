from django.urls import path

from .views import *


app_name = 'goodmenu'

urlpatterns = [
    path('',AlbumList.as_view(), name='index'),
    path('album/',AlbumList.as_view(), name='album_list'),
    path('album/<int:pk>/',AlbumDetail.as_view(),name ='album_detail'),
    path('goodmenu/<int:pk>/', GoodmenuDetail.as_view(), name = 'goodmenu_detail'),
    path("goodmenu/like/<int:goodmenu_id>/", GoodMenuLike.as_view(), name='like'),
    path("goodmenu/favorite/<int:goodmenu_id>/", GoodMenuFavorite.as_view(), name='favorite'),
    path("goodmenu/like/", GoodMenuLikeList.as_view(), name="like_list"),
    path("goodmenu/favorite/", GoodMenuFavoriteList.as_view(), name="favorite_list"),
    path("commentcreate/", GoodCommentCreate.as_view(), name = 'commentcreate'),
    path("commentdelete/<int:pk>/", GoodCommentDelete.as_view(), name='commentdelete'),
    path("commentupdate/<int:pk>/", GoodCommentUpdate.as_view(), name='commentupdate'),
]