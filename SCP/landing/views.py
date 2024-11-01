from django.shortcuts import render

# def landng_page Create your views here.


def landing_page_view(request):
    return render(request, "landing/main.html", {})