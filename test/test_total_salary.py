
from service.employee_config import Employee
from service.employee_oriented import Employee_organized_data
from service.load_data import Employee_data

# testing whether the function behaves as expected.
# apply assertion to ensure the right answer.

employee_organized_data = Employee_organized_data()
employee_row_data = Employee_data()

def test_get_total_salary_empty_employee_list():
    """ test get_total_salary function with the empty employee list"""
    totalsalaryvalue = employee_organized_data.get_total_salary([])
    assert totalsalaryvalue == 0

def test_get_total_salary_None():
    """ test get_total_salary function with no value"""
    totalsalaryvalue = employee_organized_data.get_total_salary(None)
    assert totalsalaryvalue == 0

def test_get_total_salary():
    """ test get_total_salary function with the following employee_list1 list"""
    employee_list1= [   
        Employee(1, 'A', None, 100), Employee(2, 'B', None, 200),
        Employee(3, 'C', None, 400), Employee(4, 'D', None, 500)
    ]
    totalsalaryvalue = employee_organized_data.get_total_salary(employee_list1)
    assert totalsalaryvalue == 1200

def test_get_total_salary_main():
    """ test get_total_salary function with employee list including all employees"""
    employee_list = employee_row_data.get_employee_list('input.json')
    totalsalaryvalue = employee_organized_data.get_total_salary(employee_list)
    assert totalsalaryvalue == 590000


