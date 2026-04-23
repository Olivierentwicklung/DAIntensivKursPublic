from django.http import HttpRequest
from django.shortcuts import render

# from .models import Employee
# from django.db.models import Avg, Q
# from datetime import date


def employee_overview(request: HttpRequest):

    # Hier die entsprechenden Filter anlegen und die context-Variable definieren, um die Daten an das Template zu übergeben

    return render(request, "employees_app/employee_list.html")
