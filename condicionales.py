#Ejercicio 1

edades = [15, 22, 17, 30, 18]

#Recorre la lista e imprime para cada una si es mayor o menor de edad, con este formato:
#15: menor de edad
#22: mayor de edad

for edad in edades:
    if edad >= 18:
        print(f"{edad}: mayor de edad")
    else:
        print(f"{edad}: menor de edad")

#Ejercicio 2
#Cuenta cuántos precios superan los 10 euros e imprime un único mensaje al final:
#Hay 3 productos caros

precios = [12, 5, 23, 8, 45, 3]
productos_caros = 0
for precio in precios:
    if precio > 10:
       productos_caros += 1
print(f'Hay {productos_caros} productos caros')

#Minireto

precios = [12, 5, 23, 8, 45, 30]

for precio in precios:
    if precio < 10:
        print(f"{precio}: barato")
    elif precio > 25:
        print(f"{precio}: caro")
    else:
        print(f"{precio}: normal")

