#Reto de hoy: Tablero de ajedrez
class Tablero:
    def __init__(self):
        self.tablero = [["." for _ in range(8)] for _ in range(8)] 
        self.filas = 8
        self.columnas = 8
        self.inicializar_piezas()  
    
    def mostrar(self):
        # Crear la fila de letras A-H
        columnas = "ABCDEFGH"
        print("  " + " ".join(columnas))
        # Creamos las filas del tablero
        for indice, fila in enumerate(self.tablero):
            numero_fila = 8 - indice
            print(f"{numero_fila} " + " ".join(fila))
    
    def inicializar_piezas(self):
        for columna in range(self.columnas):
            self.tablero[1][columna] = "p"  
        for columna in range(self.columnas):
            self.tablero[6][columna] = "P" 
        
        piezas_blancas = ["T", "C", "A", "Q", "K", "A", "C", "T"]
        piezas_negras = ["t", "c", "a", "q", "k", "a", "c", "t"]
        self.tablero[0] = piezas_negras
        self.tablero[7] = piezas_blancas

    def convertir_coordenadas(self, coordenada):
        """Convierte 'e2' en índices [fila, columna]"""
        columna = ord(coordenada[0].upper()) - ord('A')
        fila = 8 - int(coordenada[1])
        return fila, columna

    def validar_movimiento(self, origen, destino):
        """Valida si el movimiento es legal según las reglas del ajedrez"""
        fila_o, col_o = self.convertir_coordenadas(origen)
        fila_d, col_d = self.convertir_coordenadas(destino)
        
        pieza = self.tablero[fila_o][col_o]
        
        # Validar según el tipo de pieza
        if pieza.upper() == 'P':
            return self.validar_peon(fila_o, col_o, fila_d, col_d, pieza)
        
        # Por ahora, otras piezas se pueden mover libremente
        return True

    def validar_peon(self, fila_o, col_o, fila_d, col_d, pieza):
        """Valida movimiento de peón"""
        if pieza == 'P':  # Peón blanco
            if col_o != col_d:
                print("Error: Peón no puede moverse diagonalmente")
                return False
            
            if fila_o == 6:  # Fila inicial
                if fila_d not in [4, 5]:
                    print("Error: Peón puede moverse 1 o 2 casillas")
                    return False
            else:  # Movimientos posteriores
                if fila_d != fila_o - 1:
                    print("Error: Peón solo puede moverse 1 casilla")
                    return False
        else:  # Peón negro (p)
            if col_o != col_d:
                print("Error: Peón no puede moverse diagonalmente")
                return False
            
            if fila_o == 1:  # Fila inicial
                if fila_d not in [2, 3]:
                    print("Error: Peón puede moverse 1 o 2 casillas")
                    return False
            else:
                if fila_d != fila_o + 1:
                    print("Error: Peón solo puede moverse 1 casilla")
                    return False
        
        return True

    def mover_pieza(self, origen, destino):
        """Mueve una pieza de origen a destino"""
        fila_o, col_o = self.convertir_coordenadas(origen)
        fila_d, col_d = self.convertir_coordenadas(destino)
        
        # Verificar que haya una pieza en origen
        if self.tablero[fila_o][col_o] == ".":
            print(f"Error: No hay pieza en {origen}")
            return False
        
        # Validar el movimiento
        if not self.validar_movimiento(origen, destino):
            return False
        
        # Mover la pieza
        pieza = self.tablero[fila_o][col_o]
        self.tablero[fila_d][col_d] = pieza
        self.tablero[fila_o][col_o] = "."
        return True

if __name__ == "__main__":
    tablero = Tablero()
    tablero.mostrar()
    
    print("\n✅ Movimiento válido: e2 → e4")
    tablero.mover_pieza("e2", "e4")
    tablero.mostrar()
    
    print("\n❌ Intento inválido: e4 → e1 (3 casillas)")
    tablero.mover_pieza("e4", "e1")
    
    print("\n❌ Intento inválido: d2 → e3 (diagonal)")
    tablero.mover_pieza("d2", "e3")