def validate_employee_json(employee_json_list):
    """
    id shouldn't be duplicated
    manager id should point to an existing id ,manager shouldn't be itself
    """
    employee_list_set = set([])
    for employee in employee_json_list:
        if employee.id in employee_list_set:
             raise ValueError(f"Duplicate item {employee.id}")
        else:
            employee_list_set.add(employee.id)

    for em in employee_json_list:
        if em.manager == None :
            print("top manager")

        elif em.manager not in employee_list_set :
            raise ValueError(f"manager {em.id} not exist")
        


