from datetime import date

from django.db.models import Avg, Q
from django.http import HttpRequest
from django.shortcuts import render

from .models import Employee


def employee_overview(request: HttpRequest):

    # Hier die entsprechenden Filter anlegen und die context-Variable definieren, um die Daten an das Template zu übergeben

    all_employees = Employee.objects.select_related("department").all()

    all_employees_salary_gt_3000 = all_employees.filter(salary__gt=3000)

    all_employees_salary_gte_5000 = all_employees.filter(salary__gte=5000)
    count_all_employees_salary_gte_5000 = len(all_employees_salary_gte_5000)

    avg_salary_in_sales_team = all_employees.filter(department__name="Sales").aggregate(
        Avg("salary", default=0)
    )

    avg_salary_in_sales_team_rounded_to_2_decimal_places = round(
        avg_salary_in_sales_team["salary__avg"], 2
    )

    not_hr_employees_with_special_hire_date = all_employees.exclude(
        Q(department__name="HR")
    ).filter(hire_date__lt=date(2022, 1, 1))

    context = {
        "all_employees": all_employees,
        "all_employees_salary_gt_3000": all_employees_salary_gt_3000,
        "count_all_employees_salary_gte_5000": count_all_employees_salary_gte_5000,
        "avg_salary_in_sales_team_rounded_to_2_decimal_places": avg_salary_in_sales_team_rounded_to_2_decimal_places,
        "not_hr_employees_with_special_hire_date": not_hr_employees_with_special_hire_date,
    }

    return render(request, "employees_app/employee_list.html", context)
