def validate_employee_json(employee_json_list):
    """
    id shouldn't be duplicated
    manager id should point to an existing id ,manager shouldn't be itself
    """
    # employee_json_set = set([em.id for em in employee_json_list])
    # manager_employee_set = set([em.manager for em in employee_json_list])
    
    # if len(employee_json_list) != len(employee_json_set) :
    #     raise ValueError(f"id is duplicate")
    
    # #comment
    # #assumption
    # none_in_manager_employee_set = [filter(None,manager_employee_set)]
    # if len(manager_employee_set.union(employee_json_set))-len(none_in_manager_employee_set) != len(employee_json_set):
    #    raise ValueError(f"manager i s not exist")
    
    # return employee_json_set

    employee_list_set = set([])
    for employee in employee_json_list:
        if employee.id in employee_list_set:
             raise ValueError(f"Duplicate item {employee.id}")
        else:
            employee_list_set.add(employee.id)

    for manager in employee_json_list:
        if manager.id not in employee_list_set:
            raise ValueError(f"wrong manager")
    
    return employee_list_set
        
         
         

    

