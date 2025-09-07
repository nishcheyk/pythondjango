from django.http  import HttpResponse
from django.shortcuts import render
def about(request):
        return render(request ,"about.html")
def contact(request):
        return render(request ,"contact.html")
def index(request):
        return render(request ,"index.html")
def shopsingle(request):
        return render(request ,"shop-single.html")
def shop(request):
        return render(request ,"shop.html")
"""def about(request):
         return HttpResponse("this is a shopping app ")"""

