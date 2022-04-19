
from employee_config import Employee
from main import get_employee_list, get_total_salary


def test_get_total_salary_empty_employee_list():
    totalsalaryvalue = get_total_salary([])
    assert totalsalaryvalue == 0

def test_get_total_salary_None():
    totalsalaryvalue = get_total_salary(None)
    assert totalsalaryvalue == 0

def test_get_total_salary():
    employee_list1= [   
        Employee(1, 'A', None, 100), Employee(2, 'B', None, 200),
        Employee(3, 'C', None, 400), Employee(4, 'D', None, 500)
    ]
    totalsalaryvalue = get_total_salary(employee_list1)
    assert totalsalaryvalue == 1200

def test_get_total_salary_main():
    employee_list = get_employee_list()
    totalsalaryvalue = get_total_salary(employee_list)
    assert totalsalaryvalue == 590000