def check_access(func):
    def wrapper(employee):
        #Comprobar si el empleado tiene rol 'admin'
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print('ACESSO DENEGADO. Solo los administradores pueden acceder.')
    return wrapper


@check_access
def delete_employee(employee):
    print(f"El empleado {employee['name']} ha sido eliminado")


admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}



delete_employee(admin)
delete_employee(employee)