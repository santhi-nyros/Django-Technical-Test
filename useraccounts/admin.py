from django.contrib import admin

# Register your models here.
from .models import UserProfle, Todos

admin.site.register(Todos)
admin.site.register(UserProfle)
