from typing import Optional
from pydantic import BaseModel


class Employee:
    def __init__(self, id, first_name ,manager, salary) :
        self.id = id
        self.name = first_name
        self.manager = manager
        self.salary = salary
    
    def get_manager() -> 'Employee':
        pass
     
#DTO data transfer object
class EmployeeJson(BaseModel):
    id: int
    first_name: str
    manager: Optional[int] = None
    salary: int

    def get_employee(self):
        return Employee(self.id, self.first_name, self.manager, self.salary)
