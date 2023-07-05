import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth.models import User

def seed_users():
    User.objects.all().delete()
    
    users = [
        {'username': 'funnyguy23', 'password': 'password'},
        {'username': 'musiclover7', 'password': 'password'},
        {'username': 'bookworm99', 'password': 'password'},
        {'username': 'traveljunkie21', 'password': 'password'},
        {'username': 'gamerpro', 'password': 'password'},
        {'username': 'hikingenthusiast', 'password': 'password'},
        {'username': 'artisticmind', 'password': 'password'},
        {'username': 'fitnessfanatic', 'password': 'password'},
        {'username': 'foodieforever', 'password': 'password'},
        {'username': 'doglover123', 'password': 'password'},
    ]

    for user_data in users:
        username = user_data['username']
        password = user_data['password']
        user = User.objects.create_user(username=username, password=password)
        print(f"User {username} created!")


if __name__ == '__main__':
    seed_users()
