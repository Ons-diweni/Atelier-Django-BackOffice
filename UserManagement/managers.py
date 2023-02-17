from django.contrib.auth.models import  BaseUserManager


#The user manager is called when you call the createsuperuser command 
#and the default one is only compatible if the user model defines the following fields:
#username, email, is_staff, is_active, is_superuser, last_login, date_joined. Our custom model no longer defines username,
#so it's incompatible with the default one.

class CustomUserManager(BaseUserManager): 

    def create_user(self, email,password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
        )

        #user.set_password(password)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self,email,password): 
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
     
    