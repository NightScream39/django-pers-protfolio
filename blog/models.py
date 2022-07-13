from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=80)
    data = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
