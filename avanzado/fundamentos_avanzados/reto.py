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
def getSalaries(employees: list, limit: int) -> str:
    #Creamos una lista para guardar los nombre de los empleados
    person_salaries = []

    #Usamos un blucle para comparar el sueldo de cada empleado con el limite
    for person in employees:
        if person['salary'] > limit:
            #Agregamos a una lista los empleados correspondientes
            person_salaries.append(person['name'])
    print(f"Las personas con un salario mayor a {limit} son {person_salaries}")

getSalaries(employees, 1200)