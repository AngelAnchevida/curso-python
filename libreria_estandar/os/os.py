import os

'''cwd = os.getcwd() #invoca una funcion de os que te dice en que directorio estas actualmente

print("Directorio de trabajo actual", cwd)'''

#Listar los archivos .txt
#Forma 1
#Solo funciona si se especifica la ruta
txt_files = [f for f in os.listdir('./libreria_estandar/os') if f.endswith('.txt')]
print("Archivos txt son: ", txt_files)


#Forma 2
#Se situa en el directorio actual
# dir_path = os.path.dirname(os.path.realpath(__file__))

# #busca los archivos que tenga coincidencias
# filesSearch = []
# for root, dirs, files in os.walk(dir_path):
#     for file in files:
#         if file.endswith('.txt'):
#             filesSearch.append(file)
            #Imprime la ruta y los archivos que tengan coincidencias
            #print(root+'/'+str(file))
#print(filesSearch)


#Renombrar archivos, la ruta donde pones el archivo renombrado puede cambiar para moverlo de lugar
os.rename('./libreria_estandar/os/hola.txt', './libreria_estandar/os/hola_mundo.txt')
print('Archivo renombrado')

txt_files = [f for f in os.listdir('./libreria_estandar/os') if f.endswith('.txt')]
print("Archivos txt son: ", txt_files)
