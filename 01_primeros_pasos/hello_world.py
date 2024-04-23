# 1. TAREA: imprime "Hola, mundo"
print( "Hola, mundo" )
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Noelle"
print("Hola, ",name)	# con una coma
print("Hola, "+name )	# con un +
# 3. imprimir "Hola 42!" con el número en una variable

name = 42
print( "Hola", name ,"!" )  

lista=("Hola ", str(name) ,"!")  

resultado=list(lista) 

print( "".join( list(lista) ))	# con una coma

print( "Hola   "+ str(name) +"!" ) 	# con una +	-- este debería arrojar un error!


"""
# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( tu código aquí ) # con .format()
print( tu código aquí ) # con una cadena f

""" 

#Función que reciba un arreglo y reemplace cualquier número negativo por 0. 
#Regresa el arreglo SIN números negativos. Ej. Recibes: [1,5,10,-2], Regresas [1,5,10,0]
'''
arr = [1, 5, 10, -2]
range-> 0 - 3
i = 0
i = 1
i = 2
i = 3
arr[3] = 0
arr = [1, 5, 10, 0]
'''

arr = [1, 5, 10, -2]
def reemplazaNegativos(arreglo):
    for indice in range(len(arreglo)): # range(4)= (0,1,2,3)
        if arreglo[indice] < 0:
            arreglo[indice] = 0 
    return arreglo

"""
for i=0; i< largo(M) ; i=i+1) i++ 
    for ( j=0; j < largo(M) ;j=j+1 )

(a,b,c,d)

(x,y,z,w)
"""
