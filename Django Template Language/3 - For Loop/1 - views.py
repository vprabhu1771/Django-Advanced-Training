from django.shortcuts import render

def list_fruits(request):
    fruits = ['Apple', 'Banana', 'Cherry']
    return render(request, 'frontend/list_fruits.html', {'fruits': fruits})