from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    category = models.ForeignKey(Category, related_name="articles", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
