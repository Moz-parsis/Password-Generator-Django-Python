from django.shortcuts import render
from .main import main

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Search(request):
    letters = request.GET.get('letters', '')
    symbols = request.GET.get('symbols', '')
    numbers = request.GET.get('numbers', '')
    letters = int(letters)
    numbers = int(numbers)
    symbols = int(symbols)
    print('this is the letters: ', letters)
    print('this is the symbols: ', symbols)
    print('this is the numbers: ', numbers)

    password = main(letters, symbols, numbers)

    return render(request, 'result.html', {'pass' : password})
