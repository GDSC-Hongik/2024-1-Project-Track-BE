from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Review

UserAdmin.fieldsets += ('Custom fields', {'fields': ('nickname', 'profile_pic', 'intro',)}),

admin.site.register(User, UserAdmin)

admin.site.register(Review)
