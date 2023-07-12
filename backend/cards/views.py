from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Term, Category

def index(request):
    # Retrieve all terms and verbs from the database
    terms = Term.objects.all()

    # Serialize terms and verbs into JSON format
    terms_data = [{'id': term.id, 'word': term.word, 'definition': term.definition} for term in terms]

    # Create a JSON response with the serialized data
    data = {
        'terms': terms_data,
    }

    return JsonResponse(data)

def categories(request):
    beginner_category = Category.objects.get(name='beginner')
    intermediate_category = Category.objects.get(name='intermediate')
    advanced_category = Category.objects.get(name='advanced')
