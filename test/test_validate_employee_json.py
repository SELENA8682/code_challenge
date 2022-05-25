
from sqlalchemy import true
from service.custom_error import IDError, ManagerError, SalaryAmountError
from service.employee_config import EmployeeJson
from service.load_data import Employee_data


def test_get_employee_list():
    employee_json_list = [generate_employee(1, "Banana", 2, 10000),
    generate_employee(2, "Canana", 2, 50000),
    generate_employee(3, "Danana", 1, 30000),
    generate_employee(4, "Eanana", 1, 40000),
    generate_employee(5, "Fanana", 1, 30000)]
    Employee_data().get_employee_list(employee_json_list)
   

def test_get_employee_list_id_duplicate():
    employee_json_list = [generate_employee(1, "Banana", 2, 10000),
    generate_employee(1, "Canana", 2, 50000),
    generate_employee(3, "Danana", 1, 30000),
    generate_employee(4, "Eanana", 1, 40000),
    generate_employee(5, "Fanana", 1, 30000)]
    Employee_data().get_employee_list(employee_json_list)
    assert IDError

def generate_employee(id,first_name,manager,salary ):
   return EmployeeJson(id=id, first_name=first_name, manager=manager, salary=salary)
