from jsonschema import validate
import jsonschema



def validate_employee_json(employee_json_list):
    """
    id shouldn't be duplicated
    manager id should point to an existing id ,manager shouldn't be itself
    """
    
    employee_json_schema = {
        "properties":{
        "first_name":{
            "description":"Name of the employee",
            "type":"string",
            "pattern": "^[A-Z]{1}[a-z]$"
            },
        },
        }
    try:
        validate(instance= employee_json_list, schema= employee_json_schema)
    except jsonschema.exceptions.ValidationError as err:
        print("wrong pattern")

    employee_list_set = set([])
    for employee in employee_json_list:
        if employee.id in employee_list_set:
             raise ValueError(f"Duplicate item {employee.id}")
        else:
            employee_list_set.add(employee.id)
            pass

    for em in employee_json_list:
        if em.manager == None :
            print("top manager")

        elif em.manager not in employee_list_set :
            raise ValueError(f"manager {em.id} not exist")
        


