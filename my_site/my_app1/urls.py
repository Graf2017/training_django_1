"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path

from my_site import settings
from .views import *

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('catalog/', catalog, name='catalog'),
    path('about/', about, name='about'),
    path('box/', box, name='box'),
    path('delivery/', delivery, name='delivery'),
    path('catalog/<slug:name_of_categories>/', show_positions, name='show_positions'),
    path('catalog/<slug:name_of_categories>/<slug:position_slug>/', show_position, name='show_position'),
    path('add_position/', add_position, name='add_position'),
    path('register/', login, name='register'),
    path('login/', login, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
