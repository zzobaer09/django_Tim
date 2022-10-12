from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList , Item 

# Create your views here.



def index(response , id):
	t = ToDoList
	ls = t.objects.get(id=id)
	return HttpResponse(render(response , "main/list.html",{"ls":ls}))


def home(res):
	return HttpResponse(render(res , "main/home.html", {}))	

