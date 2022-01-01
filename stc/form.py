from django import forms

from .models import Stc


class stcform(forms.ModelForm):
    class Meta:
        _CLASS_ID = "classID"
        _CLASS_NAME = "classname"

        model = Stc

        fields = "__all__"

        widgets = {
            "classID": forms.Textarea(
                attrs={
                    "cols": 5,
                    "rows": 1,
                    "required": True,
                    "placeholder": _CLASS_ID,
                    "title": _CLASS_ID,
                    "class": "form-control border-success mt-1 mb-3",
                    "id": "classID",
                }
            ),
            "classname": forms.TextInput(
                attrs={
                    "placeholder": _CLASS_NAME,
                    "title": _CLASS_NAME,
                    "class": "form-control border-success mt-1 mb-3",
                    "minlength": 3,
                    "maxlength": 50,
                    "id": "classname",
                }
            ),
        }

        labels = {
            "classID": _CLASS_ID,
            "stcname": _CLASS_NAME,
        }
