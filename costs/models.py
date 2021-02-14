from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField('date published')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title
