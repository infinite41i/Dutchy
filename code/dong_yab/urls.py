"""dong_yab URL Configuration

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
from account import views
from account.views import serve_file
from dong_yab import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.first_page),
    path('admin/', admin.site.urls),
    path('account/', views.sign, name="sign"),
    path('home/<str:uuid>/', views.home, name="home"),
    path("logout/", views.logout_view, name="logout"),
    path("add_balance/", views.add_balance, name="add_balance"),
    path('add_group/', views.add_group, name="add_group"),
    path('media/(<str:path>)', serve_file, name='serve_file'),
    path('join_group/', views.join_group, name="join_group"),
    path('add_factor/', views.add_factor, name="add_factor")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[-1])
