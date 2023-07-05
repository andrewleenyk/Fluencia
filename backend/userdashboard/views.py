from django.http import JsonResponse
from django.contrib.auth.models import User

def UserListView(request):
    users = User.objects.all()
    user_list = [{'id': user.id, 'username': user.username} for user in users]
    return JsonResponse({'users': user_list})
