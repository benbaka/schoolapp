from django.contrib import admin
from core.models import Student, Stage, AcademicYear, RollCall
# Register your models here.
admin.site.register(Student)
admin.site.register(Stage)
admin.site.register(AcademicYear)
admin.site.register(RollCall)