from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=50, default="")
    category = models.CharField(max_length=60)

    def __str__(self):
        return self.name

