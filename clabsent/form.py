from django import forms
from .models import Clabsent


class absentform(forms.ModelForm):
    class Meta:
        _CASE = "case"
        _STUDENT_ID = "studentID"
        _CLASS_NAME = "classname"
        _DATE_ABSENT = "dateabsent"

        model = Clabsent

        fields = "__all__"

        widgets = {
            "studentID": forms.Select(
                attrs={
                    "title": _STUDENT_ID,
                    "class": "form-select border-success mt-1 mb-3",
                    "id": "studentID",
                }
            ),
            "classname": forms.Select(
                attrs={
                    "title": _CLASS_NAME,
                    "class": "form-select border-success mt-1 mb-3",
                    "id": "clasname",
                }
            ),
            "dateabsent": forms.DateInput(
                format=("%d-%m-%y"),
                attrs={
                    "class": "form-control border-success mt-1 mb-3",
                    "type": "date",
                    "title": _DATE_ABSENT,
                    "id": "dateabsent",
                },
            ),
        }

        labels = {
            "studentID": _STUDENT_ID,
            "classID": _CLASS_NAME,
            "dateabsent": _DATE_ABSENT,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["studentID"].empty_label = "Select student"
        self.fields["classname"].empty_label = "Select class"
