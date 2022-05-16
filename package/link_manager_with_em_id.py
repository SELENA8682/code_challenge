from package.employee_config import Manager

employee_dict = {}
manager_dict = {}
def link_manager_with_em_id(employee_list):
    for employee in employee_list:
        employee_dict[employee.id] = employee

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