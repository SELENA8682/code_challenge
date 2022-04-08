import json



# naming
# refactory remodule


class Employee:
    def __init__(self, employee_list: dict) -> None:
        self.id = employee_list["id"]
        self.name = employee_list['first_name']
        self.manager = employee_list['manager']
        self.salary = employee_list['salary']
        self.employees = []  # [id, name]
        print(f"Created {self.name}")

    def sort_emp(self):
        self.employees = sorted(self.employees, key= lambda x : x[1])

        

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
        add = Employee(employees)
        staffs[add.id] = add
        # print(s.id)

    # append employees
    Manager_id = 0  # assume there is no top manager
    for id in staffs:
        add = staffs[id]
        if add.manager:
            staffs[add.manager].employees.append([add.id, add.name])
        else:
            Manager_id = add.id

    #   sum up sealary simutiously
    total_salary = 0
    for id in staffs:
        add = staffs[id]
        add.sort_emp()
        total_salary += add.salary

    # printing staffs tree
    hierarchy(Manager_id, 0)
    print(f"total salary: {total_salary}")

    # unit test
    hierarchy(6, 0)  # id = 6


if __name__ == '__main__':
    main()
