from django.contrib import admin
from .models import Product
from .models import ProductDetail
from .models import Opinion

admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(Opinion)
