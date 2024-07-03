import paypalrestsdk
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

paypalrestsdk.configure({
    'mode': settings.PAYPAL_MODE,  # 'sandbox' or 'live'
    'client_id': settings.PAYPAL_CLIENT_ID,
    'client_secret': settings.PAYPAL_CLIENT_SECRET
})

def create_paypal_payment(donation):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "transactions": [{
            "amount": {"total": str(donation.amount), "currency": "USD"}
        }],
        "redirect_urls": {
            "return_url": "http://localhost:8000/payment/execute",
            "cancel_url": "http://localhost:8000/payment/cancel"
        }
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = str(link.href)
                return Response({'approval_url': approval_url})
    else:
        return Response({'error': 'Payment creation failed'}, status=status.HTTP_400_BAD_REQUEST)

def execute_paypal_payment(payment_id, payer_id):
    payment = paypalrestsdk.Payment.find(payment_id)
    if payment.execute({"payer_id": payer_id}):
        return Response({'status': 'Payment executed successfully'})
    else:
        return Response({'error': 'Payment execution failed'}, status=status.HTTP_400_BAD_REQUEST)
