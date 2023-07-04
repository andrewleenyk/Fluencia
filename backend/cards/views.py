from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Term, Verb

def index(request):
    # Retrieve all terms and verbs from the database
    terms = Term.objects.all()
    verbs = Verb.objects.all()

    # Serialize terms and verbs into JSON format
    terms_data = [{'id': term.id, 'word': term.word, 'definition': term.definition} for term in terms]
    verbs_data = [{'id': verb.id, 'word': verb.word, 'definition': verb.definition, 'conjugations': verb.conjugations} for verb in verbs]

    # Create a JSON response with the serialized data
    data = {
        'terms': terms_data,
        'verbs': verbs_data
    }

    return JsonResponse(data)
