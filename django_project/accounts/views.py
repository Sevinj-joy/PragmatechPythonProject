from django.shortcuts import render
from django.http import HttpResponse

def user_view(request):
    return HttpResponse('<h1>My Users</h1>')
