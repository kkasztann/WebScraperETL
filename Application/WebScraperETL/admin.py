from django.contrib import admin
from .models import Opinion
from .models import Product

admin.site.register(Opinion)
admin.site.register(Product)