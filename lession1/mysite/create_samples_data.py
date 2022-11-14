import os
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
django.setup()
from redis_cache.models import Product

for i in range(1000):
    Product.objects.create(name="Shoes",description ="Shoes redis_cache for products",price = 102,date_create=timezone.now(),date_modified=timezone.now())
    