
from service.employee_config import EmployeeJson
from service.load_data import Data


def test_validate_employee_json():
    employee_json_list = [generate_employee(1, "Banana", 2, 10000),
    generate_employee(2, "Canana", 2, 50000),
    generate_employee(3, "Danana", 1, 30000),
    generate_employee(4, "Eanana", 1, 40000),
    generate_employee(5, "Fanana", 1, 30000)]
    Data().validate_employee_json(employee_json_list)

def generate_employee(id,first_name,manager,salary ):
   return EmployeeJson(id=id, first_name=first_name, manager=manager, salary=salary)
