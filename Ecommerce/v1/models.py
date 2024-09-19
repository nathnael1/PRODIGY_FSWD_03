from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(username=username)
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)


        return self.create_user(username, email, password, **extra_fields)
    
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    cart = models.ManyToManyField('Products', blank=True, related_name='cart_users')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()
class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_products', default = -1)
    
