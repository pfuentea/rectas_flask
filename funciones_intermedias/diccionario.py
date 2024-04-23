lista_de_diccionarios = [
    {'nombre': 'Juan', 'edad': 25, 'ciudad': 'México'},
    {'nombre': 'María', 'edad': 30, 'ciudad': 'Bogotá'},
    {'nombre': 'Carlos', 'edad': 22, 'ciudad': 'Lima'}
]

for diccionario in lista_de_diccionarios:
    for clave, valor in diccionario.items():
        print(f"{clave} - {valor}") 