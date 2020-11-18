"""imgcap_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls import url
from django.contrib import admin
from imgapp import views
from django.conf.urls.static import static
from django.conf import settings

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^upload', 'imgapp.views.uploadImg'),
#     url(r'^show', 'imgapp.views.showImg'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('imgcap', views.show)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
