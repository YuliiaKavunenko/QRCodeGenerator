from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length = 20, default = "free")
    purchase_date = models.DateTimeField(auto_now_add=True)
    qr_limit = models.IntegerField(default = 1)