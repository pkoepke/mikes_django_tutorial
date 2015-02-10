from django.contrib import admin

# Register your models here.
from article.models import Article # import the classes that define our data

admin.site.register(Article) # register our class so the admin site knows it exists.
