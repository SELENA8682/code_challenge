
from package.employee_config import Manager
from package.link_manager_with_em_id import link_manager_with_em_id
from package.load_data import get_employee_list
from package.total_salary import get_total_salary
from package.validate_employee_json import validate_employee_json

def main():
    employee_list = get_employee_list("input.json")

    validate_employee_json(employee_list)

    link_manager_with_em_id(employee_list)
    
    print('-'*20)
    total_salary = get_total_salary(employee_list)
    print(f'Total salary :{total_salary}')
    

if __name__ == '__main__':
    main()

