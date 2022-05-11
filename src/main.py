
from src.employee_config import Manager
from src.load_data import get_employee_list
from src.total_salary import get_total_salary

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

    for employee in final_list:
        employee.print_name()
    
    print('-'*20)
    total_salary = get_total_salary(final_list)
    print(f'Total salary :{total_salary}')
    

if __name__ == '__main__':
    main()

