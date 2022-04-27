import json
from typing import List

from employee_config import Employee, EmployeeJson, Manager


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

    employee_dict = {}
    for employee in employee_list:
        employee_dict[employee.id] = employee

    manager_dict = {}
    for employee in employee_list:
        manager_id = employee.manager
        if not manager_id:
            continue

        manager = None

        if manager_id in manager_dict:
            manager = manager_dict[manager_id]
        else:
            employee_m = employee_dict.pop(manager_id)
            manager = Manager(employee_m)
            manager_dict[manager_id] = manager

        employee.set_manager(manager)

    employee_dict_list = [employee for employee in employee_dict.values()]
    employee_dict_list.sort(key=lambda e: e.name)
    
    manager_dict_list = [manager for manager in manager_dict.values()]
    manager_dict_list.sort(key=lambda m: m.manager_instance != None)

    final_list = manager_dict_list + employee_dict_list

    #TODO print the final information for each employee from final_list, print total salary as well


if __name__ == '__main__':
    main()
