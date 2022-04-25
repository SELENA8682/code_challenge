# code challenge
## Enviroment
- python
- pydantic
- pytest

##  Files

- main.py : main excute code
- employee_cogfig.py : claa Employee and Pydantic
- input.json : loading employee data in json format
- test_main : test the function with pytest
- README.md : explanation of all the project in high level
- gitignore : to ask for not showing certain file or funtion


## Work flow

### 1.load json file (input.json) 
### 2.define Enployee class and EmployeeJson(BaseModel) class for pydantic
### 3.create employee_list to store json data
### 4.create new_employee_list to get employee data from EmployeeJson which transfer from employee_list
### 5.define fuction get_total_salary from employee_list
### 6.to match manager from employee_dict by manager id
