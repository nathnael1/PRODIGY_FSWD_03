from django.contrib import admin
from .models import User, Products

# Register your models here.
admin.site.register(User)
admin.site.register(Products)
# To create a superuser, run the following command in your terminal:
# python manage.py createsuperuser