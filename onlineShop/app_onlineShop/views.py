from django.shortcuts import render

# Create your views here.


# подключаем объект для выполнения http запросов
from django.http import HttpResponse

def index(request):
    return HttpResponse("Успешно!")