from core.models import RollCall
from django.forms import ModelForm, CharField
from django import forms


class RollCallModelForm(ModelForm):
    # Override the student field to be used for presentation
    # of student name only

    class Meta:
        model = RollCall
        fields = ['student', 'present']


class RollCallForm(forms.Form):
    student_id = forms.CharField(required=False)
    student_name = forms.CharField(required=False)
    present = forms.BooleanField(required=False)


class RegisterForm(forms.Form):
    stage = forms.CharField(required=False)
    academic_year = forms.CharField(required=False)
    reg_date = forms.DateTimeField()