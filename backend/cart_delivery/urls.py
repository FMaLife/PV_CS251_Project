from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet, DeliveryViewSet

router = DefaultRouter()
router.register(r"carts", CartViewSet, basename="cart")
router.register(r"items", CartItemViewSet, basename="cart-item")
router.register(r"deliveries", DeliveryViewSet, basename="delivery")

urlpatterns = router.urls