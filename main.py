import json



# naming
# refactory remodule


class Employee:
    def __init__(self, employee_list: dict) -> None:
        self.id = employee_list["id"]
        self.name = employee_list['first_name']
        self.manager = employee_list['manager']
        self.salary = employee_list['salary']
        self.create_employees_list = []  # [id, name]
        print(f"Created {self.name}")

    def sort_emp(self):
        self.create_employees_list = sorted(self.create_employees_list, key= lambda x : x[1])

        

# global
staffs = {}


def hierarchy(id, count):
    add = staffs[id]
    slash = " \t " * count
    print(slash + add.name)
    # print(s.employees)

    if add.employees:  #dont use recursive function
        print(slash + f"Employees of: {add.name}")
        for e, _ in add.employees:
            hierarchy(e, count+1)


def get_employee_list():
    file = open("input.json")
    employee_list = json.load(file)
    file.close()
    return employee_list


def main():
    employee_list = get_employee_list()

    # create object into dict id -> object
    for employees in employee_list:  
        new_object_in_employee_list_dic = Employee(employees)
        staffs[new_object_in_employee_list_dic.id] = new_object_in_employee_list_dic
        # print(s.id)

    # append employees
    manager_id = 0  # assume there is no top manager
    for id in staffs:
        new_object_in_employee_list_dic = staffs[id]
        if new_object_in_employee_list_dic.manager:
            staffs[new_object_in_employee_list_dic.manager].employees.append([new_object_in_employee_list_dic.id, new_object_in_employee_list_dic.name])
        else:
            manager_id = new_object_in_employee_list_dic.id

    #   sum up sealary simutiously
    total_salary = 0
    for id in staffs:
        new_object_in_employee_list_dic = staffs[id]
        new_object_in_employee_list_dic.sort_emp()
        total_salary += new_object_in_employee_list_dic.salary

    # printing staffs tree
    hierarchy(manager_id, 0)
    print(f"total salary: {total_salary}")

    # unit test
    hierarchy(6, 0)  # id = 6


if __name__ == '__main__':
    main()
