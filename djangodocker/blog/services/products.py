from django.db.models import QuerySet
from djangodocker.blog.models import product

def create_product(name : str) -> QuerySet[product] :
    return product.objects.create(name = name)

    