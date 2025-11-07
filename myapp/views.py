from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

def text_response(request):
    return HttpResponse("Привет! Это текстовый ответ от Django API :)")

def html_response(request):
    context = {"title": "Пример шаблона", "message": "Это HTML-страница из шаблона"}
    return render(request, "example.html", context)

def home(request):
    return render(request, "base.html")


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'myapp/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'myapp/post_detail.html', {'post': post})