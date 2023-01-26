from django.shortcuts import render
from django.http import HttpResponse
from .task import test_func
# Create your views here.
def celerytest(request):
    test_func.delay()
    return HttpResponse("celerytest run")