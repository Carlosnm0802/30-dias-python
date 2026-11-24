from autocorrect import Speller

#Inicializar corrector
corrector = Speller(lang="es")

def corregir_palabra(palabra:str):
    #Utilizar el corrector para corregir la palabra
    if not corrector(palabra) == palabra:
        #Si esta incorrecta, devolver la corrección
        return corrector(palabra)
    else:
        return palabra

print(corregir_palabra("holaa"))