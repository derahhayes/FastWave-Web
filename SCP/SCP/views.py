#from django.http import HttpResponse
from django.shortcuts import render
from django.contrib
from members.models import member


def homepage(request, *args, **kwargs):
   # return HttpResponse("Hello World")
   if request.user.is_authenticated:
      print( request.user.first_name)
   
   member.objects.create()
   queryset = member.objects.all()
   my_title = "SCP - Swim Club Partner"
   my_context = {
       
       "page_title": my_title,
       "members_count": queryset.count()
       
   }
   return render(request, 'home.html', my_context)

def about(request, *args, **kwargs):
   # return HttpResponse("About SCP")
    return render(request, 'about.html')

VALID_CODE ="abc123"

def pw_protected_page(request, *args, **kwargs):
   is_allowed = False
   if request.method== "POST":
      user_pw_sent = request.POST.get("code") or None
      if user_pw_sent == VALID_CODE:
         is_allowed = True
         if is_allowed:
            return render(request, "protected/view.html")
         

def user_only_view(request, *args, **kwargs):
   if not request.user.is_authenticated:
      return redirect("/login")