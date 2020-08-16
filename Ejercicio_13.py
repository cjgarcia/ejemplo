#mostrar el monto a pagar de cada articulo
import collections
canasta_Compras = []
parar = False
while parar == False:

    item = input('Articulo: ')
    canasta_Compras.append(item)

    if canasta_Compras.count(item) > 1:
        print("ya tienes este articulo en tu canasta de compras")
        canasta_Compras = list(dict.fromkeys(canasta_Compras))
        continue
    
    if item == 'parar':
        break

    cantidad = float(input('cantidad: '))
    canasta_Compras.append(cantidad)
    precio = float(input('precio:  '))
    canasta_Compras.append(precio)
    monto_pagar = cantidad * precio
    canasta_Compras.append(monto_pagar)#total a pagar de cada articulo 

items = list(filter(lambda item: isinstance(item, str),canasta_Compras))

canasta_Compras.pop()# Eliminar la palabra parar de la lista

print('\n')
for mi_canasta in canasta_Compras:
    print(mi_canasta)

print('\ncantidad de articulos en la lista:\t',len(items)-1)
