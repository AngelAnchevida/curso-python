#Desempaquetado de args
def add(a,b,c):
    return a + b + c

values = (1,2,3)

print(add(*values))

#Permite leer un objeto mediante kwargs
def show_info(name, age):
    print(f"name: {name}, Age: {age}")

data = {'name' : 'Angel', 'age' : 28}

show_info(**data)