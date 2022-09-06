"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from shop import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', views.ProductModelViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include(router.urls)),
    path('company', views.CompanyGenericViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('category/create/', views.CategoryCreateAPIView.as_view()),
    path('category/list/', views.CategoryCreateAPIView.as_view()),
    path('category/update/<int:pk>/', views.CategoryUpdateAPIView.as_view()),
    path('category/destroy/<int:pk>/', views.CategoryDestroyAPIView.as_view()),
    path('category/retrieve/<int:pk>/', views.CategoryRetrieveAPIView.as_view()),
]
