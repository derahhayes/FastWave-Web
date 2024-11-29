#from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from members.models import member
from django.contrib.auth.models import User
from rest_framework import permissions, serializers, viewsets


@login_required
def homepage(request, *args, **kwargs):
   # return HttpResponse("Hello World")
   if request.user.is_authenticated:
      print( request.user.first_name)
   my_title = "FastWave"
   my_context = {
       
       "page_title": my_title,
       
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

class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User


class UserViewSet(viewsets.ModelViewSet):
   """
   API endpoint that allows users to be viewed or edited.
   """

   queryset = User.objects.all().order_by("-date_joined")
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]

#def user_only_view(request, *args, **kwargs):
#   if not request.user.is_authenticated:
#      return redirect("/login")