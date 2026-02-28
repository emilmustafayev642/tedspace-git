
from django.shortcuts import render 
from core.forms import ContactForm
from .models import *
from django.core.mail import send_mail
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            position = form.cleaned_data.get('position')
            company = form.cleaned_data.get('company')
            message = form.cleaned_data.get('message')
            send_mail(
                'New message for you to check...',
                f"{first_name}  {last_name} - {position} at {company}\nMessage: {message}",
                'emil43835@gmail.com',
                ["elcinaliyev706@gmail.com" , "murad.aghazada@div.edu.az","emil43835@gmail.com" ],
                fail_silently=False
            )
        
    blogs = Blog.objects.order_by("-id")
    partners = Partner.objects.all()
    form = ContactForm()
    subscribers = Subscriber.objects.all()
    context = {
        'blogs': blogs,
        'partners': partners,
        'subscribers': subscribers,
        'form': form
    }

    return render(request, 'index.html', context)

def contact(request):
    
    return render(request, 'indes.html')