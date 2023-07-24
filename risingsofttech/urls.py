"""risingsofttech URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name ="dashboard"),
    # path('', home, name ="home"),
    
    

    path('',include('apps.role_permission.urls',namespace='role_app')),
    path('',include('apps.authentication.urls',namespace='authentication')),
    path('',include('apps.system_settings.urls',namespace='setting')),
    
    

    
]

'''Error handling message[Look link below for message]'''
handler404 = 'risingsofttech.views.error_404'
# https://docs.djangoproject.com/en/4.1/topics/http/views/#customizing-error-views


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
