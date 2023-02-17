from django.db import models
from django.contrib.auth.models import AbstractUser 
from .managers import CustomUserManager
from django.core.validators import RegexValidator


# Create your models here.


####### we will replace Django's default user model with a custom one that uses email as the identifier ########


class CustomUser(AbstractUser):
    
    #AbstractUser defines a username, so we are overriding the model to "delete" the username field
    username = None
    
    #AbstractUser already defines an email field, but it's not unique, so we override it as well
    email = models.EmailField(unique=True)
    
    class Meta:
        db_table = ''
    
    #This sets the field that will act as a unique identifier of the User model. We are setting it to the email field.
    USERNAME_FIELD = "email"
    
    #By setting REQUIRED_FIELDS to an empty list, 
    # you are telling Django that the only required field for the User model is the email field, and that all other fields are optional
    REQUIRED_FIELDS = []
    
    
    #tells Django what to print when it needs to print out an instance of this model , it simply returns a string representation of the object.
    def __str__(self) :
        return self.email ; 
    
    objects = CustomUserManager()


class Employee(CustomUser):
    salaire= models.IntegerField()
    #CharField requires that you give it a max_length , That’s used not only in the database schema, but in validation also.
    poste= models.CharField(max_length=50)
    
    
        



        
    
        
    
    
    
    
    
    
    
   
    

