"""
URL configuration for imageShareProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from image_share.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_image, name='upload_image'),
    path('images/', image_list, name='image_list'),
    path('my-images/',my_images, name='my_images'),
    path('login/', user_login, name ='login'),
    path('logout/', user_logout, name = 'logout'),
    path('profile/', profile, name='profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
