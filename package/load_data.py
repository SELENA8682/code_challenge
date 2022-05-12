import json
from typing import List
from package.employee_config import Employee, EmployeeJson
from package.validate_employee_json import validate_employee_json


def get_employee_list(file_name) -> List[Employee]:
    if not file_name:
        return []

    with open(file_name) as file:
        employee_list = json.loads(file.read())

    new_employee_list = []
    for employee in employee_list:
        employee_instance = EmployeeJson(**employee).get_employee()
        new_employee_list.append(employee_instance)
    
    validate_employee_json(new_employee_list)
    return new_employee_list