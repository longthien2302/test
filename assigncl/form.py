from django import forms
from django.db.models.fields import IntegerField

from .models import Asscl


class assignform(forms.ModelForm):
    class Meta:
        _STUDENT_ID = "studentID"
        _CLASS_ID = "classID"
        _ASSIGN_DATE = "assigndate"

        model = Asscl

        fields = "__all__"

        widgets = {
            "studentID": forms.Select(
                attrs={
                    "title": _STUDENT_ID,
                    "class": "form-select border-success mt-1 mb-3",
                    "id": "studentID",
                }
            ),
            "classID": forms.Select(
                attrs={
                    "title": _CLASS_ID,
                    "class": "form-select border-success mt-1 mb-3",
                    "id": "clasID",
                }
            ),
            "assigndate": forms.DateInput(
                format=("%d-%m-%y"),
                attrs={
                    "class": "form-control border-success mt-1 mb-3",
                    "type": "date",
                    "title": _ASSIGN_DATE,
                    "id": "assigndate",
                },
            ),
        }

        labels = {
            "classID": _CLASS_ID,
            "classname": _CLASS_ID,
            "assigndate": _ASSIGN_DATE,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["studentID"].empty_label = "Select student"
        self.fields["classID"].empty_label = "Select class"
