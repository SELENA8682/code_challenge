def get_total_salary(employee_list):
    if employee_list:
        return sum(em.salary for em in employee_list)
    return 0
