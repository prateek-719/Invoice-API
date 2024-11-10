from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoices/(?P<invoice_pk>\d+)/details', InvoiceDetailViewSet, basename='invoice-detail')

urlpatterns = [
    path('', include(router.urls)),
]
