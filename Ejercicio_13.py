#mostrar el monto a pagar de cada articulo "lo puse todo tan pegado par que me quepa en la captura"
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

dictlist = [dict() for x in range(0,len(canasta_Compras))]
print(dictlist)

"""print('\n')
for mi_canasta in canasta_Compras:
    print(mi_canasta)

#print("El articulo más caro cuesta:\t", max(max_min))
#print("El articulo más varato cuesta:\t",min(max_min))

print('\ncantidad de articulos en la lista:\t',len(items)-1)"""