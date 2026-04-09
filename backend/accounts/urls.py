from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, CustomerAddressViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r"customers", CustomerViewSet, basename="customer")
router.register(r"addresses", CustomerAddressViewSet, basename="address")
router.register(r"employees", EmployeeViewSet, basename="employee")

urlpatterns = router.urls