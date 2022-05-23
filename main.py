from service.load_data import Employee_data
from service.main_target import Employee_organized_data 

def main():
    employee_row_data = Employee_data()
    employee_list = employee_row_data.get_employee_list("input.json")
    # employee_row_data.validate_employee_json(employee_list)
    print(employee_list)
    

    # employee_organized_data = Employee_organized_data()
    # employee_organized_data.link_manager_with_em_id(employee_list)

    # print('-'*20)
    # total_salary = employee_organized_data.get_total_salary(employee_list)
    # print(f'Total salary :{total_salary}')
    

if __name__ == '__main__':
    main()

