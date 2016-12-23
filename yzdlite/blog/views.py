from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.

def home(request):
    return render(request, 'index.html', locals())

def about(request):
	return render(request, 'about.html', locals())