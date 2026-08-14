lista_compra = ["pan", "leche", "huevos", "fruta"]
for producto in lista_compra:
    print(f"Comprar: {producto}")

numeros = [3, 7, 12, 20]

for numero in numeros:
    print(f"El doble de {numero} es {numero*2}")

precios = [12, 5, 23, 8]
total_acumulado = 0
for precio in precios:
    total_acumulado += precio
print(f'El total gastado es {total_acumulado}')