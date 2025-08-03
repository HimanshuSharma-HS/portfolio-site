from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import FileResponse, Http404
from . models import Hero,About,Technology, SkillCategory,Education,Projects,Achievements,Contact,ContactMe,Logo,Footer

# Create your views here.


def index(request):
    print("Index view loaded")
    products= Hero.objects.all()
    about=About.objects.all()
    course=Education.objects.all()
    projects = Projects.objects.prefetch_related('technology').all()
    achievements=Achievements.objects.all()
    contact=Contact.objects.all()
    categories = SkillCategory.objects.prefetch_related('skills').all()
    logo=Logo.objects.all()
    footer=Footer.objects.all()

    



    if request.method == "POST":
        print("POST received!")
        print(request.POST)
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")


        print("Data received:")
        print("Name:", name)
        print("Email:", email)
        print("Subject:", subject)
        print("Message:", message)

        if name and email and subject and message:
            ContactMe.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            print("✔ Saved successfully!")
            
        else:
            print("❌ Missing form fields")
         
        # Send email
        try:
            send_mail(
               subject=f"New Contact: {subject}",
               message=f"From: {name} <{email}>\n\n{message}",
               from_email=settings.DEFAULT_FROM_EMAIL,
               recipient_list=["hs360257@gmail.com"],
               fail_silently=False,
            )
            print("✔ Mail sent!")
        except Exception as e:
              print("❌ Mail failed:", e)

        return redirect("Portfolio")

        # Save to the database
        # ContactMe.objects.create(
        #     name=name,
        #     email=email,
        #     subject=subject,
        #     message=message
        # )
        
        # return redirect("Portfolio")
    
    
    
    

    return render(request,"index.html",{'products':products,
                                        'about':about,
                                        'course':course,
                                        'project':projects,
                                        'achievement':achievements,
                                        'cont':contact,
                                        'categories':categories,
                                        'projects':projects,
                                        'logo':logo,
                                        'footer':footer})














# from .models import SkillCategory

# def index(request):
#     categories = SkillCategory.objects.prefetch_related('skills').all()
#     return render(request, "index.html", {'categories': categories})
