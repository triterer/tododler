from django.db import models

# Create your models here.
class Messages(models.Model):
    toUser = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    text = models.TextField()
    toDate = models.DateTimeField()
