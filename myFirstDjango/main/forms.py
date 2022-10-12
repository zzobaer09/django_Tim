from django import forms


class CreateNewList(forms.Form):
	name = forms.CharField(label="Name" , max_length=200)
	item = forms.CharField(label="Item" , max_length=255)
	check = forms.BooleanField(label="Complete" , required=False)


