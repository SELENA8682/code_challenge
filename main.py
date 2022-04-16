import json

from employee_config import Employee, EmployeeJson


staffs = {}


def hierarchy(id, count):
    add = staffs[id]
    slash = " \t " * count
    print(slash + add.name)
    # print(s.employees)

    if add.create_employees_list:  # dont use recursive function
        print(slash + f"Employees of: {add.name}")
        for e, _ in add.create_employees_list:
            hierarchy(e, count+1)


def get_employee_list():
    file = open("input.json")
    employee_list = json.load(file)

    new_employee_list = []
    for employee in employee_list:
        new_object_in_employee_dict = EmployeeJson(**employee).get_employee()
        staffs[new_object_in_employee_dict.id] = new_object_in_employee_dict
        new_employee_list.append(new_object_in_employee_dict.id)

    file.close()
    return new_employee_list


def main():
    employee_list = get_employee_list()
    print(len(employee_list))

    # manager_id = None  # assume there is no top manager
    # for id in staffs:
    #     new_object_in_employee_dict = staffs[id]
    #     if new_object_in_employee_dict.manager:
    #         staffs[new_object_in_employee_dict.manager].create_employees_list.append(
    #             [new_object_in_employee_dict.id, new_object_in_employee_dict.name])
    #     else:
    #         manager_id = new_object_in_employee_dict.id

    # #   sum up sealary simutiously
    # total_salary = 0
    # for id in staffs:
    #     new_object_in_employee_dict = staffs[id]
    #     new_object_in_employee_dict.sort_emp()
    #     total_salary += new_object_in_employee_dict.salary

    # # printing staffs tree
    # hierarchy(manager_id, 0)
    # print(f"total salary: {total_salary}")

    # # unit test
    # hierarchy(6, 0)  # id = 6


if __name__ == '__main__':
    main()
