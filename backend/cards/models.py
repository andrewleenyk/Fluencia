from django.db import models


class term(models.Model):
    word = models.TextField()
    definition = models.CharField(max_length=400)
class verb(models.Model):
    word = models.TextField()
    definition = models.CharField(max_length=400)
    conjugations = models.JSONField()

