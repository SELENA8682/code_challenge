# code challenge
## Enviroment
- python
- pydantic 
- pytest
***
##  Doc

* service

    └─ __init__.py

    └─ employee_cogfig.py: class Employee and Pydantic
    
    └─ load_data.py

    └─ total_salary.py

    └─ validate_employee_json.py

* test

    └─ __init__.py

    └─ test_employee_cogfig.py
        
    └─ test_load_data.py

    └─ test_main.py

    └─ test_total_salary.py

    └─ test_validate_employee_json.py


* input.json : loading employee data in json format
* README.md : explanation of all the project in high level
* gitignore : to ask for not showing certain file or funtion
* main.py : main excute code
* setup.md :

***
## Work flow

1. load json file (input.json) 
2. define Enployee class and EmployeeJson(BaseModel)  class for pydantic
3. define Data class for loading and validateing data
4. create new_employee_list to get employee data from EmployeeJson which transfer from employee_list
5. define Target class to to match manager from employee_dict by manager id and fuction get_total_salary from employee_list
6. print the result out 