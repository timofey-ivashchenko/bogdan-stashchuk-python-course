class Employee:

    all_employees = []

    def __init__(
            self, id: int,
            first_name: str,
            last_name: str,
            job_title: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title

    def __str__(self):
        return f'[{self.id}] {self.first_name} {self.last_name}, {self.job_title}'

    @staticmethod
    def add_employee(first_name: str, last_name: str, job_title: str):
        new_id = len(Employee.all_employees) + 1
        employee = Employee(new_id, first_name, last_name, job_title)
        Employee.all_employees.append(employee)
        return employee


employee_1 = Employee.add_employee('David', 'Roberts', 'manager')
employee_2 = Employee.add_employee('Clint', 'Wallace', 'developer')
employee_3 = employee_1.add_employee('Ray', 'Freeman', 'designer')
employee_4 = employee_2.add_employee('Bob', 'Collins', 'accountant')

print('THE COMPANY STAFF')
print()

for employee in Employee.all_employees:
    print(employee)

print()
print('Total employees:', len(Employee.all_employees))
