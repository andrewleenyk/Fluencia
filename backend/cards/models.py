from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('beginner', 'beginner'),
        ('intermediate', 'intermediate'),
        ('advanced', 'advanced'),
        ('other', 'other'),
    ]
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='other')

    def __str__(self):
        return self.get_name_display()


class Term(models.Model):
    WORD_TYPE_CHOICES = [
        ('noun', 'noun'),
        ('verb', 'verb'),
        ('adjective', 'adjective'),
        ('adverb', 'adverb'),
        ('other', 'other'),
    ]

    TENSE_CHOICES = [
            ('present', 'present'),
            ('past', 'past'),
    ]

    word = models.CharField(max_length=400)
    definition = models.TextField()
    wordType = models.CharField(max_length=400, choices=WORD_TYPE_CHOICES, default='other')
    conjugations = models.JSONField(default=dict)
    tense = models.CharField(max_length=50, choices=TENSE_CHOICES, default='', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='terms')

    def __str__(self):
        return self.word
    