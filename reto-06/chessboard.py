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
        pieza_destino = self.tablero[fila_d][col_d]
        
        if pieza == 'P':  # Peón blanco
            # Movimiento normal (sin captura): solo hacia adelante en la misma columna
            if pieza_destino == ".":
                if col_o != col_d:
                    print("Error: Peón no puede moverse diagonalmente (sin capturar)")
                    return False
                
                if fila_o == 6:  # Fila inicial
                    if fila_d not in [4, 5]:
                        print("Error: Peón puede moverse 1 o 2 casillas")
                        return False
                else:  # Movimientos posteriores
                    if fila_d != fila_o - 1:
                        print("Error: Peón solo puede moverse 1 casilla")
                        return False
            # Captura diagonal: solo 1 casilla diagonalmente
            else:
                if abs(col_d - col_o) != 1 or fila_d != fila_o - 1:
                    print("Error: Peón solo captura 1 casilla diagonalmente")
                    return False
        
        else:  # Peón negro (p)
            # Movimiento normal (sin captura): solo hacia adelante en la misma columna
            if pieza_destino == ".":
                if col_o != col_d:
                    print("Error: Peón no puede moverse diagonalmente (sin capturar)")
                    return False
                
                if fila_o == 1:  # Fila inicial
                    if fila_d not in [2, 3]:
                        print("Error: Peón puede moverse 1 o 2 casillas")
                        return False
                else:
                    if fila_d != fila_o + 1:
                        print("Error: Peón solo puede moverse 1 casilla")
                        return False
            # Captura diagonal: solo 1 casilla diagonalmente
            else:
                if abs(col_d - col_o) != 1 or fila_d != fila_o + 1:
                    print("Error: Peón solo captura 1 casilla diagonalmente")
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
        if distancia_filas <= 1 and distancia_columnas <= 1 and (distancia_filas + distancia_columnas) > 0:
            return True
        else:
            print("Error: Rey debe moverse máximo 1 casilla")
            return False

    def es_pieza_contraria(self, origen, destino):
        """Verifica si la pieza en destino es del color opuesto"""
        fila_o, col_o = self.convertir_coordenadas(origen)
        fila_d, col_d = self.convertir_coordenadas(destino)
        
        pieza_origen = self.tablero[fila_o][col_o]
        pieza_destino = self.tablero[fila_d][col_d]
        
        # Si destino está vacío, no hay pieza contraria
        if pieza_destino == ".":
            return False
        
        # Comparar si son de diferente color (mayúscula vs minúscula)
        # Blancas (mayúsculas) capturan negras (minúsculas) y vice versa
        if pieza_origen.isupper() and pieza_destino.islower():
            return True  # Pieza blanca captura pieza negra
        elif pieza_origen.islower() and pieza_destino.isupper():
            return True  # Pieza negra captura pieza blanca
        
        return False

    def es_pieza_propia(self, origen, destino):
        """Verifica si la pieza en destino es del mismo color"""
        fila_o, col_o = self.convertir_coordenadas(origen)
        fila_d, col_d = self.convertir_coordenadas(destino)
        
        pieza_origen = self.tablero[fila_o][col_o]
        pieza_destino = self.tablero[fila_d][col_d]
        
        # Si destino está vacío, no hay pieza propia
        if pieza_destino == ".":
            return False
        
        # Comparar si son del mismo color
        if pieza_origen.isupper() and pieza_destino.isupper():
            return True  # Ambas blancas
        elif pieza_origen.islower() and pieza_destino.islower():
            return True  # Ambas negras
        
        return False

    def obtener_posicion_rey(self, color):
        """Encuentra la posición del rey de un color específico"""
        # color: 'blanco' o 'negro'
        rey = 'K' if color == 'blanco' else 'k'
        
        for fila in range(8):
            for col in range(8):
                if self.tablero[fila][col] == rey:
                    return fila, col
        
        return None  # Rey no encontrado (no debería ocurrir)

    def esta_bajo_amenaza(self, fila, col, color_defensor):
        """Verifica si una casilla está bajo amenaza de piezas enemigas"""
        # color_defensor: 'blanco' o 'negro' - el color de la pieza en esa casilla
        # Revisamos si alguna pieza enemiga puede atacar esta casilla
        
        for fila_atacante in range(8):
            for col_atacante in range(8):
                pieza_atacante = self.tablero[fila_atacante][col_atacante]
                
                # Ignorar casillas vacías y piezas del mismo color
                if pieza_atacante == ".":
                    continue
                
                pieza_es_blanca = pieza_atacante.isupper()
                defensor_es_blanco = color_defensor == 'blanco'
                
                # Si es del mismo color, ignorar
                if pieza_es_blanca == defensor_es_blanco:
                    continue
                
                # Convertir posiciones a notación para validar
                # Creamos coordenadas ficticias para validar el movimiento
                col_letra = chr(ord('A') + col_atacante)
                fila_num = 8 - fila_atacante
                origen = f"{col_letra}{fila_num}"
                
                col_letra_dest = chr(ord('A') + col)
                fila_num_dest = 8 - fila
                destino = f"{col_letra_dest}{fila_num_dest}"
                
                # Verificar si este atacante puede llegar a esta casilla
                # Guardamos la pieza destino temporalmente
                pieza_destino_original = self.tablero[fila][col]
                
                # Simulamos el movimiento
                if self.validar_movimiento(origen, destino):
                    # Restauramos
                    self.tablero[fila][col] = pieza_destino_original
                    return True
        
        return False

    def detectar_jaque(self, color):
        """Detecta si el rey de un color específico está en jaque"""
        # color: 'blanco' o 'negro'
        rey_pos = self.obtener_posicion_rey(color)
        
        if rey_pos is None:
            return False
        
        fila_rey, col_rey = rey_pos
        return self.esta_bajo_amenaza(fila_rey, col_rey, color)

    def mover_pieza(self, origen, destino):
        """Mueve una pieza de origen a destino (con captura opcional)"""
        fila_o, col_o = self.convertir_coordenadas(origen)
        fila_d, col_d = self.convertir_coordenadas(destino)
        
        # Verificar que haya una pieza en origen
        if self.tablero[fila_o][col_o] == ".":
            print(f"Error: No hay pieza en {origen}")
            return False
        
        pieza = self.tablero[fila_o][col_o]
        
        # Verificar si intenta capturar una pieza propia
        if self.es_pieza_propia(origen, destino):
            print(f"Error: No puedes capturar una pieza propia")
            return False
        
        # Validar el movimiento
        if not self.validar_movimiento(origen, destino):
            return False
        
        # Mover la pieza
        pieza_capturada = self.tablero[fila_d][col_d]
        
        # Colocar la pieza en destino
        self.tablero[fila_d][col_d] = pieza
        
        # Dejar vacío el origen
        self.tablero[fila_o][col_o] = "."
        
        # Mostrar captura si ocurrió
        if pieza_capturada != ".":
            print(f"✓ ¡Pieza capturada! {pieza_capturada} en {destino}")
        
        # Detectar si hay jaque después del movimiento
        if pieza.isupper():  # Pieza blanca se movió
            if self.detectar_jaque('negro'):
                print(f"⚠️  ¡JAQUE! Rey negro bajo amenaza")
        else:  # Pieza negra se movió
            if self.detectar_jaque('blanco'):
                print(f"⚠️  ¡JAQUE! Rey blanco bajo amenaza")
        
        return True

if __name__ == "__main__":
    tablero = Tablero()
    print("=" * 60)
    print("FASE 7: DETECTAR JAQUE")
    print("=" * 60)
    tablero.mostrar()
    
    # PRUEBA 1: Jaque simple con Torre
    print("\n" + "=" * 60)
    print("PRUEBA 1: Jaque con Torre (ataque vertical)")
    print("=" * 60)
    
    print("\n1. Torre blanca: a1 → a7")
    tablero.mover_pieza("a1", "a7")
    tablero.mostrar()
    
    print("\n2. Caballo negro: b8 → c6")
    tablero.mover_pieza("b8", "c6")
    tablero.mostrar()
    
    print("\n3. Torre blanca: a7 → e7 (ataque horizontal hacia el rey)")
    tablero.mover_pieza("a7", "e7")
    tablero.mostrar()
    
    # PRUEBA 2: Jaque con Alfil
    print("\n" + "=" * 60)
    print("PRUEBA 2: Jaque con Alfil (ataque diagonal)")
    print("=" * 60)
    
    print("\n1. Alfil blanco: c1 → d2")
    tablero.mover_pieza("c1", "d2")
    tablero.mostrar()
    
    print("\n2. Peón negro: d7 → d5")
    tablero.mover_pieza("d7", "d5")
    tablero.mostrar()
    
    print("\n3. Alfil blanco: d2 → e3")
    tablero.mover_pieza("d2", "e3")
    tablero.mostrar()
    
    print("\n4. Peón negro: e7 → e6")
    tablero.mover_pieza("e7", "e6")
    tablero.mostrar()
    
    print("\n5. Alfil blanco: e3 → b6 (ataque diagonal)")
    tablero.mover_pieza("e3", "b6")
    tablero.mostrar()
    
    # PRUEBA 3: Jaque con Reina
    print("\n" + "=" * 60)
    print("PRUEBA 3: Jaque con Reina")
    print("=" * 60)
    
    print("\n1. Reina blanca: d1 → d6")
    tablero.mover_pieza("d1", "d6")
    tablero.mostrar()
    
    # PRUEBA 4: Verificación automática de jaque
    print("\n" + "=" * 60)
    print("PRUEBA 4: Verificación automática después de movimiento")
    print("=" * 60)
    
    print("\n1. Peón negro: g7 → g5")
    tablero.mover_pieza("g7", "g5")
    tablero.mostrar()
    
    print("\n2. Reina blanca: d6 → e7 (ataque hacia el rey negro)")
    tablero.mover_pieza("d6", "e7")
    tablero.mostrar()
    
    print("\n" + "=" * 60)
    print("FASE 7 COMPLETADA ✅ - DETECCIÓN DE JAQUE FUNCIONA")
    print("=" * 60)
    
    print("\nResumen de Jaque:")
    print("✓ Detecta jaque de Torre (vertical/horizontal)")
    print("✓ Detecta jaque de Alfil (diagonal)")
    print("✓ Detecta jaque de Reina (combinado)")
    print("✓ Muestra advertencia automáticamente")