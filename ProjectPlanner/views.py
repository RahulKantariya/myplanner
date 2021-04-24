from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def cover(request):
    return render(request,'cover.html')