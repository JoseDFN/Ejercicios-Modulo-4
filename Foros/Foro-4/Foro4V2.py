import os

def mostrar_o_crear_linea_tabla(n, m):

    if not (1 <= n <= 10 and 1 <= m <= 10):
        return "Error: n y m deben estar entre 1 y 10."
    
    carpeta = "Foros/Foro-4"
    os.makedirs(carpeta, exist_ok=True)
    nombre_fichero = os.path.join(carpeta, f'suma-{n}.txt')


    try:
        with open(nombre_fichero, 'r') as f:
            lineas = f.readlines()
        return lineas[m - 1].strip()
    except FileNotFoundError:
        print(f"El archivo {nombre_fichero} no existe. ¿Deseas crearlo? (sí/no)")
        opcion = input("Respuesta: ").strip().lower()

        match opcion:
            case "si":
                crear_tabla_suma(n, nombre_fichero)
                return f"Archivo {nombre_fichero} creado. Vuelve a intentarlo."
            case "no":
                return "Operación cancelada."
            case _:
                return "Opción no válida. Operación cancelada."
    except IndexError:
        return f"Error: No hay suficientes líneas en el archivo {nombre_fichero}."


def crear_tabla_suma(n, nombre_fichero):
    """
    Crea el archivo de tabla de suma para el número n.
    """
    with open(nombre_fichero, 'w') as f:
        for i in range(1, 11):
            f.write(f"{n} + {i} = {n + i}\n")
    print(f"Archivo {nombre_fichero} creado exitosamente con la tabla de suma de {n}.")


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Interacción con el usuario
    try:
        n = int(input("Introduce un número entero entre 1 y 10: "))
        m = int(input("Introduce otro número entero entre 1 y 10: "))
        print(mostrar_o_crear_linea_tabla(n, m))
    except ValueError:
        print("Error: Debes introducir números enteros.")
