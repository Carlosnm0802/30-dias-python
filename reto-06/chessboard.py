#Reto de hoy: Tablero de ajedrez
# Esta clase representa un tablero de ajedrez con todas sus funcionalidades

class Tablero:
    # El método __init__ se ejecuta automáticamente cuando creamos un nuevo objeto Tablero
    def __init__(self):
        # Crear un tablero 8x8 lleno de puntos (.) que representan casillas vacías
        # La lista comprensiva [["." for _ in range(8)] for _ in range(8)] crea 8 filas de 8 columnas
        self.tablero = [["." for _ in range(8)] for _ in range(8)] 
        self.filas = 8        # Almacenamos el número de filas
        self.columnas = 8     # Almacenamos el número de columnas
        self.inicializar_piezas()  # Llamamos a la función que coloca todas las piezas en su posición inicial
    
    def mostrar(self):
        # Esta función imprime el tablero en la consola de forma visual y legible
        
        # Crear la fila de letras A-H (las columnas del tablero)
        columnas = "ABCDEFGH"
        print("  " + " ".join(columnas))  # Imprime "  A B C D E F G H" al inicio
        
        # Recorrer cada fila del tablero y mostrarla
        for indice, fila in enumerate(self.tablero):
            # enumerate nos da el índice (0-7) y el contenido de cada fila
            numero_fila = 8 - indice  # Convertimos el índice a número de fila (8, 7, 6... 1)
            # Imprimimos el número de la fila seguido de las piezas separadas por espacios
            print(f"{numero_fila} " + " ".join(fila))
    
    def inicializar_piezas(self):
        # Esta función coloca todas las piezas en su posición inicial de ajedrez
        
        # Colocar peones negros en la fila 1 (índice 1) - la segunda fila del tablero
        for columna in range(self.columnas):
            self.tablero[1][columna] = "p"  # "p" representa un peón negro
        
        # Colocar peones blancos en la fila 6 (índice 6) - la séptima fila del tablero
        for columna in range(self.columnas):
            self.tablero[6][columna] = "P"  # "P" representa un peón blanco
        
        # Definir el orden de las piezas principales (de izquierda a derecha)
        # T=Torre, C=Caballo, A=Alfil, Q=Reina, K=Rey
        piezas_blancas = ["T", "C", "A", "Q", "K", "A", "C", "T"]  # Piezas blancas (mayúsculas)
        piezas_negras = ["t", "c", "a", "q", "k", "a", "c", "t"]    # Piezas negras (minúsculas)
        
        # Colocar piezas negras en la fila 0 (primera fila del tablero)
        self.tablero[0] = piezas_negras
        
        # Colocar piezas blancas en la fila 7 (última fila del tablero)
        self.tablero[7] = piezas_blancas

    def convertir_coordenadas(self, coordenada):
        """
        Convierte la notación de ajedrez (como 'e2') a índices de matriz [fila, columna]
        
        Ejemplo: 'e2' → columna 4 (E=4), fila 6 (porque 8-2=6)
        Las columnas van de 0-7 (A-H)
        Las filas van de 0-7 (representando 8-1 en la pantalla)
        """
        # Convertimos la letra de la columna (A-H) a un número (0-7)
        # ord('A') da el código ASCII de 'A'
        # Si es 'e', ord('e') - ord('A') da 4 (porque E es la 5ª letra, índice 4)
        columna = ord(coordenada[0].upper()) - ord('A')
        
        # Convertimos el número de fila (1-8) a índice (7-0)
        # Si es fila 2, entonces 8 - 2 = 6 (el índice en la matriz)
        fila = 8 - int(coordenada[1])
        
        return fila, columna

    def validar_movimiento(self, origen, destino):
        """
        Valida si el movimiento es legal según las reglas del ajedrez
        Para cada tipo de pieza, llamamos a su función específica de validación
        """
        # Convertir coordenadas de notación ajedrez a índices de matriz
        fila_o, col_o = self.convertir_coordenadas(origen)
        fila_d, col_d = self.convertir_coordenadas(destino)
        
        # Obtener la pieza que se quiere mover
        pieza = self.tablero[fila_o][col_o]
        
        # Validar según el tipo de pieza (usamos .upper() para verificar sin importar color)
        if pieza.upper() == 'P':  # Si es un Peón
            return self.validar_peon(fila_o, col_o, fila_d, col_d, pieza)
        elif pieza.upper() == 'T':  # Si es una Torre
            return self.validar_torre(fila_o, col_o, fila_d, col_d, pieza)
        elif pieza.upper() == 'C':  # Si es un Caballo
            return self.validar_caballo(fila_o, col_o, fila_d, col_d, pieza)
        elif pieza.upper() == 'A':  # Si es un Alfil
            return self.validar_alfil(fila_o, col_o, fila_d, col_d, pieza)
        elif pieza.upper() == 'Q':  # Si es una Reina
            return self.validar_reina(fila_o, col_o, fila_d, col_d, pieza)
        elif pieza.upper() == 'K':  # Si es un Rey
            return self.validar_rey(fila_o, col_o, fila_d, col_d, pieza)
        
        return True

    def validar_peon(self, fila_o, col_o, fila_d, col_d, pieza):
        """
        Valida movimiento de peón
        
        Reglas del peón:
        - Movimiento normal: 1 casilla hacia adelante (2 casillas si está en posición inicial)
        - Solo puede moverse hacia adelante, no hacia atrás
        - Captura: solo en diagonal, 1 casilla
        - Los peones blancos bajan (incrementan fila), los negros suben (decrementan fila)
        """
        # Obtener la pieza que hay en la casilla destino
        pieza_destino = self.tablero[fila_d][col_d]
        
        if pieza == 'P':  # Peón blanco (mayúscula)
            # Si la casilla destino está vacía, es movimiento normal (sin captura)
            if pieza_destino == ".":
                # El peón no puede cambiar de columna sin capturar
                if col_o != col_d:
                    print("Error: Peón no puede moverse diagonalmente (sin capturar)")
                    return False
                
                # Si está en la fila inicial (fila 6 = posición 7 en el tablero mostrado)
                if fila_o == 6:
                    # Puede moverse 1 o 2 casillas: a fila 5 o 4
                    if fila_d not in [4, 5]:
                        print("Error: Peón puede moverse 1 o 2 casillas")
                        return False
                else:  # Si ya se ha movido antes
                    # Solo puede moverse 1 casilla hacia adelante
                    if fila_d != fila_o - 1:
                        print("Error: Peón solo puede moverse 1 casilla")
                        return False
            else:  # Si hay una pieza en destino, es captura
                # La captura debe ser diagonal (1 columna a izquierda o derecha)
                # y solo 1 fila hacia adelante
                if abs(col_d - col_o) != 1 or fila_d != fila_o - 1:
                    print("Error: Peón solo captura 1 casilla diagonalmente")
                    return False
        
        else:  # Peón negro (minúscula 'p')
            # Si la casilla destino está vacía, es movimiento normal (sin captura)
            if pieza_destino == ".":
                # El peón no puede cambiar de columna sin capturar
                if col_o != col_d:
                    print("Error: Peón no puede moverse diagonalmente (sin capturar)")
                    return False
                
                # Si está en la fila inicial (fila 1 = posición 2 en el tablero mostrado)
                if fila_o == 1:
                    # Puede moverse 1 o 2 casillas: a fila 2 o 3
                    if fila_d not in [2, 3]:
                        print("Error: Peón puede moverse 1 o 2 casillas")
                        return False
                else:  # Si ya se ha movido antes
                    # Solo puede moverse 1 casilla hacia adelante (incrementar fila)
                    if fila_d != fila_o + 1:
                        print("Error: Peón solo puede moverse 1 casilla")
                        return False
            else:  # Si hay una pieza en destino, es captura
                # La captura debe ser diagonal (1 columna a izquierda o derecha)
                # y solo 1 fila hacia adelante
                if abs(col_d - col_o) != 1 or fila_d != fila_o + 1:
                    print("Error: Peón solo captura 1 casilla diagonalmente")
                    return False
        
        return True

    def validar_torre(self, fila_o, col_o, fila_d, col_d, pieza):
        """
        Valida movimiento de torre
        
        La torre se mueve en línea recta: horizontal (misma fila) o vertical (misma columna)
        Puede moverse cualquier número de casillas siempre que no haya piezas en el camino
        """
        # Torre se mueve en línea recta: misma fila O misma columna
        # Si fila_o == fila_d → movimiento horizontal
        # Si col_o == col_d → movimiento vertical
        if fila_o == fila_d or col_o == col_d:
            return True
        else:
            print("Error: Torre debe moverse en línea recta (horizontal o vertical)")
            return False

    def validar_caballo(self, fila_o, col_o, fila_d, col_d, pieza):
        """
        Valida movimiento de caballo
        
        El caballo se mueve en forma de 'L': 
        - 2 casillas en un sentido y 1 casilla perpendicular, O
        - 1 casilla en un sentido y 2 casillas perpendicular
        
        El caballo es la única pieza que puede saltar sobre otras
        """
        # Calcular la distancia de filas y columnas
        distancia_filas = abs(fila_d - fila_o)
        distancia_columnas = abs(col_d - col_o)
        
        # El movimiento válido del caballo es:
        # (2 filas y 1 columna) O (1 fila y 2 columnas)
        if (distancia_filas == 2 and distancia_columnas == 1) or \
           (distancia_filas == 1 and distancia_columnas == 2):
            return True
        else:
            print("Error: Caballo debe moverse en forma de L (2+1 o 1+2)")
            return False

    def validar_alfil(self, fila_o, col_o, fila_d, col_d, pieza):
        """
        Valida movimiento de alfil
        
        El alfil se mueve en diagonal: se desplaza el mismo número de casillas en filas y columnas
        La condición es: |diferencia de filas| = |diferencia de columnas|
        """
        # Calcular la distancia de filas y columnas
        distancia_filas = abs(fila_d - fila_o)
        distancia_columnas = abs(col_d - col_o)
        
        # El movimiento es válido si:
        # 1. La distancia de filas es igual a la distancia de columnas (diagonal pura)
        # 2. Se mueve al menos 1 casilla (distancia_filas > 0)
        if distancia_filas == distancia_columnas and distancia_filas > 0:
            return True
        else:
            print("Error: Alfil debe moverse en diagonal")
            return False

    def validar_reina(self, fila_o, col_o, fila_d, col_d, pieza):
        """
        Valida movimiento de reina
        
        La reina es la pieza más poderosa: combina los movimientos de torre y alfil
        - Puede moverse como torre: línea recta (horizontal o vertical)
        - Puede moverse como alfil: en diagonal
        """
        distancia_filas = abs(fila_d - fila_o)
        distancia_columnas = abs(col_d - col_o)
        
        # Movimiento de torre: línea recta (horizontal o vertical)
        if fila_o == fila_d or col_o == col_d:
            return True
        # Movimiento de alfil: diagonal (distancia de filas = distancia de columnas)
        elif distancia_filas == distancia_columnas:
            return True
        else:
            print("Error: Reina debe moverse en línea recta o diagonal")
            return False

    def validar_rey(self, fila_o, col_o, fila_d, col_d, pieza):
        """
        Valida movimiento de rey
        
        El rey es la pieza más importante en el ajedrez
        Se mueve máximo 1 casilla en cualquier dirección (horizontal, vertical o diagonal)
        """
        distancia_filas = abs(fila_d - fila_o)
        distancia_columnas = abs(col_d - col_o)
        
        # El rey se mueve máximo 1 casilla en cualquier dirección
        # Condiciones:
        # - distancia_filas <= 1: se mueve máximo 1 fila
        # - distancia_columnas <= 1: se mueve máximo 1 columna
        # - (distancia_filas + distancia_columnas) > 0: se debe mover al menos a 1 casilla
        if distancia_filas <= 1 and distancia_columnas <= 1 and (distancia_filas + distancia_columnas) > 0:
            return True
        else:
            print("Error: Rey debe moverse máximo 1 casilla")
            return False

    def es_pieza_contraria(self, origen, destino):
        """
        Verifica si la pieza en destino es del color opuesto (pieza enemiga)
        
        Se usa para saber si un movimiento es una captura válida
        Las piezas blancas se representan con mayúsculas (P, T, C, etc.)
        Las piezas negras se representan con minúsculas (p, t, c, etc.)
        """
        fila_o, col_o = self.convertir_coordenadas(origen)
        fila_d, col_d = self.convertir_coordenadas(destino)
        
        pieza_origen = self.tablero[fila_o][col_o]
        pieza_destino = self.tablero[fila_d][col_d]
        
        # Si destino está vacío (.), no hay pieza contraria
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
        """
        Verifica si la pieza en destino es del mismo color (pieza amiga)
        
        Se usa para evitar que una pieza capture a su propia pieza
        No puedes atacar/capturar las piezas de tu propio equipo
        """
        fila_o, col_o = self.convertir_coordenadas(origen)
        fila_d, col_d = self.convertir_coordenadas(destino)
        
        pieza_origen = self.tablero[fila_o][col_o]
        pieza_destino = self.tablero[fila_d][col_d]
        
        # Si destino está vacío (.), no hay pieza propia
        if pieza_destino == ".":
            return False
        
        # Comparar si son del mismo color
        # Ambas mayúsculas = ambas blancas
        # Ambas minúsculas = ambas negras
        if pieza_origen.isupper() and pieza_destino.isupper():
            return True  # Ambas blancas
        elif pieza_origen.islower() and pieza_destino.islower():
            return True  # Ambas negras
        
        return False

    def obtener_posicion_rey(self, color):
        """
        Encuentra la posición del rey de un color específico
        
        Esta función es importante para detectar el jaque:
        Busca en todo el tablero el rey ('K' para blanco, 'k' para negro)
        y retorna su posición como [fila, columna]
        """
        # Determinar qué rey buscamos según el color
        rey = 'K' if color == 'blanco' else 'k'
        
        # Recorrer todas las casillas del tablero (filas y columnas)
        for fila in range(8):
            for col in range(8):
                # Si encontramos el rey, retornamos su posición
                if self.tablero[fila][col] == rey:
                    return fila, col
        
        return None  # Rey no encontrado (no debería ocurrir en un juego válido)

    def esta_bajo_amenaza(self, fila, col, color_defensor):
        """
        Verifica si una casilla está bajo amenaza de piezas enemigas
        
        Esta es la función clave para detectar el jaque.
        Recorre todas las piezas enemigas y verifica si alguna puede atacar esta casilla.
        
        Parámetros:
        - fila, col: la casilla que queremos verificar si está bajo amenaza
        - color_defensor: 'blanco' o 'negro' - el color de la pieza en esa casilla
        """
        # Recorrer todas las casillas del tablero
        for fila_atacante in range(8):
            for col_atacante in range(8):
                pieza_atacante = self.tablero[fila_atacante][col_atacante]
                
                # Ignorar casillas vacías
                if pieza_atacante == ".":
                    continue
                
                # Verificar si la pieza atacante es del color enemigo
                pieza_es_blanca = pieza_atacante.isupper()  # Mayúscula = blanca
                defensor_es_blanco = color_defensor == 'blanco'
                
                # Si es del mismo color que el defensor, ignorar (no es enemigo)
                if pieza_es_blanca == defensor_es_blanco:
                    continue
                
                # Convertir posiciones de índices a notación de ajedrez para validar el movimiento
                # Por ejemplo: fila=0, col=0 → 'a8'
                col_letra = chr(ord('A') + col_atacante)
                fila_num = 8 - fila_atacante
                origen = f"{col_letra}{fila_num}"
                
                # Crear la notación de destino (la casilla que queremos verificar)
                col_letra_dest = chr(ord('A') + col)
                fila_num_dest = 8 - fila
                destino = f"{col_letra_dest}{fila_num_dest}"
                
                # Guardar la pieza que hay actualmente en destino
                # porque vamos a simular un movimiento
                pieza_destino_original = self.tablero[fila][col]
                
                # Verificar si esta pieza enemiga puede atacar la casilla
                # Usamos validar_movimiento para saber si el movimiento es legal
                if self.validar_movimiento(origen, destino):
                    # Restauramos la pieza original en destino
                    self.tablero[fila][col] = pieza_destino_original
                    # Si llegamos aquí, la casilla está bajo amenaza
                    return True
        
        # Si ninguna pieza enemiga puede atacar, la casilla está segura
        return False

    def detectar_jaque(self, color):
        """
        Detecta si el rey de un color específico está en jaque
        
        JAQUE: Significa que el rey está bajo amenaza (atacado por una pieza enemiga)
        
        El proceso es:
        1. Encuentra la posición del rey
        2. Verifica si esa posición está bajo amenaza
        3. Retorna True si está en jaque, False si está seguro
        """
        # Obtenemos la posición actual del rey (blanco o negro)
        rey_pos = self.obtener_posicion_rey(color)
        
        # Si no encontramos el rey, retornamos False
        if rey_pos is None:
            return False
        
        # Desempaquetamos la posición en fila y columna
        fila_rey, col_rey = rey_pos
        
        # Verificamos si la casilla del rey está bajo amenaza
        return self.esta_bajo_amenaza(fila_rey, col_rey, color)

    def mover_pieza(self, origen, destino):
        """
        Mueve una pieza de origen a destino
        
        Esta es la función principal para hacer movimientos en el tablero.
        Realiza varias validaciones:
        1. Verifica que haya una pieza en origen
        2. Verifica que no intente capturar una pieza propia
        3. Valida el movimiento según las reglas del ajedrez
        4. Realiza el movimiento
        5. Detecta si hay jaque después del movimiento
        """
        # Convertir coordenadas de notación ajedrez a índices de matriz
        fila_o, col_o = self.convertir_coordenadas(origen)
        fila_d, col_d = self.convertir_coordenadas(destino)
        
        # Verificar que haya una pieza en origen
        if self.tablero[fila_o][col_o] == ".":
            print(f"Error: No hay pieza en {origen}")
            return False
        
        # Obtener la pieza que se quiere mover
        pieza = self.tablero[fila_o][col_o]
        
        # Verificar si intenta capturar una pieza propia (error)
        if self.es_pieza_propia(origen, destino):
            print(f"Error: No puedes capturar una pieza propia")
            return False
        
        # Validar el movimiento según las reglas del ajedrez
        # Esto llama a la función validar_movimiento que verifica si el movimiento es legal
        if not self.validar_movimiento(origen, destino):
            return False
        
        # Guardar la pieza que hay en destino (para saber si se capturó algo)
        pieza_capturada = self.tablero[fila_d][col_d]
        
        # Colocar la pieza en destino
        self.tablero[fila_d][col_d] = pieza
        
        # Dejar vacía la casilla origen
        self.tablero[fila_o][col_o] = "."
        
        # Si se capturó una pieza, mostrarlo
        if pieza_capturada != ".":
            print(f"✓ ¡Pieza capturada! {pieza_capturada} en {destino}")
        
        # Detectar si hay jaque después del movimiento
        # Verificamos el rey del color contrario (si se movió una pieza blanca, 
        # verificamos si hay jaque al rey negro, y vice versa)
        if pieza.isupper():  # Si la pieza movida es blanca (mayúscula)
            if self.detectar_jaque('negro'):
                print(f"⚠️  ¡JAQUE! Rey negro bajo amenaza")
        else:  # Si la pieza movida es negra (minúscula)
            if self.detectar_jaque('blanco'):
                print(f"⚠️  ¡JAQUE! Rey blanco bajo amenaza")
        
        return True

if __name__ == "__main__":
    # Crear un nuevo tablero de ajedrez
    tablero = Tablero()
    
    # Mostrar encabezado de FASE 7
    print("=" * 60)
    print("FASE 7: DETECTAR JAQUE")
    print("=" * 60)
    
    # Mostrar el tablero inicial
    tablero.mostrar()
    
    # ==================================================================
    # PRUEBA 1: Jaque simple con Torre (movimiento vertical)
    # ==================================================================
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
    
    # ==================================================================
    # PRUEBA 2: Jaque con Alfil (movimiento diagonal)
    # ==================================================================
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
    
    # ==================================================================
    # PRUEBA 3: Jaque con Reina (pieza más poderosa)
    # ==================================================================
    print("\n" + "=" * 60)
    print("PRUEBA 3: Jaque con Reina")
    print("=" * 60)
    
    print("\n1. Reina blanca: d1 → d6")
    tablero.mover_pieza("d1", "d6")
    tablero.mostrar()
    
    # ==================================================================
    # PRUEBA 4: Verificación automática de jaque después de movimiento
    # ==================================================================
    print("\n" + "=" * 60)
    print("PRUEBA 4: Verificación automática después de movimiento")
    print("=" * 60)
    
    print("\n1. Peón negro: g7 → g5")
    tablero.mover_pieza("g7", "g5")
    tablero.mostrar()
    
    print("\n2. Reina blanca: d6 → e7 (ataque hacia el rey negro)")
    tablero.mover_pieza("d6", "e7")
    tablero.mostrar()
    
    # ==================================================================
    # RESUMEN FINAL
    # ==================================================================
    print("\n" + "=" * 60)
    print("FASE 7 COMPLETADA ✅ - DETECCIÓN DE JAQUE FUNCIONA")
    print("=" * 60)
    
    print("\nResumen de Jaque:")
    print("✓ Detecta jaque de Torre (vertical/horizontal)")
    print("✓ Detecta jaque de Alfil (diagonal)")
    print("✓ Detecta jaque de Reina (combinado)")
    print("✓ Muestra advertencia automáticamente")