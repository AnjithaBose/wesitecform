from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings




# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('msg')
        send_mail(name,message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
        return render(request,'Contact/send_email.html',{'email':email})

    return render(request,'Contact/index.html',{})





