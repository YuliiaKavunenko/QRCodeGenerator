from django.db import models
from django.contrib.auth.models import User
# Create your models here
class QRCodes(models.Model):
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    link = models.TextField()
    picture = models.ImageField(upload_to = 'images/')
    date = models.DateTimeField(auto_now_add = True)