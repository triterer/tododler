from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Messages(models.Model):
	class Meta:
		db_table = "messages_db1"
	toUser = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='user1')
	text = models.TextField()
	toDate = models.DateTimeField()
