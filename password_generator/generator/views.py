from django.shortcuts import render
import random
import string


def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = 'testing'

    characters = list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend([x.upper() for x in characters])

    if request.GET.get('special'):
        characters.extend(string.punctuation)

    if request.GET.get('numbers'):
        characters.extend([str(x) for x in range(10)])

    length = int(request.GET.get('length', 10))
    thepassword = ''

    for i in range(length):
        thepassword+=random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')