from django.shortcuts import render
from .models import Category, Company, Product
from .serializers import CategorySerializer, CompanySerializer, ProductSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, \
    UpdateAPIView, DestroyAPIView, RetrieveAPIView


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CompanyGenericViewSet(GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
