variable1 = 10

variable1= variable1*2


#lista se define con []
lista2=[]

variable3 = None


print(variable1)  

#  comentarios de una linea

''' comentario de varias lineas 

'''
lista=['uno',2,'three']

if variable1 > 20 : # entonces
    print(variable3)
elif variable1 < 20:
    print(lista)
else:   #  variable1 = 20   
    print(lista2) 

#diccionarios se definen con {}

diccionario = { 
    "llave": "valor",
    "llave2": variable1,
    "llave3": lista,
    }

print(diccionario["llave3"][2])

print(diccionario["llave2"])

# los conjuntos se definen con () 

conjunto=( 4,3,8,2 ) 
print ("recorriendo el diccionario")
for llaves in diccionario: # CAST 
    print(llaves+':'+ str(diccionario[llaves]) ) 

print ("recorriendo la lista")
for elem in lista:
    print(elem)

print ("recorriendo el conjunto")
for elemento in conjunto:
    print(elemento) 

for i in range(4,10) :
    print(i) 
