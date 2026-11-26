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
        elif pieza.upper() == 'T':
            return self.validar_torre(fila_o, col_o, fila_d, col_d, pieza)
        elif pieza.upper() == 'C':
            return self.validar_caballo(fila_o, col_o, fila_d, col_d, pieza)
        elif pieza.upper() == 'A':
            return self.validar_alfil(fila_o, col_o, fila_d, col_d, pieza)
        elif pieza.upper() == 'Q':
            return self.validar_reina(fila_o, col_o, fila_d, col_d, pieza)
        elif pieza.upper() == 'K':
            return self.validar_rey(fila_o, col_o, fila_d, col_d, pieza)
        
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

    def validar_torre(self, fila_o, col_o, fila_d, col_d, pieza):
        """Valida movimiento de torre (línea recta)"""
        # Torre se mueve en línea recta: misma fila O misma columna
        if fila_o == fila_d or col_o == col_d:
            return True
        else:
            print("Error: Torre debe moverse en línea recta (horizontal o vertical)")
            return False

    def validar_caballo(self, fila_o, col_o, fila_d, col_d, pieza):
        """Valida movimiento de caballo (forma de L)"""
        # Caballo se mueve en L: 2 casillas en un sentido, 1 en perpendicular
        distancia_filas = abs(fila_d - fila_o)
        distancia_columnas = abs(col_d - col_o)
        
        if (distancia_filas == 2 and distancia_columnas == 1) or \
           (distancia_filas == 1 and distancia_columnas == 2):
            return True
        else:
            print("Error: Caballo debe moverse en forma de L (2+1 o 1+2)")
            return False

    def validar_alfil(self, fila_o, col_o, fila_d, col_d, pieza):
        """Valida movimiento de alfil (diagonal)"""
        # Alfil se mueve en diagonal: diferencia de filas = diferencia de columnas
        distancia_filas = abs(fila_d - fila_o)
        distancia_columnas = abs(col_d - col_o)
        
        if distancia_filas == distancia_columnas and distancia_filas > 0:
            return True
        else:
            print("Error: Alfil debe moverse en diagonal")
            return False

    def validar_reina(self, fila_o, col_o, fila_d, col_d, pieza):
        """Valida movimiento de reina (torre + alfil)"""
        distancia_filas = abs(fila_d - fila_o)
        distancia_columnas = abs(col_d - col_o)
        
        # Movimiento de torre (línea recta)
        if fila_o == fila_d or col_o == col_d:
            return True
        # Movimiento de alfil (diagonal)
        elif distancia_filas == distancia_columnas:
            return True
        else:
            print("Error: Reina debe moverse en línea recta o diagonal")
            return False

    def validar_rey(self, fila_o, col_o, fila_d, col_d, pieza):
        """Valida movimiento de rey (1 casilla en cualquier dirección)"""
        distancia_filas = abs(fila_d - fila_o)
        distancia_columnas = abs(col_d - col_o)
        
        # Rey se mueve máximo 1 casilla en cualquier dirección
        if distancia_filas <= 1 and distancia_columnas <= 1 and \
           (distancia_filas > 0 or distancia_columnas > 0):
            return True
        else:
            print("Error: Rey solo puede moverse 1 casilla en cualquier dirección")
            return False

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
    print("=" * 40)
    print("TABLERO INICIAL")
    print("=" * 40)
    tablero.mostrar()
    
    # PRUEBAS CON PEONES
    print("\n" + "=" * 40)
    print("PRUEBAS: PEONES")
    print("=" * 40)
    
    print("\n✅ Peón blanco: e2 → e4 (2 casillas válidas)")
    tablero.mover_pieza("e2", "e4")
    tablero.mostrar()
    
    print("\n❌ Peón: e4 → e1 (3 casillas - INVÁLIDO)")
    tablero.mover_pieza("e4", "e1")
    
    # PRUEBAS CON TORRES
    print("\n" + "=" * 40)
    print("PRUEBAS: TORRES")
    print("=" * 40)
    
    print("\n✅ Torre blanca: a1 → a3 (vertical)")
    tablero.mover_pieza("a1", "a3")
    tablero.mostrar()
    
    print("\n✅ Torre: a3 → d3 (horizontal)")
    tablero.mover_pieza("a3", "d3")
    tablero.mostrar()
    
    print("\n❌ Torre: d3 → e4 (diagonal - INVÁLIDO)")
    tablero.mover_pieza("d3", "e4")
    
    # PRUEBAS CON CABALLOS
    print("\n" + "=" * 40)
    print("PRUEBAS: CABALLOS")
    print("=" * 40)
    
    print("\n✅ Caballo blanco: b1 → c3 (forma de L)")
    tablero.mover_pieza("b1", "c3")
    tablero.mostrar()
    
    print("\n❌ Caballo: c3 → c5 (línea recta - INVÁLIDO)")
    tablero.mover_pieza("c3", "c5")
    
    # PRUEBAS CON ALFILES
    print("\n" + "=" * 40)
    print("PRUEBAS: ALFILES")
    print("=" * 40)
    
    print("\n✅ Alfil blanco: c1 → f4 (diagonal)")
    tablero.mover_pieza("c1", "f4")
    tablero.mostrar()
    
    print("\n❌ Alfil: f4 → f6 (vertical - INVÁLIDO)")
    tablero.mover_pieza("f4", "f6")
    
    # PRUEBAS CON REINA
    print("\n" + "=" * 40)
    print("PRUEBAS: REINA")
    print("=" * 40)
    
    print("\n✅ Reina blanca: d1 → d3 (vertical)")
    tablero.mover_pieza("d1", "d3")
    tablero.mostrar()
    
    print("\n✅ Reina: d3 → f5 (diagonal)")
    tablero.mover_pieza("d3", "f5")
    tablero.mostrar()
    
    print("\n❌ Reina: f5 → g3 (forma de L - INVÁLIDO)")
    tablero.mover_pieza("f5", "g3")
    
    # PRUEBAS CON REY
    print("\n" + "=" * 40)
    print("PRUEBAS: REY")
    print("=" * 40)
    
    print("\n✅ Rey blanco: e1 → e2 (1 casilla)")
    tablero.mover_pieza("e1", "e2")
    tablero.mostrar()
    
    print("\n❌ Rey: e2 → e4 (2 casillas - INVÁLIDO)")
    tablero.mover_pieza("e2", "e4")
    
    print("\n" + "=" * 40)
    print("FIN DE PRUEBAS - FASE 5 COMPLETADA ✅")
    print("=" * 40)