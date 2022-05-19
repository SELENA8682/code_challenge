def get_total_salary(employee_list):
    try:
        if employee_list:
            return sum(em.salary for em in employee_list)
    except TypeError:
        print("salary should be integer")
    return 0
