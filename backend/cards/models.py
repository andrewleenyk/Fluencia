from django.db import models


class Term(models.Model):
    word = models.CharField(max_length=400)
    definition = models.TextField()
    def __str__(self):
        return self.word
class Verb(models.Model):
    word = models.CharField(max_length=400)
    definition = models.TextField()
    conjugations = models.JSONField()
    def __str__(self):
        return self.word

