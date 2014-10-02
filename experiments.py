# Just added my name to try out integration with openshift
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')

from django.forms.models import modelform_factory, modelformset_factory
from core.models import RollCall, Student, AcademicYear, Stage
from core.forms import RollCallForm
from django.forms import CharField
from django.forms.formsets import formset_factory



#RollCallForm1 = modelform_factory(RollCall, form=RollCallForm,
#                                  widgets={"student": CharField()})



"""
First Try
RollCallForm1 = modelform_factory(RollCall, form=RollCallForm,
                                  widgets={"student": CharField()})

rcSet = modelformset_factory(RollCall, fields=('present',))

fset = rcSet()

for form in fset:
    print(form.as_table())
print(fset)

"""

students = Student.objects.all()
for student in students:
    print(student.id)


RollCallFormSet = formset_factory(RollCallForm, extra=0)
# build the hash to be passed to the form
# as the initial data

array_of_student_hashes = []
for student in students:
    student_hash = {'student_id': student.id, 'student_name': student.first_name + " " + student.last_name,
                         'present': False}
    array_of_student_hashes.append(student_hash)


formset = RollCallFormSet(initial=array_of_student_hashes)

for form in formset:
    print(form.as_table())


