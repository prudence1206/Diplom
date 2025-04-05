from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from marketplace.views import (
    UserViewSet, CategoryViewSet, ShopViewSet, ProductViewSet,
    BasketViewSet, OrderViewSet, ContactViewSet, ProductInfoViewSet,
    PartnerUpdate, PartnerState, PartnerOrders
)

app_name = 'marketplace'
router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-info', ProductInfoViewSet)
router.register(r'basket', BasketViewSet)
router.register(r'order', OrderViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/password_reset/', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm/', reset_password_confirm, name='password-reset-confirm'),
    path('partner/update/', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state/', PartnerState.as_view(), name='partner-state'),
    path('partner/orders/', PartnerOrders.as_view(), name='partner-orders'),
]
