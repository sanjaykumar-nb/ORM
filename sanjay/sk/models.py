from django.db import models
from django.contrib import admin
class books(models.Model):
	name=models.CharField(max_length=20);
	author=models.CharField(max_length=20);
	id=models.IntegerField(primary_key=True);
	copies=models.IntegerField();
	price=models.IntegerField();
class booksAdmin(admin.ModelAdmin):
	list_display=("name","author","id","copies","price");