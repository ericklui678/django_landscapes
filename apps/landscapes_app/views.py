from django.shortcuts import render, redirect
import random

def checkPrime(num):
    if num == 1:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def index(request):
    return render(request, 'landscapes_app/index.html')

def landscape(request, num):
    num = int(str(num))
    if checkPrime(num):
        randomIndex = random.randint(0, 4)
        list = ['/static/images/snow.jpg', '/static/images/desert.jpg', '/static/images/forest.jpg', '/static/images/vineyard.jpg', '/static/images/tropical.jpg']
        src = list[randomIndex]
    elif num <= 10:
        src = '/static/images/snow.jpg'
    elif num <= 20:
        src = '/static/images/desert.jpg'
    elif num <= 30:
        src = '/static/images/forest.jpg'
    elif num <= 40:
        src = '/static/images/vineyard.jpg'
    elif num <= 50:
        src = '/static/images/tropical.jpg'
    else:
        return redirect('/')

    context = {
        'src': src
    }
    return render(request, 'landscapes_app/success.html', context)
