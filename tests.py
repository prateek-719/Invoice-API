from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.invoice_data = {
            "date": "2024-01-04",
            "customer_name": "Test Invoice",
        }
        self.invoice = Invoice.objects.create(**self.invoice_data)

        self.detail_data = {
            "invoice": self.invoice,
            "description": "Item 1",
            "quantity": 2,
            "unit_price": 10.0,
            "price": 20.0,
        }
        self.detail = InvoiceDetail.objects.create(**self.detail_data)

    def test_create_invoice(self):
        url = reverse('invoice-list')
        data = {
            "date": "2024-01-05",
            "customer_name": "New Customer",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_invoice(self):
        url = reverse('invoice-detail', args=[self.invoice.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invoice(self):
        url = reverse('invoice-detail', args=[self.invoice.id])
        data = {
            "date": "2024-01-05",
            "customer_name": "Updated Customer",
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invoice(self):
        url = reverse('invoice-detail', args=[self.invoice.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_invoice_detail(self):
        invoice_data = {
            'date': '2024-01-04',
            'customer_name': 'Test Invoice'
        }
        invoice_url = reverse('invoice-list')
        response = self.client.post(invoice_url, invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        invoice_id = response.data['id']

        data = {
            'invoice': invoice_id,  
            'description': 'Item 1',
            'quantity': 2,
            'unit_price': 10.0,
            'price': 20.0
        }
        url = reverse('invoice-detail', args=[invoice_id]) + 'details/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_invoice_detail(self):
        url = reverse('invoice-detail-detail', args=[self.invoice.id, self.detail.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invoice_detail(self):
        url = reverse('invoice-detail-detail', args=[self.invoice.id, self.detail.id])
        data = {
            "description": "Updated Item",
            "quantity": 4,
            "unit_price": 12.0,
            "price": 48.0,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invoice_detail(self):
        url = reverse('invoice-detail-detail', args=[self.invoice.id, self.detail.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


