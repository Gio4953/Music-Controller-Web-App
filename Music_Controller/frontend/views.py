from django.shortcuts import render

# Create your views here.


def index(request, *args, **kwargs):
    return render(request, 'C:/Users/Giorgi/Desktop/Music-Controller-Web-App/Music_Controller/frontend/templates/frontend/index.html')