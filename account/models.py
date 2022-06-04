from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UsersManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
        email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_staffuser(self, email, password):
        user = self.create_user(
        email,
        password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

      user = self.create_user(
      email,
      password=password,
      )
      user.staff = True
      user.admin = True
      user.save(using=self._db)
      return user





class Myuser(AbstractBaseUser):
    email=models.CharField(primary_key=True,max_length=155)
    active=models.BooleanField(default=True)
    staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)
    time_stamp=models.TimeField(auto_now_add=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    def get_first_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff
    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
    @property
    def is_active(self):
        "Is the user active?"
        return self.active
    
    object=UsersManager()











from django.contrib.auth import get_user_model
from razorpay import Payment
User = get_user_model()

class address(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
