# Documentación del Tablero de Ajedrez - FASE 7: DETECTAR JAQUE

## 📋 Índice
1. [Estructura General](#estructura-general)
2. [Funciones de Validación de Movimientos](#funciones-de-validación-de-movimientos)
3. [Funciones de Detección de Jaque](#funciones-de-detección-de-jaque)
4. [Función Principal: mover_pieza](#función-principal-mover_pieza)
5. [Flujo de Ejecución](#flujo-de-ejecución)

---

## Estructura General

### Clase `Tablero`
La clase principal que representa el tablero de ajedrez y todas sus funcionalidades.

#### Atributos:
- `self.tablero`: Matriz 8x8 que contiene todas las piezas
- `self.filas`: Número de filas (8)
- `self.columnas`: Número de columnas (8)

#### Inicialización:
```python
def __init__(self):
    self.tablero = [["." for _ in range(8)] for _ in range(8)]  # Crear tablero vacío
    self.inicializar_piezas()  # Colocar todas las piezas en posición inicial
```

---

## Funciones de Validación de Movimientos

### 1. `convertir_coordenadas(coordenada)`
**Propósito**: Convertir notación de ajedrez (como "e2") a índices de matriz.

**Ejemplo**:
- Entrada: "e2"
- Salida: (6, 4) → fila 6, columna 4

**Lógica**:
```
Columnas: A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7
Filas: 1→7, 2→6, 3→5, 4→4, 5→3, 6→2, 7→1, 8→0
(Porque fila_índice = 8 - número_fila)
```

---

### 2. `validar_movimiento(origen, destino)`
**Propósito**: Router central que valida movimientos según el tipo de pieza.

**Flujo**:
1. Convierte las coordenadas
2. Obtiene la pieza en origen
3. Llama a la función específica según el tipo de pieza

---

### 3. `validar_peon(fila_o, col_o, fila_d, col_d, pieza)`
**Reglas**:
- **Peón Blanco (P)**:
  - Movimiento normal: 1 o 2 casillas hacia adelante (desde fila inicial)
  - Captura: diagonal, 1 casilla
  
- **Peón Negro (p)**:
  - Movimiento normal: 1 o 2 casillas hacia adelante (desde fila inicial)
  - Captura: diagonal, 1 casilla

**Diferencia de dirección**:
- Blanco: decrece fila (fila_o - 1, fila_o - 2)
- Negro: incrementa fila (fila_o + 1, fila_o + 2)

---

### 4. `validar_torre(fila_o, col_o, fila_d, col_d, pieza)`
**Regla**: Se mueve en línea recta (horizontal o vertical)

**Validación**:
```
fila_o == fila_d  → Movimiento horizontal (misma fila)
O
col_o == col_d    → Movimiento vertical (misma columna)
```

---

### 5. `validar_caballo(fila_o, col_o, fila_d, col_d, pieza)`
**Regla**: Se mueve en forma de L (2+1 o 1+2)

**Validación**:
```
(2 filas y 1 columna) O (1 fila y 2 columnas)
```

**Particularidad**: Es la única pieza que puede saltar sobre otras.

---

### 6. `validar_alfil(fila_o, col_o, fila_d, col_d, pieza)`
**Regla**: Se mueve en diagonal puro

**Validación**:
```
|fila_destino - fila_origen| == |col_destino - col_origen|
Y
distancia > 0
```

---

### 7. `validar_reina(fila_o, col_o, fila_d, col_d, pieza)`
**Regla**: Combina movimientos de Torre + Alfil

**Validación**:
```
Puede moverse como Torre: fila_o == fila_d OR col_o == col_d
O
Puede moverse como Alfil: distancia_filas == distancia_columnas
```

---

### 8. `validar_rey(fila_o, col_o, fila_d, col_d, pieza)`
**Regla**: Se mueve máximo 1 casilla en cualquier dirección

**Validación**:
```
distancia_filas <= 1 AND
distancia_columnas <= 1 AND
(distancia_filas + distancia_columnas) > 0
```

La última condición asegura que se mueva al menos a 1 casilla (no puede quedarse quieto).

---

## Funciones de Detección de Jaque

### 1. `obtener_posicion_rey(color)`
**Propósito**: Encontrar la posición del rey en el tablero

**Parámetro**:
- `color`: 'blanco' (busca 'K') o 'negro' (busca 'k')

**Retorno**:
- Tupla: (fila, columna) del rey
- None si no se encuentra (no debería ocurrir)

**Proceso**:
1. Recorre cada casilla del tablero
2. Si encuentra el rey, retorna su posición
3. Si no lo encuentra, retorna None

---

### 2. `esta_bajo_amenaza(fila, col, color_defensor)`
**Propósito**: Verificar si una casilla está bajo amenaza de piezas enemigas

**Parámetros**:
- `fila, col`: Casilla a verificar
- `color_defensor`: Color de la pieza que defiende (blanco o negro)

**Proceso**:
1. Recorre todas las casillas del tablero
2. Para cada pieza enemiga encontrada:
   - Convierte posiciones a notación de ajedrez
   - Simula el movimiento usando `validar_movimiento()`
   - Si el movimiento es válido, la casilla está bajo amenaza
3. Retorna True si está bajo amenaza, False si está segura

**Nota**: Esta función no verifica obstáculos entre casillas (eso se hace en las funciones de validación).

---

### 3. `detectar_jaque(color)`
**Propósito**: Detectar si el rey de un color está en jaque

**Jaque**: Significa que el rey está bajo amenaza (atacado por una pieza enemiga)

**Proceso**:
1. Obtiene la posición del rey
2. Verifica si esa posición está bajo amenaza
3. Retorna True si hay jaque, False si no

**Ejemplo**:
```python
if tablero.detectar_jaque('negro'):
    print("⚠️ ¡JAQUE! Rey negro bajo amenaza")
```

---

## Función Principal: mover_pieza

### `mover_pieza(origen, destino)`
**Propósito**: Realizar un movimiento y actualizar el estado del juego

**Parámetros**:
- `origen`: Coordenadas en notación de ajedrez (ej: "e2")
- `destino`: Coordenadas en notación de ajedrez (ej: "e4")

**Proceso paso a paso**:

1. **Convertir coordenadas**:
   ```python
   fila_o, col_o = self.convertir_coordenadas(origen)
   fila_d, col_d = self.convertir_coordenadas(destino)
   ```

2. **Verificar que hay una pieza en origen**:
   ```python
   if self.tablero[fila_o][col_o] == ".":
       print("Error: No hay pieza en origen")
       return False
   ```

3. **Verificar que no capture pieza propia**:
   ```python
   if self.es_pieza_propia(origen, destino):
       print("Error: No puedes capturar una pieza propia")
       return False
   ```

4. **Validar el movimiento según las reglas**:
   ```python
   if not self.validar_movimiento(origen, destino):
       return False
   ```

5. **Realizar el movimiento**:
   ```python
   pieza_capturada = self.tablero[fila_d][col_d]
   self.tablero[fila_d][col_d] = pieza
   self.tablero[fila_o][col_o] = "."
   ```

6. **Mostrar captura si ocurrió**:
   ```python
   if pieza_capturada != ".":
       print(f"✓ ¡Pieza capturada! {pieza_capturada}")
   ```

7. **Detectar jaque después del movimiento**:
   ```python
   if pieza.isupper():  # Pieza blanca se movió
       if self.detectar_jaque('negro'):
           print("⚠️ ¡JAQUE! Rey negro bajo amenaza")
   ```

**Retorno**:
- True si el movimiento fue exitoso
- False si hay algún error

---

## Flujo de Ejecución

### Ejemplo: Torre blanca de a1 a a7

```
1. Llamar: tablero.mover_pieza("a1", "a7")
   ↓
2. Convertir coordenadas:
   origen: a1 → (7, 0)
   destino: a7 → (1, 0)
   ↓
3. Verificar que hay pieza en a1
   tablero[7][0] = 'T' ✓
   ↓
4. Obtener pieza: 'T' (Torre blanca)
   ↓
5. Verificar que no es pieza propia
   tablero[1][0] = 'p' (peón negro) → Es contraria ✓
   ↓
6. Validar movimiento de Torre:
   validar_torre(7, 0, 1, 0, 'T')
   → ¿fila_o == fila_d? 7 == 1? NO
   → ¿col_o == col_d? 0 == 0? SÍ ✓
   → Es línea recta vertical → VÁLIDO
   ↓
7. Realizar movimiento:
   tablero[1][0] = 'T'  (colocar Torre en destino)
   tablero[7][0] = '.'  (vaciar origen)
   ↓
8. Mostrar captura:
   "✓ ¡Pieza capturada! p en a7"
   ↓
9. Detectar jaque:
   detectar_jaque('negro')
   → obtener_posicion_rey('negro') → (0, 4)  Rey en e8
   → esta_bajo_amenaza(0, 4, 'negro')
   → Verifica si alguna pieza blanca puede atacar e8
   → Torre en a7 puede atacar? validar_movimiento("a7", "e8")?
   → ¿col_o == col_d? NO (0 != 4)
   → ¿fila_o == fila_d? NO (1 != 0)
   → NO PUEDE ATACAR (aún)
   ↓
10. Retornar True (movimiento exitoso)
```

---

## Representación de Piezas

| Pieza | Blanca | Negra | Significado |
|-------|--------|-------|-------------|
| Peón | P | p | Pawn |
| Torre | T | t | Torre (Rook) |
| Caballo | C | c | Caballo (Knight) |
| Alfil | A | a | Alfil (Bishop) |
| Reina | Q | q | Reina (Queen) |
| Rey | K | k | Rey (King) |
| Vacío | . | . | Casilla vacía |

---

## Notas Importantes

✅ **Mayúsculas = Piezas Blancas**
✅ **Minúsculas = Piezas Negras**
✅ **Punto (.) = Casilla Vacía**

✅ **Sistema de Coordenadas**:
- Columnas: A(0) → H(7)
- Filas: 8(0) → 1(7)

✅ **Jaque**: El rey está siendo atacado por una pieza enemiga
✅ **Próxima fase**: Jaque Mate (rey sin escape posible)

---

## Resumen del Código

Este sistema implementa un completo detector de jaque para un tablero de ajedrez con:
- ✓ Validación de movimientos para 6 tipos de piezas
- ✓ Detección de jaque automática
- ✓ Captura de piezas
- ✓ Visualización del tablero
- ✓ Mensajes de error descriptivos
