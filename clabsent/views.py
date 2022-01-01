from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages


from .models import Clabsent
from .form import absentform

# Create your views here.
def index_absent(request):
    clabsents = Clabsent.objects.all()
    context = {"clabsents": clabsents}
    return render(request, "index_absent.html", context)


def add_absent(request):
    form = absentform(request.POST or None)

    if form.is_valid():
        studentID = request.POST["studentID"]
        classname = request.POST["classname"]
        form.save()

        messages.success(
            request,
            f"Create {studentID}/{classname} successfull.",
        )

        return redirect(index_absent)
    context = {"form": form}
    return render(request, "add_absent.html", context)


def delete(request, id):
    clabsent = get_object_or_404(Clabsent, id=id)

    clabsent.delete()

    messages.success(
        request,
        f"Delete {clabsent.studentID} {clabsent.classname} successfull.",
    )
    return redirect(index_absent)


def edit(request, id):
    studentmanage = get_object_or_404(Clabsent, id=id)
    form = absentform(request.POST or None, instance=studentmanage)

    if form.is_valid():
        studentID = request.POST["studentID"]
        classname = request.POST["classname"]
        form.save()

        messages.success(
            request,
            f"Create {studentID}/{classname} successfull.",
        )

        return redirect(index_absent)

    context = {"form": form}

    return render(request, "edit_absent.html", context)
