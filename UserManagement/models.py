from django.db import models

# Create your models here.

class UserApp (models.Model):
    #CharField requires that you give it a max_length , That’s used not only in the database schema, but in validation
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=90)
    email=models.EmailField(validators=[])
    
    #tells Django what to print when it needs to print out an instance of this model
    def __str__(self) :
        return self.firstname ; 


class Employe(UserApp):
    salaire= models.IntegerField()
    poste = models.TextField(max_length=50)
    
    
    
    
    
   
    

