from django.shortcuts import render
from django.http import HttpResponse
from news.models import *


# Create your views here.

def index(request):
    context = {}
    context["header_list"] = HeaderModel.objects.all()
    context["news_list"] = News.objects.all()
    return render(request, "index.html", context)


