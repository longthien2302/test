from typing import Text
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages


from .models import Studentmanage
from .form import listform


# Create your views here.
def index_list(request):
    studentmanages = Studentmanage.objects.all()
    context = {"studentmanages": studentmanages}
    return render(request, "studentmanage/index_list.html", context)


def add_list(request):
    form = listform(request.POST or None)

    if form.is_valid():
        studentID = request.POST["studentID"]
        fullname = request.POST["fullname"]
        birthday = request.POST["birthday"]

        form.save()

        messages.success(
            request,
            f"Create {studentID} / {fullname} /{birthday} successfull.",
        )

        return redirect(index_list)
    context = {"form": form}
    return render(request, "studentmanage/add_list.html", context)


def delete(request, id):
    studentmanage = get_object_or_404(Studentmanage, id=id)

    studentmanage.delete()

    messages.success(
        request,
        f"Delete {studentmanage.studentID} {studentmanage.fullname} successfull.",
    )
    return redirect(index_list)


def edit(request, id):
    studentmanage = get_object_or_404(Studentmanage, id=id)
    form = listform(request.POST or None, instance=studentmanage)

    if form.is_valid():
        studentID = request.POST["studentID"]
        fullname = request.POST["fullname"]

        form.save()

        messages.success(request, f"Edit {studentID} {fullname} successfull.")

        return redirect(index_list)

    context = {"form": form}

    return render(request, "studentmanage/edit_list.html", context)
