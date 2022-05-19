import json
from typing import List
from pydantic import ValidationError
from package.employee_config import Employee, EmployeeJson


def get_employee_list(file_name) -> List[Employee]:
    try:
        if not file_name:
            return []

        with open(file_name) as file:
            employee_list = json.loads(file.read())

        new_employee_list = []
        for employee in employee_list:
            employee_instance = EmployeeJson(**employee).get_employee()
            new_employee_list.append(employee_instance)       
        return new_employee_list
    
   
    except IOError:
        print(file_name, "is not a valid JSON file")
    except TypeError:
        print("wrong type")
    except ValidationError as e:
        print("ValidationError")
    

    except Exception as e :
        print(e)
    
    
    