from django.db import models

# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    username= models.CharField(max_length=200,null=False,blank=False)
    email= models.EmailField(null=False,blank=False)
    password=models.CharField(max_length=200)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    def __unicode__(self):
        return self.username
