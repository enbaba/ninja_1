from django.db import models
import re
import bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validate(self, form_data):
        errors = {}
        if len(form_data['first_name']) < 2:
            errors['first_name'] = 'First Name is required'

        if len(form_data['last_name']) < 2:
            errors['last_name'] = 'Last Name  is required'

        if not EMAIL_REGEX.match(form_data['email']):
            errors['email'] = 'Invalid Email'
        
       

        if len(form_data['password']) < 10:
            errors['password'] = 'Password must be at least 10 characters'
        
        if form_data['password'] != form_data['confirm']:
            errors['password'] = 'Passwords do not match'
        

        users_with_email= self.filter(email=form_data['email'])
        if users_with_email:
            errors['email'] ='Email in use'


        return errors


class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# the manager is called in the models to run validation
    objects = UserManager()

# this part of the code shows you what it is 

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
    


