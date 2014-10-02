from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.template import RequestContext

from core.models import Student
from core.forms import RollCallForm


# Create your views here.
def register(request):

    context = RequestContext(request)
    RollCallFormSet = formset_factory(RollCallForm, extra=0)
    formset = ""

    if request.method == "POST":
        register_formset = RollCallFormSet(request.POST, request.FILES)
        if register_formset.is_valid():
            for data in register_formset.cleaned_data:
                print(data['student_id'])

        else:
            print(register_formset.errors)

    else:

        students = Student.objects.all()
        # Build the hash to be passed to the form
        # as the initial data
        array_of_student_hashes = []
        for student in students:
            student_hash = {'student_id': student.id, 'student_name': student.first_name + " " + student.last_name,
                            'present': False}
            array_of_student_hashes.append(student_hash)

            formset = RollCallFormSet(initial=array_of_student_hashes)

    return render_to_response("register.html",{'formset':formset}, context)