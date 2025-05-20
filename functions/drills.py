def show_team_members(team_members):
    for team_member in team_members:
        print("\n" + team_member.title())

team_members = ['john', 'alice', 'bob', 'eve']

show_team_members(team_members)

def promote_team_members(team_members):
    promoted_team_members = []

    while team_members:
        team_member = team_members.pop()
        promoted_team_member = team_member + " (Promoted)"
        promoted_team_members.append(promoted_team_member)

    return promoted_team_members

    for promoted_team_member in promoted_team_members:
        team_members.append(promoted_team_member)


show_team_members(team_members)
promoted_team_members = promote_team_members(team_members[:])
show_team_members(promoted_team_members)

########

def show_animals(animals):
    for animal in animals:
        print(animal.title())

animals = ['zebra', 'hippo', 'cat', 'crocodile', 'polar bear']
show_animals(animals)

def add_new_animal(animals):
    new_animals = []

    while animals:
        animal = animals.pop()
        new_animal = new_animals.append(animal)

    return new_animals
    for new_animal in new_animals:
        animals.append(new_animal)

show_animals(animals)
new_animals = add_new_animal(animals[:])
add_new_animal(new_animals)

#####

def show_students(students):
    for student, grade in students.items():
        print(student.title() + ": " + str(grade))

students = {'anna': 69, 'bella': 37, 'cleo': 88, 'daisy': 52, 'emma': 40 }

show_students(students)

def assign_grades(students):
    students_grades = {}

    for student, grade in students.items():
        if grade < 40:
            classification = "Fail"
        elif grade < 50:
            classification = 3
        elif grade < 60:
            classification = "2:2"
        elif grade < 70:
            classification = "2:1"
        elif grade >= 70:
            classification = 1

        students_grades[student] = classification
    
    return students_grades

print(assign_grades(students))


######

def show_salaries(employees):
    for employee, salary in employees.items():
        print(employee.title() + ": £" + str(salary))

employees = {'alice': 4000, 'bob': 3500, 'charlie': 4200, 'diana': 3800}

show_salaries(employees)   

def add_bonus(employees):
    bonus_salaries = {}
    for employee, salary in employees.items():
        salary_after_bonus = salary * 1.10

        bonus_salaries[employee] = salary_after_bonus

    return bonus_salaries

salaries_with_bonus = add_bonus(employees)
print(salaries_with_bonus)

