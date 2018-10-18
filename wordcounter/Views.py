from django.http import HttpResponse
from django.shortcuts import render

def Hellow(request):
    #return HttpResponse("Hellow")
    return render(request,"home.html")
def count(request):
    return render(request,"count.html")
