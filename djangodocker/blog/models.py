from django.db import models
from djangodocker.common.models import BaseModel
# Create your models here.

class product(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)

