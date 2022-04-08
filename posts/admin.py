from django.contrib import admin
from .models import Interest, Post, Report

# Register your models here.

admin.site.register(Post)
admin.site.register(Report)
admin.site.register(Interest)
