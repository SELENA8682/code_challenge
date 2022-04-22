import json
from typing import List

from employee_config import Employee, EmployeeJson




def get_employee_list(file_name) -> List[Employee]:
    if not file_name:
        return []
        
    file = open(file_name)
    employee_list = json.load(file)
    new_employee_list = []
    for employee in employee_list:
        employee_instance = EmployeeJson(**employee).get_employee()
        new_employee_list.append(employee_instance)

    file.close()
    return new_employee_list

def get_total_salary(employee_list):
    if employee_list:
        return sum(em.salary for em in employee_list)
    return 0 

def main():
    employee_list = get_employee_list("input.json") 
    
    employee_dict =  {}
    for employee in employee_list: 
        employee_dict[employee.id] = employee
            
    for employee in employee_list:
           if employee.manager:
                manager = employee_dict.get(employee.manager)
                employee.set_manager(manager)
       
    totalsalary = get_total_salary(employee_list)   


if __name__ == '__main__':
    main()
