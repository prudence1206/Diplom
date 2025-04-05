from distutils.util import strtobool
from rest_framework.request import Request
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import IntegrityError
from django.db.models import Q, Sum, F
from django.http import JsonResponse
from requests import get
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from ujson import loads as load_json
from yaml import load as load_yaml, Loader
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from marketplace.models import Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Order, OrderItem, \
    Contact, ConfirmEmailToken
from marketplace.serializers import UserSerializer, CategorySerializer, ShopSerializer, ProductInfoSerializer, \
    OrderItemSerializer, OrderSerializer, ContactSerializer, ProductSerializer, BasketSerializer
from marketplace.signals import new_user_registered, new_order

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def login(self, request):
        # Реализация логина
        return Response({'status': 'success'})

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.AllowAny]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related('product_infos').all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

class ProductInfoViewSet(viewsets.ModelViewSet):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer
    permission_classes = [permissions.AllowAny]

class BasketViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = BasketSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(user=self.request.user)
        return Order.objects.none()

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(user=self.request.user)
        return Order.objects.none()

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(user=self.request.user)
        return Contact.objects.none()

# Старые представления для совместимости
class RegisterAccount(viewsets.ViewSet):
    def create(self, request):
        return UserViewSet().register(request)

class ConfirmAccount(viewsets.ViewSet):
    def create(self, request):
        return Response({'status': 'success'})

class AccountDetails(viewsets.ViewSet):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class LoginAccount(viewsets.ViewSet):
    def create(self, request):
        return UserViewSet().login(request)

class CategoryView(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

class ShopView(viewsets.ViewSet):
    def list(self, request):
        queryset = Shop.objects.all()
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductInfoView(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class BasketView(viewsets.ViewSet):
    def list(self, request):
        queryset = Order.objects.filter(user=request.user)
        serializer = BasketSerializer(queryset, many=True)
        return Response(serializer.data)

class PartnerUpdate(APIView):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'Status': False, 'Error': 'Log in required'}, status=403)
        return Response({'Status': True})

class PartnerState(APIView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'Status': False, 'Error': 'Log in required'}, status=403)
        return Response({'Status': True})

class PartnerOrders(APIView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'Status': False, 'Error': 'Log in required'}, status=403)
        return Response({'Status': True})

class ContactView(viewsets.ViewSet):
    def list(self, request):
        queryset = Contact.objects.filter(user=request.user)
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)

class OrderView(viewsets.ViewSet):
    def list(self, request):
        queryset = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
