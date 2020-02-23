from django.db import models


# Create your models here.
class signup(models.Model):
    fullname = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50,null=True)
    telephone = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.email
        

class Document(models.Model):
    document = models.FileField(upload_to='documents/')
