from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Django!</h1>")


def profile(request):
    context = {
        "name": "Jerry",
        "age": 46,
        "height": 164,
        "weight": 58.6,
    }

    return JsonResponse(context)
