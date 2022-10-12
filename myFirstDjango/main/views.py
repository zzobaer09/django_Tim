from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import ToDoList , Item 
from .forms import CreateNewList
# Create your views here.



def index(response , id):
	t = ToDoList
	ls = t.objects.get(id=id)
	return HttpResponse(render(response , "main/list.html",{"ls":ls}))


def home(res):
	return HttpResponse(render(res , "main/home.html", {}))	



def create(response):
	
	if response.method == "POST":
		form = CreateNewList(response.POST)
		if form.is_valid():

			name = form.cleaned_data["name"]
			text = form.cleaned_data["item"]
			complete = form.cleaned_data["check"]

			t = ToDoList(name=name)
			t.save()
			t.item_set.create(text=text , complete=complete)

			return HttpResponseRedirect("/%i"  %t.id)
	else:
		form = CreateNewList()
	return HttpResponse(render(response , "main/create.html", {"form":form}))
