from django.shortcuts import render
from django.http import HttpResponse
import random


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = 10
    thepassword = ''
   for x in range(length):
         thepassword += random.choice(characters)

    return render(request, 'generator/password.html' , {'password': generatedpassword})
