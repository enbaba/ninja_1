from django.db import models


class Dojo(models.Model):
    name=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    email =models.CharField(max_length=255)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    desc = models.TextField(default="old dojo") 

class Ninjas(models.Model):
    first_name=models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    email =models.CharField(max_length=255)
    dojo=models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    age =models.IntegerField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

