#CRUD DE TABLAS DE MULTIPLICAR CON CICLO FOR

#REGISTROS
registros = []

#INGRESO DE DATOS
def crear():
    limite_tablas = int(input("Ingrese el límite de tablas: "))
    limite_numeros = int(input("Ingrese el límite de números: "))

    # Guardar datos
    datos = {
        "tablas": limite_tablas,
        "numeros": limite_numeros
    }

    registros.append(datos)

    print("\nTABLAS DE MULTIPLICAR\n")

    #IMPLEMENTACION CICLO FOR
    for tabla in range(1, limite_tablas + 1):

        print(f"--- TABLA DEL {tabla} ---")

        for numero in range(1, limite_numeros + 1):

            resultado = tabla * numero
            print(f"{tabla} x {numero} = {resultado}")

        print()


def leer():
    if len(registros) == 0:
        print("No hay registros guardados.")
    else:
        print("\nREGISTROS GUARDADOS")

        for i, dato in enumerate(registros):

            print(f"{i+1}. "
                  f"Tablas: {dato['tablas']} | "
                  f"Números: {dato['numeros']}")



def actualizar():
    leer()

    if len(registros) > 0:

        opcion = int(input("Seleccione el registro a actualizar: ")) - 1

        if 0 <= opcion < len(registros):

            nuevos_tablas = int(input("Nuevo límite de tablas: "))
            nuevos_numeros = int(input("Nuevo límite de números: "))

            registros[opcion]["tablas"] = nuevos_tablas
            registros[opcion]["numeros"] = nuevos_numeros

            print("Registro actualizado correctamente.")

        else:
            print("Opción inválida.")


def eliminar():
    leer()

    if len(registros) > 0:

        opcion = int(input("Seleccione el registro a eliminar: ")) - 1

        if 0 <= opcion < len(registros):

            registros.pop(opcion)

            print("Registro eliminado correctamente.")

        else:
            print("Opción inválida.")


# MENÚ PRINCIPAL
while True:

    print("\n===== CRUD TABLAS DE MULTIPLICAR =====")
    print("1. Crear tablas")
    print("2. Leer registros")
    print("3. Actualizar registros")
    print("4. Eliminar registros")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear()

    elif opcion == "2":
        leer()

    elif opcion == "3":
        actualizar()

    elif opcion == "4":
        eliminar()

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")
