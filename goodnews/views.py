from django.shortcuts import render
from django.http import HttpResponse

def setup_check(request):
    return HttpResponse("Everything works!")

