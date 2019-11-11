from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#class Coreuser(models.Model):
    #id = models.IntegerField(primary_key = True)
#    name = models.CharField(max_length = 20, unique = True)#(db.String(20), nullable = False, unique = True)
#    password = models.CharField(max_length = 20)#(db.String(20), nullable = False)

class Messages(models.Model):
    #id = model.IntegerField()#(db.Integer, primary_key = True)
    #class Meta:
    #    db_table = "messages_db"
    toUser = models.ForeignKey(User,on_delete=models.DO_NOTHING)#(db.String(20),db.ForeignKey('user.name'), nullable = False)
    text = models.TextField()
    toDate = models.DateTimeField()#(db.Date, default = date.today)

    #question_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')