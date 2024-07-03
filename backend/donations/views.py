from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Campaign, Donation, Payment
from .serializers import CampaignSerializer, DonationSerializer, PaymentSerializer
from .donation_modules.paypal_donations import create_paypal_payment, execute_paypal_payment
from .donation_modules.stripe_donations import create_stripe_payment_intent

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    @action(detail=True, methods=['post'])
    def pay(self, request, pk=None):
        donation = self.get_object()
        payment_method = request.data.get('payment_method')

        if payment_method == 'paypal':
            return create_paypal_payment(donation)
        elif payment_method == 'stripe':
            return create_stripe_payment_intent(donation)
        # Add more payment methods here

        return Response({'error': 'Invalid payment method'}, status=status.HTTP_400_BAD_REQUEST)
