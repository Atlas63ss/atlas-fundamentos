precios_tienda_a = [12, 5, 23]
precios_tienda_b = [40, 8, 15]
precios_tienda_c = [3, 5, 2]

def clasificar_precios(precios):
    for precio in precios:
        if precio < 10:
            print(f'{precio}: barato')
        elif precio > 25:
            print(f'{precio}: caro')
        else:
            print(f'{precio}: normal')

def calcular_total(precios):
    total = 0
    for precio in precios:
        total += precio
    return total

total_tienda_a = calcular_total(precios_tienda_a)
total_tienda_b = calcular_total(precios_tienda_b)
total_tienda_c = calcular_total(precios_tienda_c)

clasificar_precios(precios_tienda_a)
clasificar_precios(precios_tienda_b)
clasificar_precios(precios_tienda_c)

print(f'''Tienda A: {total_tienda_a}
Tienda B: {total_tienda_b}
Tienda C: {total_tienda_c}''')

if total_tienda_a > total_tienda_b and total_tienda_a > total_tienda_c:
    print('La tienda más cara es la A')
elif total_tienda_b > total_tienda_c and total_tienda_b > total_tienda_a:
    print('La tienda más cara es la B')
elif total_tienda_c > total_tienda_a and total_tienda_c > total_tienda_b:
    print('La tienda más cara es la C')