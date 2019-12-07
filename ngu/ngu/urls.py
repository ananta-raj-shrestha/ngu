"""ngu URL Configuration

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
from django.contrib.auth  import views as auth_views
from django.conf.urls import url
from django.urls import path,include
from blog import views as blog_views
from  users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name="register"),
    path('',include('blog.urls')),
    path('login/',user_views.login,name="login"),
    path('logout/',user_views.logout,name="logout"),
    path('profile/',user_views.profile,name="profile"),
    path('update/',user_views.update,name="edit"),
    # path('password-reset/',auth_views.password_reset,name="password_reset"),
    # path('password-reset-done/',auth_views.password_reset_done,name="password_reset_done"),
    # path('password-reset-confirm/',auth_views.password_reset_confirm,name="password_reset_confirm"),
    # path('password-reset-complete/',auth_views.password_reset_complete,name="password_reset_complete"),

   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
