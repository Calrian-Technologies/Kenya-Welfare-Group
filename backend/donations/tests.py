from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Campaign, Donation
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework.test import APIClient
from unittest.mock import patch

class CampaignTests(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_campaign(self):
        url = reverse('campaign-list')
        data = {
            'name': 'Test Campaign',
            'description': 'Test Description',
            'goal_amount': '1000.00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Campaign.objects.count(), 1)
        self.assertEqual(Campaign.objects.get().name, 'Test Campaign')

    def test_get_campaigns(self):
        Campaign.objects.create(name='Test Campaign', description='Test Description', goal_amount='1000.00')
        url = reverse('campaign-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class DonationTests(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.campaign = Campaign.objects.create(name='Test Campaign', description='Test Description', goal_amount='1000.00')

    def test_create_donation(self):
        url = reverse('donation-list')
        data = {
            'user': self.user.id,
            'campaign': self.campaign.id,
            'amount': '100.00',
            'payment_status': 'pending'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Donation.objects.count(), 1)
        self.assertEqual(str(Donation.objects.get().amount), '100.00')

    @patch('donations.donation_modules.paypal_donations.create_paypal_payment')
    def test_paypal_payment(self, mock_create_paypal_payment):
        donation = Donation.objects.create(user=self.user, campaign=self.campaign, amount='100.00', payment_status='pending')
        url = reverse('donation-pay', args=[donation.id])
        data = {'payment_method': 'paypal'}
        mock_create_paypal_payment.return_value = Response({'approval_url': 'http://paypal.com'}, status=status.HTTP_200_OK)
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('approval_url', response.data)

    @patch('donations.donation_modules.stripe_donations.create_stripe_payment_intent')
    def test_stripe_payment(self, mock_create_stripe_payment_intent):
        donation = Donation.objects.create(user=self.user, campaign=self.campaign, amount='100.00', payment_status='pending')
        url = reverse('donation-pay', args=[donation.id])
        data = {'payment_method': 'stripe'}
        mock_create_stripe_payment_intent.return_value = Response({'client_secret': 'secret'}, status=status.HTTP_200_OK)
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('client_secret', response.data)
