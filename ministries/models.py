from django.db import models


class Ministries(models.Model):
    name = models.CharField(max_length=200)
    minister = models.CharField(max_length=100)
    minister_state = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    website = models.URLField(max_length=200)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name
    