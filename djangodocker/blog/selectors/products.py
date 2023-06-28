from django.db.models import QuerySet
from djangodocker.blog.models import product

def get_products() -> QuerySet[product] :
    return product.objects.all()

    