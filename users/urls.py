from django.urls import path, include

app_name = 'users'

url_patter = [
    path('', include('django.contrib.auth.urls')),
]