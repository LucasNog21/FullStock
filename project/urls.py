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
from django.conf import settings
from django.conf.urls.static import static
from stock import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('categorys/', views.CategoryListView.as_view(), name='categorys'),
    path('providers/', views.ProviderListView.as_view(), name='providers'),
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('createProduct/', views.ProductCreateView.as_view(), name='createProduct'),
    path('createProvider/', views.ProviderCreateView.as_view(), name='createProvider'),
    path('createCategory/', views.CategoryCreateView.as_view(), name='createCategory'),
    path('updateProduct/<int:pk>', views.ProductUpdateView.as_view(), name='updateProduct'),
    path('updateCategory/<int:pk>', views.CategoryUpdateView.as_view(), name='updateCategory'),
    path('updateProvider/<int:pk>', views.ProviderUpdateView.as_view(), name='updateProvider'),
    path('deleteProduct/<int:pk>', views.ProductDeleteView.as_view(), name='deleteProduct'),
    path('deleteCategory/<int:pk>', views.CategoryDeleteView.as_view(), name='deleteCategory'),
    path('deleteProvider/<int:pk>', views.ProviderDeleteView.as_view(), name='deleteProvider'),
    path('createOrder/', views.OrderCreateView.as_view(), name='createOrder'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('createOrder/', views.OrderCreateView.as_view(), name='createOrder'),
    path('updateOrder/<int:pk>', views.OrderUpdateView.as_view(), name='updateOrder'),
    path('deleteOrder/<int:pk>', views.OrderDeleteView.as_view(), name='deleteOrder'),
    path('sales/', views.SaleListView.as_view(), name='sales'),
    path('createSale/', views.SaleCreateView.as_view(), name='createSale'),
    path('updateSale/<int:pk>', views.SaleUpdateView.as_view(), name='updateSale'),
    path('deleteSale/<int:pk>', views.SaleDeleteView.as_view(), name='deleteSale'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)