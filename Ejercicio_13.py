#mostrar el monto a pagar de cada articulo
import collections, os
# No creo que necesites usuar collections en este problema
# Aveces si agregamos dependencias innecesarias nuestro benchmark se dispara en los review

# Debes tener cuidado con el uso de caps. 
# canasta_compras es un nombre de var más python friendly

# Cuando tengas que repetir cierta logica en tu codigo siempre es bueno encapsular en una func
# Esta func es para manejar las excepts de valor cuando leas 'parar' por teclado.
# Es un ejemplo, puedes modificar a tu gusto.

def obt_dato(valor):
    resp = 0.0

    try:
        resp = float(valor) 
    except ValueError:
        print('\nERROR: La cantidad y el precio deben ser numeros. Se ha asignado 0')
    
    return resp

canasta_compras = [] 
# parar = False

# Observando tu codigo veo que no necesitas utilizar ** while parar == False **
while True:


    # Aqui hay un problema de diseño, veras debes tener control del loop y saber cuando pedir que cosa
    # Si en un momento pides el precio e introduzco 'parar' pues el program explota
    # Eso lo podríamos resolver con un manejo de excepcion. Te voy hacer un ejem.
    # Sé que no lo tocamos en el curso, pero como te dije obvie ese tipo de cosas porque entenida que la mayoria ya tenia la nocion
    

    # Es siempre buena practica indicarle al usuario que esta pasando:
    print('Entre los datos de un articulo o "parar".\n')

    item = {} # Item ahora es un dict
    
    num_items = len(canasta_compras) + 1 # Saber el número de items en la canasta


    # Ahora solo voy agregando los keys del dict hasta completar 
    item['nombre'] = input(f'Articulo #{num_items}: ')

    # Aqui podriamos utilizar una tecnica para garantizar que todos los items se agrupen
    # Eso se hace agregando un item a la lista con el nombre del producto.. Para no complicartelo y modificar más de la cuenta
    # lo voy hacer siguiendo tu logica. 
    #
    # Algo que aclarar. El ejercicio no te pedia limitar a productos unicos, solo clasificarlos 
    # Asi que esta parte de comprobar si el item existe no es necesaria. 
    
    if item['nombre'] == 'parar': break

    item['cantidad'] = obt_dato(input('cantidad: '))
    item['precio'] = obt_dato(input('precio:  '))
    item['monto_pagar'] = item['cantidad'] * item['precio']

    # Ahora si agrego el item a la canasta
    canasta_compras.append(item) 

    # Solo por costumbre, limpia la pantalla
    os.system("cls | clear") # windows or linux 


# Estas sentencias no son necesarias tampoco
# items = list(filter(lambda item: isinstance(item, str),canasta_compras))

# canasta_compras.pop()# Eliminar la palabra parar de la lista

os.system("cls | clear")

# Validar que exista un item en la canasta
if canasta_compras:

    print('Articulo','Cantidad','Precio', 'Monto a Pagar', sep='|\t')

    for item in canasta_compras:
        print(item['nombre'], int(item['cantidad']), item['precio'], item['monto_pagar'], sep='|\t\t')

    print('\nTOTALES:\nCantidad de articulos en la lista:\t',len(canasta_compras))
    # Te voy hacer un ejemplo utilizando comprehension  
    print('Menor valor de precio:\t', min([item['precio'] for item in canasta_compras]))
    print('Monto total:\t', sum([item['monto_pagar'] for item in canasta_compras]))
    print('Ariticulos (unicos): \t', ', '.join(set([item['nombre'] for item in canasta_compras])))

else:
    print("\nNo agrego ningun articulo a la canasta.".upper())

# Con el ejemplo de más arriba puedes sacar si un item se repite, el valor maximo y demas.

# No quise hacer este ejemplo en las grabaciones porque la idea era que practicaran todos los fundamentos
# La verdad es dificil luego escribir mucho codigo, si sacas los comentarios veras que hay menos lineas que antes
# pero como te dije para la mayoria lo que quiero es que practiquen los fundamentos y así lleguen a comprender estos conceptos