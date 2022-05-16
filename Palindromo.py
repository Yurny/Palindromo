
texto = input("Ingrese el caracter que desea evaluar: ")

def es_palindromo(texto):
    texto = texto.lower() #devuelve lo caracteres en minuscula
    texto = texto.replace(' ', '')#reemplaza los espacios
    longitud = len(texto) #len devuelve la cantidad de caracteres
    if longitud % 2 == 0:
        izquierda = texto[:longitud // 2]
        derecha = texto[longitud // 2:]
    else:
        izquierda = texto[:longitud // 2]
        derecha = texto[longitud // 2 + 1:]
    
    return izquierda == derecha[::-1] #:: lectura de derecha a izquierda

print(f"¿el siguiente caracter es palindromo? {es_palindromo(texto)}")




