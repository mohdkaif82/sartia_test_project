from django.db import models
from users.models import MyUser

# Create your models here.
class AccountVerify(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    link = models.CharField(max_length=500)
    verify = models.BooleanField(default=False)

    def __str__(self):
        return self.user