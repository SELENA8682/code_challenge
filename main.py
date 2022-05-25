from service.employee_oriented import Employee_organized_data
from service.load_data import Employee_data
from service.custom_error import IDError, ManagerError, SalaryAmountError, SalaryRangeError 

def main():
    try:
        employee_row_data = Employee_data()
        employee_list = employee_row_data.get_employee_list("input_wrong_manager.json")
        employee_organized_data = Employee_organized_data()
        employee_organized_data.link_manager_with_em_id(employee_list)
        print('-'*20)
        total_salary = employee_organized_data.get_total_salary(employee_list)
        print(f'Total salary :{total_salary}')
    
    except IDError:
        print(f"Duplicate ID {employee_list.id}")
    except ManagerError:
        print(f"manager {employee_list.id} is not exist")
    except SalaryRangeError:
        print(f"ID {employee_list.id} ,salary amount not in (50000, 200000) range")
    except SalaryAmountError:
        print(f"ID {employee_list.id} has the wrong salary amount")

if __name__ == '__main__':
    main()

