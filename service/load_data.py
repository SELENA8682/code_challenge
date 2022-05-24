import json
from typing import List
from jsonschema import validate
import jsonschema
from pydantic import ValidationError
from service.employee_config import Employee, EmployeeJson

class Employee_data:
    def get_employee_list(self, file_name) -> List[Employee]:
        try:  
            if not file_name:
                return []

            with open(file_name) as file:
                file_name = json.loads(file.read())
           
            json_object_schema = {
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                    "Employee_json_data": {
                        "type": "array",
                        "description": "a side project with employee",
                        "items": {
                            "type": "object",
                            "properties":{
                            "id":{
                                "description":"employee id",
                                "type":"integer"
                            },
                            "first_name":{
                                "description":"employee name",
                                "type":"string",
                                "pattern": "^[A-Z][a-z]"
                                
                            },
                            "manager":{
                                "description":"manager of employee",
                                "type":"integer"
                                
                            },
                            "salary":{ 
                                "description":"monthly salary",
                                "type":"integer"
                                }
                            }
                            
                        },
                        "required": [
                            "id",
                            "fist_name",
                            "manage",
                            "salary"
                            ]
                        }
                    },
                    "additionalProperties": False
                }
            jsonschema.Draft4Validator.check_schema(json_object_schema)
            validate(instance= file_name, schema= json_object_schema)
        
            new_employee_list = []
            for employee in file_name:
                employee_instance = EmployeeJson(**employee).get_employee()
                new_employee_list.append(employee_instance)       
        
            """
            id shouldn't be duplicated
            manager id should point to an existing id ,manager shouldn't be itself
            """
            employee_list_set = set([])
            for employee in new_employee_list:
                if employee.id in employee_list_set:
                    raise ValueError(f"Duplicate item {employee.id}")
                else:
                    employee_list_set.add(employee.id)
                pass

            for em in new_employee_list:
                if em.manager == None :
                    print(f"top manager {em.name} ")

                elif em.manager not in employee_list_set :
                    raise ValueError(f"manager {em.id} not exist")
            return new_employee_list
            
        except jsonschema.exceptions.ValidationError as err:
            print("errors in schema : ")
            print(jsonschema.Draft4Validator.check_schema(json_object_schema))
            print("errors in data : ")
            print(jsonschema.validate(file_name, json_object_schema))
        except IOError:
            print(file_name, "is not a valid JSON file")
        except ValidationError as e:
            print("ValidationError")
        except Exception as e :
            print(e)