#Escribe un programa que:
# 1. Pida precios al usuario uno a uno, en bucle.
# 2. Se detenga cuando el usuario escriba fin.
# 3. Guarde cada precio en una lista.
# 4. Al terminar, muestre cuántos productos hay, el total y el más caro.

def suma(lista):
    total = 0
    for precio in lista:
        total += precio
    return total

def maximo(lista):
    max = 0
    for precio in lista:
        if precio > max:
            max = precio
    return max

precios = []

while True:
    precio = (input("Ingrese el precio: "))
    if precio == 'fin':
        break
    if not precio.isdigit():
        print("El precio debe ser numeral.")
        continue
    precio = int(precio)
    if precio <= 0:
        print("El precio no puede ser igual o inferior a 0.")
        continue
    precios.append(precio)

if len(precios) < 1:
    print("No hay productos en la lista")
elif len(precios) == 1:
    print(f'Solo hay un producto, y cuesta {precios[0]} euros.')
else:
    print(f'La lista de precios es: {precios}, y son {len(precios)} productos. En total cuestan {suma(precios)} euros, y el producto más caro cuesta {maximo(precios)} euros.')

