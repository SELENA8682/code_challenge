import json

from employee_config import Employee, EmployeeJson




def get_employee_list(file_name):
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
    
    manager_dict =  {}
    for employee in employee_list: 
        if employee not in  manager_dict:
            return 0
        else:
           manager_dict[id].append([Employee.id, Employee.firstname])
       
       
    totalsalary = get_total_salary(employee_list)   


if __name__ == '__main__':
    main()
