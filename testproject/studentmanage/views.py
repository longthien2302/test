from typing import Text
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    date = datetime.now()
    day = datetime.now().date()
    number = 10
    return render(
        request, "index.html", {"abc": number, "currentime": date, "day": day}
    )


def test(request):
    id = 5
    date = datetime.now()
    day = datetime.now().date()
    number = 15
    return render(request, "test.html", {"abc": number, "currentime": date, "id": id})
