from django.db import models
from django.contrib.auth.models import AbstractBaseUser
#from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone
from .managers import UserManager
#models here

#User = get_user_model()

class Categorie(models.Model):
    nom = models.CharField(max_length = 255, null = True, blank = True)
    description = models.TextField(max_length = 255)


class Produit(models.Model):
    nom = models.CharField(max_length = 255, null = True, blank = True)
    image = models.ImageField(upload_to = "static/market/img", null=True, blank=True)
    like_number = models.IntegerField()
    buy_number = models.IntegerField()
    qte_stock = models.IntegerField()
    base_price = models.IntegerField()
    description = models.TextField(max_length = 255)
    poster = models.BooleanField(default=False)
    categorie = models.ManyToManyField(Categorie)


class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    address = models.CharField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def __str__(self):
        return self.email  


class Achat(models.Model):
    "class des achats"
    client = models.ForeignKey(User, models.CASCADE)
    produits = models.ManyToManyField(Produit)
    date_achat = models.DateTimeField(auto_now_add=True)