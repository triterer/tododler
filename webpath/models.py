from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Messages(models.Model):
    toUser = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='webtouser')
    text = models.TextField()
    toDate = models.DateTimeField()
