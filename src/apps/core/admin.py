from django.contrib import admin
from .models.model import User, Doc, Company

admin.site.register([User, Doc, Company])