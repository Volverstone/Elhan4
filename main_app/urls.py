from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/text/', views.text_response, name='text_response'),
    path('api/html/', views.html_response, name='html_response'),
]
