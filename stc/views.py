from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .models import Stc
from .form import stcform

# Create your views here.


def stc(request):
    STC = Stc.objects.all()
    context = {"STC": STC}
    return render(request, "index_stc.html", context)


def add_stc(request):
    form = stcform(request.POST or None)

    if form.is_valid():
        classID = request.POST["classID"]
        classname = request.POST["classname"]

        form.save()

        messages.success(
            request,
            f"Create {classID} / {classname}  successfull.",
        )

        return redirect(stc)
    context = {"form": form}
    return render(request, "add_stc.html", context)


def delete(request, id):
    stclass = get_object_or_404(Stc, id=id)

    stclass.delete()

    messages.success(
        request,
        f"Delete {stclass.classID} {stclass.classname} successfull.",
    )
    return redirect(stc)


def edit(request, id):
    studentmanage = get_object_or_404(Stc, id=id)
    form = stcform(request.POST or None, instance=studentmanage)

    if form.is_valid():
        classID = request.POST["classID"]
        classname = request.POST["classname"]

        form.save()

        messages.success(request, f"Edit {classID} {classname} successfull.")

        return redirect(stc)

    context = {"form": form}

    return render(request, "edit_stc.html", context)
