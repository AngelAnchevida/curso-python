import json

def check_access(func):
    #El Wrapper recibe los mismos elementos que la función que contiene
    def wrapper(): #2
        print("Bienvenido")
        action_admin = input(f"Administrador {admin['name']} ingrese la acción que desea realizar: ")
        action_employee = input(f"Empleado {employee['name']} ingrese la acción que desea realizar: ")
        for emp in employees:
            if emp.get('role') == 'admin':
                func(emp, action_admin)
            else:
                func(emp, action_employee)

        #Formas de convertir una lista a string
        actions_text = '\n'.join(map(str, actions_list))
        #actions_text = json.dumps(actions_list)
                
        with open('avanzado/decorators/actions-list.txt', 'w') as file:
            file.write(actions_text)

        print("Se ha registrado la accion del usuario")
        print(actions_list)
    return wrapper

@check_access #2
def add_action_employee(employe, actions):
    #3
    #Creamos la forma de empleado
    emp_action = {
                    'name' : employe.get('name'),
                    'actions' : actions
                 }

    actions_list.append(emp_action)

actions_list = []

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

employees = [
                {'name': 'Carlos', 'role': 'admin'},
                {'name': 'Ana', 'role': 'employee'}
            ]

#NOTA IMPORTANTE
#Se puede llamar una función a ejecutarse sin recibir ningun elemento si después
# le pasas los valores requeridos a la funcion dentro del wrapper no al wrapper mismo
#El wrapper debe recibir exactamente los mismo valores que
#uses al llamar una funcion y si no mandas nada, el wrapper tampoco
#recibe nada
add_action_employee() #1

