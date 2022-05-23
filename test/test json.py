from jsonschema import validate
import jsonschema

json_object_schema = {
            "title":"Employee json data",
            "description":"a side project with employee",
            "type":"object",
            "properties":{
                "id":{
                    "description":"employee id",
                    "type":"integer"
                },
                "first_name":{
                    "description":"employee name",
                    "type":"string",
                    "pattern": "^[A-Z]{1}[a-z]"
                    
                },
                "manager":{
                    "description":"manager of employee",
                    "type":"integer"
                    
                },
                "salary":{ 
                    "description":"monthly salary",
                    "type":"integer"
                },
            },
            "required":[
                "id",
                "first_name",
                "manager",
                "salary"
            ]
            }

json_data = { 
                
                "id": 1,
                "first_name": "Smk456ev",
                "manager": 1,
                "salary": 5000
                   
            }
try:
    validate(instance= json_data, schema= json_object_schema)

except jsonschema.exceptions.ValidationError as err:
               print("wrong pattern")