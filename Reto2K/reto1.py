laberinto = [
    [' ', 'X', 'X', 'X', 'X'],
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X', ' '],
    ['X', 'X', 'X', 'X', 'S'],
]

def imprimir_laberinto(l):
    for fila in l:
        print(''.join(fila))

# Ejemplo de uso:
imprimir_laberinto(laberinto)

movimientos = ['Abajo', 'Abajo', 'Abajo', 'Derecha', 'Derecha', 'Arriba', 'Arriba', 'Derecha', 'Derecha', 'Abajo', 'Abajo', 'Abajo']