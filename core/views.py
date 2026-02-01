from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    blog = Blog.objects.order_by("-id")
    partners = Partner.objects.all()
    subscribers = Subscriber.objects.all()
    context = {
        'blogs': blog,
        'partners': partners,
        'subscribers': subscribers,
    }

    return render(request, 'index.html', context)
