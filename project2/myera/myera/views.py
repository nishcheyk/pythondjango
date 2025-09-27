from django.shortcuts import render, redirect
from django.http import HttpResponse

def calculator(request):
    return render(request , 'calculator.html')
