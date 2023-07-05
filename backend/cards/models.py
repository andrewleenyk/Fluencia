from django.db import models

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

    def __str__(self):
        return self.word