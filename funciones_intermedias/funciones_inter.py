dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#print(len(dojo['ubicaciones']))

def printInfo(some_dict): #firma del metodo
    for llave_dict in some_dict:
        lista=some_dict[llave_dict]
        tamaño=len(lista)

        #print(f"{tamaño} {item}")
        #imprimimos la cabecera
        print(f"{len(some_dict[llave_dict])} {llave_dict}")

        #imprimimos las ciudades
        for item_lista in some_dict[llave_dict]:
            print(item_lista)

        print(" ")


        #print(item)
        

printInfo(dojo) 