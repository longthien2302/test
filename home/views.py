from django.shortcuts import render
from typing import Text
from django.http import HttpResponse


def home(request):

    return render(
        request,
        "Home.html",
    )


# Create your views here.
