from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse

from EmployeeInfoApp.forms import EmpCreate
from EmployeeInfoApp.models import Employee


# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'


def register(request):
    upload = EmpCreate()
    if request.method == 'POST':
        upload = EmpCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return HttpResponse(""" Invalid Form, reload on <a href="{{ url : 'home' }}">Reload</a> """)
    else:
        return render(request, 'index.html', {'insert_form': upload})


def display(request):
    shelf = Employee.objects.all()
    return render(request, 'display.html', {'shelf': shelf})


def update_employee(request, empid):
    empid = int(empid)
    try:
        employee_select = Employee.objects.get(id=empid)
    except Employee.DoesNotExist:
        return redirect('display')
    employee_form = EmpCreate(request.POST or None, instance=employee_select)
    if employee_form.is_valid():
        employee_form.save()
        return redirect('display')
    return render(request, 'index.html', {'insert_form': employee_form})


def delete_employee(request, empid):
    empid = str(empid)
    try:
        employee_select = Employee.objects.get(id=empid)
    except Employee.DoesNotExist:
        return redirect('home')
    employee_select.delete()
    return redirect('home')
