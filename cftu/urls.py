"""
URL configuration for cftu project.

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from cftu import settings
from holes.views import create
from home.views import index
from members.views import signup, logout_user, login_user, info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('info', info, name='info'),
    path('login', login_user, name="login"),
    path('signup', signup, name="signup"),
    path('logout', logout_user, name="logout"),
    path('create_hole', create, name="create")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
