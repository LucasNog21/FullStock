"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from stock.views import (ProductListView, ProductCreateView, DashboardView, AnalyticsView, MessagesView, RegisterView,
                         LoginView, LogoutView, ProviderCreateView, CategoryCreateView, CategoryListView, ProviderListView,
                         ProductUpdateView, CategoryUpdateView, ProviderUpdateView, ProductDeleteView, CategoryDeleteView, ProviderDeleteView, )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductListView.as_view(), name='products'),
    path('categorys/', CategoryListView.as_view(), name='categorys'),
    path('providers/', ProviderListView.as_view(), name='providers'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
    path('messages/', MessagesView.as_view(), name='messagesView'),
    path('register/', RegisterView.as_view(), name='register'),
    path('createProduct/', ProductCreateView.as_view(), name='createProduct'),
    path('createProvider/', ProviderCreateView.as_view(), name='createProvider'),
    path('createCategory/', CategoryCreateView.as_view(), name='createCategory'),
    path('updateProduct/<int:pk>', ProductUpdateView.as_view(), name='updateProduct'),
    path('updateCategory/<int:pk>', CategoryUpdateView.as_view(), name='updateCategory'),
    path('updateProvider/<int:pk>', ProviderUpdateView.as_view(), name='updateProvider'),
    path('deleteProduct/<int:pk>', ProductDeleteView.as_view(), name='deleteProduct'),
    path('deleteCategory/<int:pk>', CategoryDeleteView.as_view(), name='deleteCategory'),
    path('deleteProvider/<int:pk>', ProviderDeleteView.as_view(), name='deleteProvider'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)