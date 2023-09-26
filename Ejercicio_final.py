import random
import diagrama_de_muñeco

diccionario = {"Terror": "lamonja","Aventura": "avatar","Carreras": "rapidoyfurioso","Caricatura": "nemo","Niños":"pepapig"}

vidas = 6

print("Bienvenido al juego de ahorcado")
print("Presiona Enter para comenzar")
inicio = input ("")

palabra = random.choice(list(diccionario.values()))

categoria = []

for key, value in diccionario.items():
        if value == palabra:
            categoria = key
            break

numero_de_letras = 0
letras_separadas = []
guiones = []

for i in palabra:
        i = guiones.append("_")
        numero_de_letras += 1

for i in palabra:
    letras_separadas.append(i)

while vidas>0:
    palabra_actualizada = []

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
    if vidas == 6:
         diagrama_de_muñeco.fase_0()
    elif vidas == 5:
         diagrama_de_muñeco.fase_1()
    elif vidas == 4:
         diagrama_de_muñeco.fase_2()
    elif vidas == 3:
         diagrama_de_muñeco.fase_3()
    elif vidas == 2:
         diagrama_de_muñeco.fase_4()
    elif vidas == 1:
         diagrama_de_muñeco.fase_5()
    else:
         break


    print(f"Tienes : {vidas} oportunidades.")
    print(f"La cantidad de letras es: {numero_de_letras}")
    print(f"El genero de la pelicula es: {categoria}")
    print(f"{guiones}")
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")

    dato = input("Ingresa UNA LETRA EN MINUSCULA:  ")

    acierto = 0

    for i in range(len(letras_separadas)):
        if dato == letras_separadas[i]:
            guiones[i] = dato
            acierto +=1
        else:
             i = i
        
    if acierto == 0:
         vidas = vidas - 1

    if "_" not in guiones:
        print("Felicidades, ganaste el juego!\n")
        print(f"La palabra es: {palabra}")
        break

while vidas == 0:
     
    diagrama_de_muñeco.fase_6()
    
    print(f"Tienes : {vidas} oportunidades.")
    print(f"La cantidad de letras es: {numero_de_letras}")
    print(f"El genero de la pelicula es: {categoria}")
    print(f"{guiones}")
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")

    dato = input("Ingresa UNA LETRA EN MINUSCULA:  ")

    acierto = 0

    for i in range(len(letras_separadas)):
        if dato == letras_separadas[i]:
            guiones[i] = dato
            acierto +=1
        else:
             i = i

    if "_" not in guiones:
        print("Felicidades, ganaste el juego!")
    else:
         vidas = vidas - 1

while vidas<0:
    print(f"Perdiste. El numerodeintentos se agotó\n")
    print(f"La palabra era {palabra}")
    break
             