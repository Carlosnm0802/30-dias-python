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
        
if __name__ == "__main__":
    tablero = Tablero()
    tablero.inicializar_piezas()
    tablero.mostrar()