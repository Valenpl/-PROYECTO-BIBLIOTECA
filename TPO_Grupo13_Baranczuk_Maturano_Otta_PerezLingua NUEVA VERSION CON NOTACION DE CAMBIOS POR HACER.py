# Primer Parcial Grupo 13 Jueves turno mañana
# Baranczuk Thiago 1191201
# Lucas Damian Maturano 1184850
# Santiago diego otta mendez 1151647
# Valentino perez lingua 1190848

import random


def generarId(usuarios):
    while True:
        usuarioId = random.randint(100, 999) 
        idUnico = True 
        for usuario in usuarios:
            if usuario['ID'] == usuarioId:
                idUnico = False 
                break  
        if idUnico:
            return usuarioId

def añadir(elemento, lista, datos, generos=None):#usamos la misma funcion para usuario, genero y libro
    if elemento == "género":
        nuevoId = max(lista.keys()) + 1 if lista else 1 #ya que los generos los identificamos de uno en uno como ya lo establecimos en el main y si no hay, arranca en 1
        lista[nuevoId] = datos
        print(f"Género '{datos}' añadido con ID {nuevoId}.")
    elif elemento == "libro":
        for libro in lista:
            if libro['SKU'] == datos[0]:
                print(f"Error: El libro con SKU '{datos[0]}' ya existe.")
                return # MALA PRAXIS USAR UN RETURN PARA SALIR DE UNA FUNCION DENTRO DE UN
        if datos[3] not in generos.values():
            print(f"Error: El género '{datos[3]}' no existe.")
            return
        libro = {'SKU': datos[0], 'Título': datos[1], 'Autor': datos[2], 'Género': datos[3], 'Disponible': True}
        lista.append(libro)
        print(f"Libro '{datos[1]}' añadido con SKU {datos[0]}.")
    elif elemento == "usuario":
        if not datos[0].isalpha() or not datos[1].isalpha():
            print("Error: El nombre y apellido deben ser una cadena de caracteres.")
            return
        usuarioId = generarId(lista)
        usuario = {'ID': usuarioId, 'Nombre': datos[0], 'Apellido': datos[1]}
        lista.append(usuario)
        print(f"Usuario '{datos[0]} {datos[1]}' registrado con ID '{usuarioId}'.")

def eliminar(elemento, lista, id):#usamos la misma funcion para usuario, genero y libro
    if elemento == "género":
        id = int(id)
        if id in lista:
            eliminado = lista.pop(id)
            print(f"Género '{eliminado}' eliminado.")
        else:
            print(f"El género con ID '{id}' no existe.")
    elif elemento == "libro":
        libroEncontrado = False
        for libro in lista[:]:  # porque copiamos la lista
            if libro['SKU'] == id:
                lista.remove(libro)
                print(f"Libro con SKU '{id}' eliminado.")
                libroEncontrado = True
                break
        if not libroEncontrado:
            print(f"El libro con SKU '{id}' no existe.")
    elif elemento == "usuario":
        id = int(id)
        usuarioEncontrado = False
        for usuario in lista[:]:
            if usuario['ID'] == id:
                lista.remove(usuario)
                print(f"Usuario con ID '{id}' eliminado.")
                usuarioEncontrado = True
                break
        if not usuarioEncontrado:
            print(f"El ID '{id}' no existe.")

def ver(elemento, lista):#usamos la misma funcion para usuario, genero y libro
    if not lista:
        print(f"No hay {elemento}s registrados.")
        return
    print(f"Lista de {elemento}s:")
    if elemento == "género":
        for idGenero, nombre in lista.items():
            print(f"- ID: {idGenero}, Nombre: {nombre}")
    elif elemento == "libro":
        for libro in lista:
            print(f"- SKU: {libro['SKU']}, Título: {libro['Título']}, Autor: {libro['Autor']}, Género: {libro['Género']}, Disponible: {libro['Disponible']}")
    elif elemento == "usuario":
        for usuario in lista:
            print(f"- ID: {usuario['ID']}, Nombre: {usuario['Nombre']}, Apellido: {usuario['Apellido']}")

def prestarLibro(usuarios, libros, prestamos):
    usuarioId = int(input("Ingresá el ID del usuario: "))
    skuLibro = input("Ingresá el SKU del libro a prestar: ")
    usuario = None
    for u in usuarios:
        if u['ID'] == usuarioId:
            usuario = u
            break
    if not usuario:
        print(f"Usuario con ID '{usuarioId}' no existe.")
        return
    libro = None
    for l in libros:
        if l['SKU'] == skuLibro:
            libro = l
            break
    if not libro:
        print(f"El libro con SKU '{skuLibro}' no existe.")
        return
    if not libro['Disponible']: #buscamos que disponible este en false
        print(f"El libro con SKU '{skuLibro}' no está disponible para préstamo.")
        return
    
    prestamos.append({'IdUsuario': usuarioId, 'SKULibro': skuLibro})
    libro['Disponible'] = False
    print(f"Libro con SKU '{skuLibro}' prestado al usuario '{usuario['Nombre']} {usuario['Apellido']}'.")

def devolverLibro(usuarios, libros, prestamos):
    usuarioId = int(input("Ingresá el ID del usuario: "))
    skuLibro = input("Ingresá el SKU del libro a devolver: ")
    usuario = None
    for u in usuarios: #verificamos que exista un usuario con ese id
        if u['ID'] == usuarioId:
            usuario = u
            break
    if not usuario:
        print(f"Usuario con ID '{usuarioId}' no existe.")
        return
    
    prestamo = None
    for p in prestamos: #buscamos que exista el prestamo
        if p['IdUsuario'] == usuarioId and p['SKULibro'] == skuLibro:
            prestamo = p
            break
    if not prestamo:
        print(f"No se encontró registro de que el usuario '{usuarioId}' sacó un prestamo del libro '{skuLibro}'.")
        return
    
    libro = None
    for l in libros: #cambiamos el estado del libro despues que lo devuelven
        if l['SKU'] == skuLibro:
            libro = l
            break
    if libro:
        libro['Disponible'] = True

    prestamos.remove(prestamo)
    print(f"Libro con SKU '{skuLibro}' devuelto por el usuario '{usuario['Nombre']} {usuario['Apellido']}'.")

def main():
    usuarios = []
    libros = [
        {'SKU': '1', 'Título': 'Duna', 'Autor': 'Frank Herbert', 'Género': 'Ciencia Ficción', 'Disponible': True},
        {'SKU': '2', 'Título': 'Neuromante', 'Autor': 'William Gibson', 'Género': 'Ciencia Ficción', 'Disponible': True},
        {'SKU': '3', 'Título': 'La comunidad del anillo', 'Autor': 'J.R.R. Tolkien', 'Género': 'Fantasía', 'Disponible': True},
        {'SKU': '4', 'Título': 'El nombre del viento', 'Autor': 'Patrick Rothfuss', 'Género': 'Fantasía', 'Disponible': True},
        {'SKU': '5', 'Título': 'La chica del tren', 'Autor': 'Paula Hawkins', 'Género': 'Misterio', 'Disponible': True},
        {'SKU': '6', 'Título': 'El asesinato de Roger Ackroyd', 'Autor': 'Agatha Christie', 'Género': 'Misterio', 'Disponible': True}
    ]
    generos = {1: 'Ciencia Ficción', 2: 'Fantasía', 3: 'Misterio'}
    prestamos = []
# MEJORAR MENU Y EL INTERFACE
#AGREGAR UNA TECLA PARA VOLVER AL MENU
#FILTRAR POR GENERO/AUTOR/PARTE DEL TITULO
#MANEJAR UN STOCK
##HACER RESERVAS DE UN LIBRO
###PERIODO DE PRESTAMO/SANCION O PENALIDAD
#### TITULOS VENCIDOS Y NO DEVUELTOS
#USAR MODULO DATE TIME
#
    while True:
        print("\nOpciones:")
        print("1. Añadir género")
        print("2. Eliminar género")
        print("3. Añadir libro")
        print("4. Eliminar libro")
        print("5. Añadir usuario")
        print("6. Eliminar usuario")
        print("7. Ver géneros")
        print("8. Ver libros")
        print("9. Ver usuarios")
        print("10. Prestar libro")
        print("11. Devolver libro")
        print("12. Salir")
        
        opcion = input("Seleccioná una opción: ")

        if opcion == '1':
            genero = input("Ingresá el nombre del género a añadir: ")
            añadir("género", generos, genero)
        elif opcion == '2':
            idGenero = input("Ingresá el ID del género a eliminar: ")
            eliminar("género", generos, idGenero)
        elif opcion == '3':
            sku = input("Ingresá el SKU del libro: ")
            titulo = input("Ingresá el título del libro: ")
            autor = input("Ingresá el autor del libro: ")
            genero = input("Ingresá el género del libro: ")
            añadir("libro", libros, (sku, titulo, autor, genero),generos)
        elif opcion == '4':
            sku = input("Ingresá el SKU del libro a eliminar: ")
            eliminar("libro", libros, sku)
        elif opcion == '5':
            nombre = input("Ingresá su nombre: ")
            apellido = input("Ingresá su apellido: ")
            añadir("usuario", usuarios, (nombre, apellido))
        elif opcion == '6':
            idUsuario = input("Ingresá el ID del usuario a eliminar: ")
            eliminar("usuario", usuarios, idUsuario)
        elif opcion == '7':
            ver("género", generos)
        elif opcion == '8':
            ver("libro", libros)
        elif opcion == '9':
            ver("usuario", usuarios)
        elif opcion == '10':
            prestarLibro(usuarios, libros, prestamos)
        elif opcion == '11':
            devolverLibro(usuarios, libros, prestamos)
        elif opcion == '12':
            print("Saliste del programa!")
            break
        else:
            print("Opción no válida, intentá de nuevo.")

if __name__ == "__main__":
    main()
