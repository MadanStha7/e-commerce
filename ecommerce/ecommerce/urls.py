"""ecommerce URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from products.views import ProductListView, product_list_view, ProductDetailView, product_detail_view
from . import views
from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_page, name='home_page'),
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('login/', views.login_page, name='login_page'),
    path('products/', ProductListView.as_view()),
    path('products-fbv/', product_list_view, name='list'),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('products-fbv/<int:product_id>/', product_detail_view, name='detail.html'),
    path('register/', views.register_page, name='register_page'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
v=27