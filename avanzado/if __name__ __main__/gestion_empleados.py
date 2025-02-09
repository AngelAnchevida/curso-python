def add_employee(name: str) -> list:
    print(employees)
    print("Empleado agregado")
    employees.append(name)
    return employees

def delete_employee(name: str) -> list:
    print(employees)
    print("Empleado eliminado")
    if name in employees:
        employees.remove(name)
        return employees
    else:
        print("No se encontró al empleado")


employees = ['Angel', 'Ana', 'Luis']

if __name__ == "__main__":
    print("Gestión de empleados")
    op1 = add_employee(input("Ingresa el nombre del empleado: "))
    print(op1)

    op2 = delete_employee(input("Ingrese el nombre del empleado que desea eliminar: "))
    print(op2)
    


#emp1 = input("Ingrese el nombre del empleado: ")



# add_employee(emp1)
# print(employees)

#emp2 = input("Ingrese el nombre del empleado a eliminar: ")
#delete_employee("Angel")
#delete_employee(emp2)


