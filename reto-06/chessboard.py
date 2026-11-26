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
        #Creamos las filas del tablero
        for indice, fila in enumerate(self.tablero):
            numero_fila = 8 - indice  # 8, 7, 6, 5... (ajedrez usa 8 en arriba)
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
        columna = ord(coordenada[0].upper()) - ord('A')  # e → 4
        fila = 8 - int(coordenada[1])                     # 2 → 6
        return fila, columna

    def mover_pieza(self, origen, destino):
        """Mueve una pieza de origen a destino"""
        fila_o, col_o = self.convertir_coordenadas(origen)
        fila_d, col_d = self.convertir_coordenadas(destino)
        
        # Verificar que haya una pieza en origen
        if self.tablero[fila_o][col_o] == ".":
            print(f"Error: No hay pieza en {origen}")
            return
        
        # Mover la pieza
        pieza = self.tablero[fila_o][col_o]
        self.tablero[fila_d][col_d] = pieza
        self.tablero[fila_o][col_o] = "."
        
if __name__ == "__main__":
    tablero = Tablero()
    tablero.mostrar()
    
    print("\nMovimiento 1: e2 → e4 (Peón blanco)")
    tablero.mover_pieza("e2", "e4")
    tablero.mostrar()
    
    print("Movimiento 2: e7 → e5 (Peón negro)")
    tablero.mover_pieza("e7", "e5")
    tablero.mostrar()