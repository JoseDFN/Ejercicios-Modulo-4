def mostrar_linea_tabla(n, m):
    """
    Lee la tabla de multiplicar del número n desde un archivo y muestra la línea m.

    >>> mostrar_linea_tabla(3, 2)
    '3 x 2 = 6\\n'
    >>> mostrar_linea_tabla(5, 5)
    '5 x 5 = 25\\n'
    >>> mostrar_linea_tabla(10, 11)
    'Error: No existe la línea solicitada en la tabla 10\\n'
    >>> mostrar_linea_tabla(11, 1)
    'Error: El número debe estar entre 1 y 10\\n'
    """
    if not (1 <= n <= 10 and 1 <= m <= 10):
        return f'Error: El número debe estar entre 1 y 10\n'
    
    nombre_fichero = f'tabla-{n}.txt'
    
    try:
        with open(nombre_fichero, 'r') as f:
            lineas = f.readlines()
        
        if m - 1 < len(lineas):
            return lineas[m - 1]
        else:
            return f'Error: No existe la línea solicitada en la tabla {n}\n'
    
    except FileNotFoundError:
        return f'Error: No existe el fichero con la tabla del {n}\n'

# Ejecutando las pruebas
if __name__ == '__main__':
    import doctest
    doctest.testmod()
