from typing import AsyncContextManager
from django.contrib import admin
from .models import Item
# Register your models here.
admin.site.register(Item)