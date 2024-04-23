```
#Iterar a través de una lista de diccionarios
#Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionario de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'}, #posicion 0
         {'first_name' : 'John', 'last_name' : 'Rosales'}, #posicion 1
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},#posicion 2
         {'first_name' : 'KB', 'last_name' : 'Tonel'},#posicion 3
         {'ultimo_nombre':'Gonzalez'} #posicion 4
    ]

#para acceder a los elemento de ls LISTA 
estudiantes[3]['first_name'] = 'Randy'
#print(estudiantes[3] ) #lista que parte en indice=0 
"""
for alumno in estudiantes:
    print(alumno)

for alumno in estudiantes:
    for item in alumno:
        print(item)
        print(alumno[item])
"""

def recorrer_lista(p_lista):
    for elemento in p_lista:
        print(elemento)

def recorrer_lista_dict(p_lista_2):
    for elemento in p_lista_2:
        for item in elemento:
            print(item)
            print(elemento[item])


recorrer_lista(estudiantes)
print("segundo metodo")
recorrer_lista_dict(estudiantes)

```




