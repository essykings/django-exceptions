from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return "{}".format(self.name)
