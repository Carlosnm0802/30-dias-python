#Reto de hoy: Tablero de ajedrez
class Tablero:
    def __init__(self):
        self.tablero = [[" " for _ in range(8)] for _ in range(8)]
        self.filas = 8
        self.columnas = 8
    
    def mostrar(self):
        # Crear la fila de letras A-H
        columnas = "ABCDEFGH"
        print("  " + " ".join(columnas))
        #Creamos las filas del tablero
        for indice, fila in enumerate(self.tablero):
            numero_fila = 8 - indice  # 8, 7, 6, 5... (ajedrez usa 8 en arriba)
            print(f"{numero_fila} " + " ".join(fila))
    
if __name__ == "__main__":
    tablero = Tablero()
    tablero.mostrar()