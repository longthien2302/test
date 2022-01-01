from django import forms
from .models import Studentmanage


class listform(forms.ModelForm):
    class Meta:
        _STUDENT_ID = "studentID"
        _FULL_NAME = "fullname"
        _PHONE = "phone"
        _EMAIL = "email"
        _BIRTHDAY = "birthday"
        _COURSE = "course"

        model = Studentmanage

        fields = "__all__"

        widgets = {
            "studentID": forms.Textarea(
                attrs={
                    "cols": 5,
                    "rows": 1,
                    "required": True,
                    "placeholder": _STUDENT_ID,
                    "title": _STUDENT_ID,
                    "class": "form-control border-success mt-1 mb-3",
                    "id": "studentID",
                }
            ),
            "fullname": forms.TextInput(
                attrs={
                    "placeholder": _FULL_NAME,
                    "title": _FULL_NAME,
                    "class": "form-control border-success mt-1 mb-3",
                    "minlength": 3,
                    "maxlength": 50,
                    "id": "fullmname",
                }
            ),
            "birthday": forms.DateInput(
                format=("%d-%m-%y"),
                attrs={
                    "class": "form-control border-success mt-1 mb-3",
                    "type": "date",
                    "title": _BIRTHDAY,
                    "id": "birthday",
                },
            ),
            "phone": forms.TextInput(
                attrs={
                    "title": _PHONE,
                    "placeholder": _PHONE,
                    "class": "form-control border-success mt-1 mb-3",
                    "id": "phone",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "title": _EMAIL,
                    "placeholder": _EMAIL,
                    "class": "form-control border-success mt-1 mb-3",
                    "id": "email",
                }
            ),
            "course": forms.Select(
                attrs={
                    "title": _COURSE,
                    "class": "form-select border-success mt-1 mb-3",
                    "id": "course",
                }
            ),
        }

        labels = {
            "studentID": _STUDENT_ID,
            "fullname": _FULL_NAME,
            "phone": _PHONE,
            "email": _EMAIL,
            "birthday": _BIRTHDAY,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["course"].empty_label = "Select course"
