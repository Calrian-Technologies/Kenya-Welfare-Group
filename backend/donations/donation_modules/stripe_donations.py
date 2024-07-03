import stripe
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_stripe_payment_intent(donation):
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(donation.amount * 100),  # Amount in cents
            currency='usd',
            payment_method_types=['card'],
        )
        return Response({'client_secret': intent.client_secret})
    except stripe.error.StripeError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
