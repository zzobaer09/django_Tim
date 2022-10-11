from django.urls import path 
from . import views


urlpatterns = [
	path("<int:id>/" , views.index, name="index"),
	# path("" , views.base, name="base"),
	path("" , views.home , name="home"),
]
