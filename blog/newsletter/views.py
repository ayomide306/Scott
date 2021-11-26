from post.models import *
from newsletter.models import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
"""
    Sending NewsLetter  
"""
def SendLetter(request):
    emails = list(Newsletter.objects.values_list("email", flat=True).all())
    latest = Posts.objects.order_by("-pk")[0:3]
    html = render_to_string(
        "Newsletter/newsletter.htm", context={
            "posts":latest
        }
    )
    send_mail(
        "Daliy Newsletter From Scott Wilson Blogging Site",
        message="newsletter",
        recipient_list=emails,
        from_email="ScottWilson@gmail.com ",
        html_message=html,
    )
    return render(request,"Newsletter/newsletter.htm", context={
            "posts":latest
        })
    
"""
    Oping into Newsletter
"""
def  JoinLetter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if request.user.is_authenticated:
            if Newsletter.objects.filter(email=request.user.email).exists():
                return HttpResponse("Email Already Exists In Our Newsletter")
            else:
                news = Newsletter(email=request.user.email)
                news.save()
                return HttpResponse("You Have Successfully Subcribe To Our Newsletter")
        else:        
            if email == "":
                return HttpResponse("Email Field Can't Be Left Null")
            else:
                if Newsletter.objects.filter(email=email).exists():
                    return HttpResponse("Email Already Exists In Our Newsletter")
                else:
                    news = Newsletter(email=email)
                    news.save()
                    return HttpResponse("You Have Successfully Subcribe To Our Newsletter")
"""
    Oping out of Newsletter
"""
def LeaveLetter(request):
    if request.user.is_authenticated:
        if Newsletter.objects.filter(email=request.user.email).exists():
            news = get_object_or_404(Newsletter, email=request.user.email)
            news.delete()
            return HttpResponse("You Have UnSubcribed From Our Newsletter")
    else:        
        if request.method == "POST":
            pks = request.POST.get("email")
            if Newsletter.objects.filter(email=pks).exists():
                news = get_object_or_404(Newsletter, pk=pk)
                news.delete()
                return HttpResponse("You Have UnSubcribed From Our Newsletter")
        