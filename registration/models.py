from django.db import models
from main.models import Trening
from django.conf import settings


class Registration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Registrationitem(models.Model):
    registration = models.ForeignKey(Registration,related_name='items',on_delete=models.CASCADE)
    trening = models.ForeignKey(Trening,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def get_total_price(self):
        return self.trening.price * self.quantity