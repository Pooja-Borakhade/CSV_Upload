"""csv_upload URL Configuration

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
from django.contrib import admin
from django.urls import path
from  csv_app.views import export_csv,home,import_csv,reg_form,login_page,logout_app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('export_csv/', export_csv, name = "export_csv"),
    path('home/', home, name = "home"),
    path('upload/',import_csv,name ='upload'),
    path('reg/',reg_form,name ='reg'),
    path('login/',login_page,name ='login'),
    path('login/logout/',logout_app,name ='logout'),
    
    
    
    
    
]
