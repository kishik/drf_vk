from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class FriendRequest(models.Model):
    from_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    to_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    is_active = models.BooleanField(default=True)


class Friends(models.Model):
    from_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    to_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    is_active = models.BooleanField(default=True)
