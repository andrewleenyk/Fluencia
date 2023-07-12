from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Term, Category

def index(request):
    terms = Term.objects.all()
    terms_data = [{'id': term.id, 'word': term.word, 'definition': term.definition} for term in terms]

    data = {
        'terms': terms_data,
    }

    return JsonResponse(data)

def categories(request):
    category_names = Category.objects.values_list('name', flat=True).distinct()
    data = {
        'categories': list(category_names),
    }

    return JsonResponse(data)

def terms_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)

    terms = category.terms.all()
    terms_data = [{'id': term.id, 'word': term.word, 'definition': term.definition} for term in terms]

    data = {
        'terms': terms_data,
    }

    return JsonResponse(data)
