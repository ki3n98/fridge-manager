from django.shortcuts import render
from django.http import HttpResponse


def loginPage(request):
    return render(request, 'loginPage.html')

def coverPage(request):
    return render(request, 'heroPage.html')