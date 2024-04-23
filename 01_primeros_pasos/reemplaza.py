
def reemplazaNegativos(arr):
    for elemento in arr: 
        print(f"elemento:{elemento}")
        if elemento < 0:
            #buscar el elemnto en el arreglo y modificarlo
            indice=arr.index(elemento)
            print(f"indice:{indice}")
            arr[indice]=0 
            # elemento = 0 
    return arr



arr = [1, 5, 10, -2, 4,-2,-7] 

1000 -> arr
1001 -> 1
1002 -> 5
1003 -> 10
1004 -> -2

elemento -> 5010  =-2
elemento ->5010=0




resultado = reemplazaNegativos(arr) 
print(resultado) 


# [1, 5, 10, 0, 4, 0, 0]



# MI SOLUCION
def reemplazarNegativos(num_list): 
    i = 0
    for x in num_list:
        print(f"El valor de x es: {x}")
        if x < 0:
            num_list[i] = 0
        i+=1
    return num_list

a = [-2,4,-10,16,-0.1]
b = reemplazarNegativos(a)
print(b)
# salida:
# [2,4,10,16]