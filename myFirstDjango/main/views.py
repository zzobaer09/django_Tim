from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import ToDoList , Item 
from .forms import CreateNewList
# Create your views here.



def index(response , id):
	t = ToDoList
	ls = t.objects.get(id=id)

	if response.method == "POST":

		if response.POST.get("save"): 

			for item in ls.item_set.all():
				if response.POST.get("c"+str(item.id)) == "checked":
					item.complete = True 
				else:
					item.complete = False

				item.save()
		elif response.POST.get("newItem"):
			txt = response.POST.get("newItemField")

			if len(txt) > 2:
				ls.item_set.create(text=txt , complete=False)





	return HttpResponse(render(response , "main/list.html",{"ls":ls}))


def home(res):
	return HttpResponse(render(res , "main/home.html", {}))	



def create(response):
	
	if response.method == "POST":
		form = CreateNewList(response.POST)
		if form.is_valid(): 
			name = form.cleaned_data["name"]
			t = ToDoList(name=name)
			t.save()

			return HttpResponseRedirect("/%i"  %t.id)
	else:
		form = CreateNewList()
	return HttpResponse(render(response , "main/create.html", {"form":form}))
