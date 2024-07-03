from django.db import models
from users.models import CustomUser

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Donation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    donation = models.OneToOneField(Donation, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20)
    payment_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
