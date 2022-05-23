from jsonschema import validate
import jsonschema


schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
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


data = {
    "Employee_json_data": [
        {
            "id": 1,
            "first_name": "Ssss",
            "manager": 2,
            "salary": 4000,
            "age" : 1
        },
        {
            "id": 3,
            "first_name": "Sdef123",
            "manager": 2,
            "salary": 7000
        },
        {
            "id": 4,
            "first_name": "Smmlp",
            "manager": 1,
            "salary": 12000
        }
    ]
}
print("errors in schema : ")
print(jsonschema.Draft4Validator.check_schema(schema))
print("errors in data : ")
print(jsonschema.validate(data, schema))
