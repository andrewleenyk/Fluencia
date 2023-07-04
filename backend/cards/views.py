from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Term, Verb

def index(request):
    # Retrieve all terms and verbs from the database
    terms = Term.objects.all()
    verbs = Verb.objects.all()

    # Pass the terms and verbs to the template
    context = {
        'terms': terms,
        'verbs': verbs
    }
    return render(request, 'cards/index.html', context)
