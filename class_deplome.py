"""
1. Create structure for department:
 a) There are 3 types of employee: developer, designer and manager
 b) Each employee has: first name, second name, salary, experiance (years) and manager
 c) Each designer has effectivness coefficient(0-1)
 d) Each manager has team of developers and designers.
 e) Department should have list of managers(which have their own teams)
 
 f) Department should be able to give salary (for each employee 
 message: "@firstName@ @secondName@: got salary: @salaryValue@")
 
 g) Each employee gets the salary, defined in field Salary. 
 If experiance of employee is > 2 years, he gets bonus + 200$, 
 if experiance is > 5 years, he gets salary*1.2 + bonus 500
 
 h) Each designer gets the salary = salary*effCoeff
 i) Each manager gets salary +
   ii) 200$ if his team has >5 members
   iii) 300$ if his team has >10 members
   iiii) salary*1.1 if more than half of team members are developers.
 j) Redefine string representation for employee as follows:
"@firstName@ @secondName@, manager:@manager secondName@, experiance:@experiance@" 
"""


class Department:
    list_managers = set()

    def give_salary(self):
        salary_employee = self.first_name + ' ' + \
            self.second_name + ': got salary: ' + str(self.salary)
        print(salary_employee)


class Employee(Department):
    def __init__(self, first_name, second_name, salary, experiance, manager):
        self.first_name = first_name
        self.second_name = second_name
        self.experiance = experiance
        self.salary = salary
        if self.experiance > 5:
            self.salary = self.salary * 1.1 + 500
        elif self.experiance > 2:
            self.salary = self.salary + 200
        self.manager = manager
        if self.manager:
            Department.list_managers.add(self.manager)

    def __str__(self):
        answer_line = '[ ' + self.first_name + ' ' + self.second_name + \
            '] manager: [' + self.manager + \
            '] experiance: [ ' + str(self.experiance) + ' ]'
        return answer_line


class Manager(Employee):
    manager_team = {'developer': [], 'designer': []}

    def __init__(self, first_name, second_name,
                 salary, experiance, manager=None):
        super().__init__(first_name, second_name, salary, experiance, manager)

    def give_salary(self):
        length, dev = 0
        for item in Manager.manager_team.keys():
            if item == 'developer':
                dev = len(Manager.manager_team[item])
            length += len(Manager.manager_team[item])

        if (length // 2) < dev:
            self.salary = self.salary * 1.1
        elif length > 10:
            self.salary = self.salary + 300
        elif length > 5:
            self.salary = self.salary + 300

        salary_employee = self.first_name + ' ' + \
            self.second_name + ': got salary: ' + str(self.salary)
        print(salary_employee)


class Developer(Employee):

    def __init__(self, first_name, second_name, salary, experiance, manager):
        super().__init__(first_name, second_name, salary, experiance, manager)
        Manager.manager_team['developer'].append(self.first_name)


class Designer(Employee):

    def __init__(self, first_name, second_name, salary,
                 experiance, manager, coefficient):
        super().__init__(first_name, second_name, salary, experiance, manager)
        self.coefficient = coefficient
        self.salary = self.salary * coefficient
        Manager.manager_team['designer'].append(self.first_name)


a = Designer('Petur', 'Portov', 1000, 4, 'Martin', 0.4)
b = Developer('Bobor', 'Maksimov', 1800, 0, 'Putin')
k = Designer('Tuer', 'ipirin', 1400, 4, 'Borov', 0.7)
n = Designer('Tur', 'pirin', 1400, 4, 'Borov', 0.7)
v = Designer('ter', 'irin', 1400, 4, 'Borov', 0.7)
r = Designer('ter', 'Pipirin', 1400, 4, 'Borov', 0.7)
d = Manager('Martun', 'Porontuv', 800, 6,)
print(a)
print(Manager.manager_team)
