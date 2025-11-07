from django.http import HttpResponse
from django.shortcuts import render

def text_response(request):
    return HttpResponse("Привет! Это текстовый ответ от Django API :)")

def html_response(request):
    context = {"title": "Пример шаблона", "message": "Это HTML-страница из шаблона"}
    return render(request, "myapp/example.html", context)
