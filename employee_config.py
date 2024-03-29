
from typing import Optional
from pydantic import BaseModel


class Employee:
    """
    This is a class for all the employees .

    Attributes:
    -----------
        id (int): The id number of each employee.
        first_name (str):The first name of each employee.
        manager (int): To show whether employee has manager, if it has manager reveals the manager id ; while shows  null
        salary (int): salary of each employee.
    """

    def __init__(self, id, first_name, manager, salary):
        """
        Construct all the necessary attributes for the employee object.

        Parameters
        ---
            id (int): The id number of each employee.
            first_name (str):The first name of each employee.
            manager (int): To show whether employee has manager, if it has manager reveals the manager id ; while shows  null
            salary (int): salary of each employee.

        Methods
        ---
            get_manager():
                to load manager's instance from employee

            set_manager(manager):
                 to link employee and manager
        """
        self.id = id
        self.name = first_name
        self.salary = salary
        self.manager = manager
        self.manager_instance = None

    def get_manager(self) -> 'Employee':
        """
            to get manager info 

             Returns
             -------
                manager_instance: 
                    the variable in Employee to put manager info
        """
        return self.manager_instance

    def set_manager(self, manager):
        """
        to link employee and manager

        Parameters
        ----------
        manager : 
            link the manager info in to manager instance
        """
        self.manager_instance = manager
        manager.employees.append(self)

    def print_name(self):
        print(self.name)


class Manager(Employee):
    def __init__(self, employee):
        super().__init__(employee.id, employee.name, employee.manager, employee.salary)
        self.manager_instance = employee.manager_instance
        self.employees = []
    
    def print_name(self):
        super().print_name()
        print(f'Employee of {self.name}')
        for employee in self.employees:
            print("\t " + employee.name)
        print('-'*20)

# DTO data transfer object
class EmployeeJson(BaseModel):
    id: int
    first_name: str
    manager: Optional[int] = None
    salary: int

    def get_employee(self):
        """
            to get all the employee info 

             Returns
             -------
               return all the parameters in class EmployeeJson(BaseModel)
        """
        return Employee(self.id, self.first_name, self.manager, self.salary)
