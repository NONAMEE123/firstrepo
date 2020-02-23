

"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from mproject import views



urlpatterns = [
    
    #path('plot/',views.plot,name='plot'),
    path('detail_4/',views.detail_4,name='detail_4'),
    path('detail_3/',views.detail_3,name='detail_3'),
    path('detail_2/',views.detail_2,name='detail_2'),
    path('detail_1/',views.detail_1,name='detail_1'),
    path('images_5/',views.images_5,name='images_5'),
    path('images_4/',views.images_4,name='images_4'),
    path('images_3/',views.images_3,name='images_3'),
    path('images_2/',views.images_2,name='images_2'),
    path('images_1/',views.images_1,name='images_1'),
    path('graphes/',views.graphes,name='graphes'),
    path('dataframecss/',views.dataframecss,name='dataframecss'),
    path('statics/',views.statics,name='statics'),
    path('tail/',views.tail,name='tail'),
    path('head/',views.head,name='head'), 
    path('dataframe/',views.dataframe,name='dataframe'),
    path('acc2/',views.exportjson,name='exportjson'),
    path('acc1/',views.exporthtml,name='exporthtml'),
    path('acc/',views.simple_upload,name='simple_upload'),
    path('registerform/',views.registerform,name='registerform'),
    path('login/',views.login,name='login'),
    path('contact/',views.contact_form, name='contact_form'),
    path('home/',views.home, name='home'),
    path('admin/', admin.site.urls),
    
    #path('login/',views.login,name="login"),
    #path('logout/',views.logout,name="logout"),
    #path('registre',views.registre,name="registre")





] 
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

