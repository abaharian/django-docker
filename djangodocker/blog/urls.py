from django.urls import path, include
from djangodocker.blog.apis.product import productAPI
urlpatterns = [
    path('product/', productAPI.as_view(), name="product", )
]
