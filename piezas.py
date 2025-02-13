tablero = [["_"for i in range(8)] for i in range(8)]

def imprimir_tablero():
    for i in range(8):
        print(" ".join(tablero[i]))

def inicializar_tablero():
    piezas = [
        Torre([0, 0], "T"), Torre([0, 7], "T"),
        Torre([7, 0], "t"), Torre([7, 7], "t"),
        Reina([0, 3], "Q"), Reina([7, 3], "q"),
        Rey([0, 4], "K"), Rey([7, 4], "k"),
        Alfil([0, 2], "A"), Alfil([0, 5], "A"),
        Alfil([7, 2], "a"), Alfil([7, 5], "a"),
        Caballo([0, 1], "C"), Caballo([0, 6], "C"),
        Caballo([7, 1], "c"), Caballo([7, 6], "c"),
        Peon([1, 0], "P"), Peon([1, 1], "P"), Peon([1, 2], "P"), Peon([1, 3], "P"),
        Peon([1, 4], "P"), Peon([1, 5], "P"), Peon([1, 6], "P"), Peon([1, 7], "P"),
        Peon([6, 0], "p"), Peon([6, 1], "p"), Peon([6, 2], "p"), Peon([6, 3], "p"),
        Peon([6, 4], "p"), Peon([6, 5], "p"), Peon([6, 6], "p"), Peon([6, 7], "p")
    ]

    for pieza in piezas:
        pieza.añadir_pieza()
    
    imprimir_tablero()

class Pieza:
    def __init__(self, posicion): #posicion es un array con coordenadas x y
        self.posicion = posicion

    def assign_pos(self, pos):
        tablero[pos[0]][pos[1]] = self.icono
        return tablero

    def añadir_pieza(self):
        self.assign_pos(self.posicion)

    def camino_libre(self, nueva_pos):
            x_actual, y_actual = self.posicion
            x_destino, y_destino = nueva_pos

            paso_x = 0 if x_actual == x_destino else (1 if x_destino > x_actual else -1)
            paso_y = 0 if y_actual == y_destino else (1 if y_destino > y_actual else -1)

            x, y = x_actual + paso_x, y_actual + paso_y
            while (x, y) != (x_destino, y_destino):
                if tablero[x][y] != "_":  # Si hay una pieza en el camino
                    return False
                x += paso_x
                y += paso_y
            return True

    def mover_pieza(self, nueva_posicion):
        
        if nueva_posicion in self.calcular_movimientos() and self.camino_libre(nueva_posicion) == True:
            posicion_destino = tablero[nueva_posicion[0]][nueva_posicion[1]]
            if posicion_destino == "_":
                tablero[nueva_posicion[0]][nueva_posicion[1]] = self.icono
                tablero[self.posicion[0]][self.posicion[1]] = "_"
                self.posicion = nueva_posicion
        
    def comer_pieza(self, nueva_posicion):
        if nueva_posicion in self.calcular_movimientos() and self.camino_libre(nueva_posicion):
            pieza_destino = tablero[nueva_posicion[0]][nueva_posicion[1]]
            if pieza_destino != "_" and pieza_destino.islower() != self.icono.islower():
                tablero[nueva_posicion[0]][nueva_posicion[1]] = self.icono
                tablero[self.posicion[0]][self.posicion[1]] = "_"
                self.posicion = nueva_posicion

class Peon(Pieza):
    def __init__(self, posicion, icono = "p"):
        super().__init__(posicion)
        self.icono = icono
    
    def calcular_movimientos(self):
        if self.icono.islower():
            movimientos_posibles = [([self.posicion[0]-1, self.posicion[1]])]
        else:
            movimientos_posibles = [([self.posicion[0]+1, self.posicion[1]])]
        return movimientos_posibles

class Reina(Pieza):
    def __init__(self, posicion, icono="Q"):
        super().__init__(posicion)
        self.icono = icono

    def calcular_movimientos(self):
        movimientos_posibles = []
        x, y = self.posicion

        # Movimientos horizontales y verticales
        for i in range(8):
            if i != x:
                movimientos_posibles.append([i, y])
            if i != y:
                movimientos_posibles.append([x, i])

        # Movimientos diagonales
        for i in range(1, 8):
            if x + i < 8 and y + i < 8:
                movimientos_posibles.append([x + i, y + i])
            if x - i >= 0 and y - i >= 0:
                movimientos_posibles.append([x - i, y - i])
            if x + i < 8 and y - i >= 0:
                movimientos_posibles.append([x + i, y - i])
            if x - i >= 0 and y + i < 8:
                movimientos_posibles.append([x - i, y + i])

        return movimientos_posibles

class Torre(Pieza):
    def __init__(self, posicion, icono="T"):
        super().__init__(posicion)
        self.icono = icono

    def calcular_movimientos(self):
        movimientos_posibles = []
        x, y = self.posicion

        # Movimientos horizontales y verticales
        for i in range(8):
            if i != x:
                movimientos_posibles.append([i, y])
            if i != y:
                movimientos_posibles.append([x, i])

        return movimientos_posibles

class Alfil(Pieza):
    def __init__(self, posicion, icono="A"):
        super().__init__(posicion)
        self.icono = icono

    def calcular_movimientos(self):
        movimientos_posibles = []
        x, y = self.posicion

        # Movimientos diagonales
        for i in range(1, 8):
            if x + i < 8 and y + i < 8:
                movimientos_posibles.append([x + i, y + i])
            if x - i >= 0 and y - i >= 0:
                movimientos_posibles.append([x - i, y - i])
            if x + i < 8 and y - i >= 0:
                movimientos_posibles.append([x + i, y - i])
            if x - i >= 0 and y + i < 8:
                movimientos_posibles.append([x - i, y + i])

        return movimientos_posibles

class Rey(Pieza):
    def __init__(self, posicion, icono="K"):
        super().__init__(posicion)
        self.icono = icono
    
    def calcular_movimientos(self):
        movimientos_posibles = [
            [self.posicion[0] + 1, self.posicion[1]],
            [self.posicion[0] - 1, self.posicion[1]],
            [self.posicion[0], self.posicion[1] + 1],
            [self.posicion[0], self.posicion[1] - 1],
            [self.posicion[0] + 1, self.posicion[1] + 1],
            [self.posicion[0] + 1, self.posicion[1] - 1],
            [self.posicion[0] - 1, self.posicion[1] + 1],
            [self.posicion[0] - 1, self.posicion[1] - 1]
        ]
        return movimientos_posibles

class Caballo(Pieza):
    def __init__(self, posicion, icono= "C"):
        super().__init__(posicion)
        self.icono = icono
    
    def calcular_movimientos(self):
        movimientos_posibles = [
            [self.posicion[0] + 2, self.posicion[1] + 1],
            [self.posicion[0] + 2, self.posicion[1] - 1],
            [self.posicion[0] - 2, self.posicion[1] + 1],
            [self.posicion[0] - 2, self.posicion[1] - 1],
            [self.posicion[0] + 1, self.posicion[1] + 2],
            [self.posicion[0] + 1, self.posicion[1] - 2],
            [self.posicion[0] - 1, self.posicion[1] + 2],
            [self.posicion[0] - 1, self.posicion[1] - 2]
        ]
        return movimientos_posibles



