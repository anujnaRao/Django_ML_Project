from django import forms
from EmployeeInfoApp.models import Employee


class EmpCreate(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
