from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from django.shortcuts import get_object_or_404

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetailViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceDetailSerializer

    def get_object(self):
        invoice_id = self.kwargs['invoice_pk']
        detail_id = self.kwargs['pk']
        return get_object_or_404(InvoiceDetail, invoice__id=invoice_id, id=detail_id)

    def get_queryset(self):
        invoice_id = self.kwargs['invoice_pk']
        return InvoiceDetail.objects.filter(invoice__id=invoice_id)

