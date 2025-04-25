from django.contrib import admin

# Register your models here.
from .models import Profile, Document

# Register your models here.
admin.site.register(Profile)
admin.site.register(Document)
