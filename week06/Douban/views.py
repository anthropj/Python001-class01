from django.shortcuts import render
from .models import Douban1

# from django.http import HttpResponse

# Create your views here.
def books_short(request):
    shorts = Douban1.objects.filter(new_star__gt=3)
    return render(request,'result.html',locals())