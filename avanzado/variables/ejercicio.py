employees = [{
                'name' : 'Angel',
                'age' : 24,
                'salary' : 1000
              },
              {
                'name' : 'Laura',
                'age' : 29,
                'salary' : 1400
              },
              {
                'name' : 'Juan',
                'age' : 25,
                'salary' : 900
              },
              {
                'name' : 'Jesus',
                'age' : 22,
                'salary' : 1500
              },
              {
                'name' : 'Ramon',
                'age' : 25,
                'salary' : 1450
              }]

#Metodo for
def getSalaries(employees, limit):
    #Creamos una lista para guardar los nombre de los empleados
    person_salaries = []

    #Usamos un blucle para comparar el sueldo de cada empleado con el limite
    for person in employees:
        if person['salary'] > limit:
            #Agregamos a una lista los empleados correspondientes
            person_salaries.append(person['name'])
    print(f"Las personas con un salario mayor a {limit} son {person_salaries}")

getSalaries(employees, 1200)

#Método buscar
def search_salary():
    employees_max_salary = []
    employees_max_salary = list(filter(lambda employe: employe['salary'] > 1200, employees))
    employees_names = []
    for emp in employees_max_salary:
                employees_names.append(emp['name'])
    return employees_names

print(f'Los empleados que ganan mas de 1200 son: {search_salary()}')