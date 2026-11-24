# Reto 04: corrector ortográfico

Este programa utiliza la biblioteca `autocorrect` para sugerir correcciones ortográficas en español. Actualmente corrige un ejemplo definido en el código y muestra el resultado en la terminal.

## Instalación y ejecución

Desde la raíz del repositorio, crea y activa un entorno virtual e instala las dependencias:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

Después, ejecuta el programa:

```bash
python reto-04/corrector-ortografico.py
```

La primera vez, `autocorrect` puede necesitar descargar el diccionario de español y requerir conexión a internet.

Si aparece `ModuleNotFoundError: No module named 'autocorrect'`, comprueba que el entorno virtual esté activado e instala las dependencias con el comando anterior. No ejecutes el archivo con `/usr/bin/python3`: ese intérprete no utiliza los paquetes instalados en el entorno virtual.

## Cómo funciona

1. Importa `Speller` de la biblioteca `autocorrect`.
2. Crea un corrector en español con `Speller(lang="es")`.
3. La función `corregir_palabra(palabra)` compara la sugerencia del corrector con la palabra original. Si son diferentes, devuelve la sugerencia; de lo contrario, devuelve la palabra original.
4. El programa llama a la función con `"holaa"` y muestra el resultado:

```text
hola
```

Para probar otra palabra, cambia `"holaa"` en la última línea del archivo. El programa no solicita texto por teclado.
