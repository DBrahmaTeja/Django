from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def age_page(request ,age):
    return HttpResponse(
        """
        <h1 style='margin:5rem'>
        """
        +
        age
        +
        """
        </h1>
        """
    )

def index(request):
    return HttpResponse("<h1>Hello World</h1>")

def about_me(response):
    return HttpResponse(
        """
        <h1> About Me</h1>
        <p>
        I am BrahmaTeja ,I graduated from MIT 2023.
        </p>
        """  
    )