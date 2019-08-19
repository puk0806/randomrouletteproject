from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('roulettehome.urls')),
    path('goodmenu/', include('goodmenu.urls')),
    path('usermenu/',include('usermenu.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name ='register_done'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
