import random
import time
iniciar_trivia = True 
intentos = 0 
puntaje = 0
punto = 0
puntaje = random.randint(0, 10)
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
print(MAGENTA+"\033[1m"+"\n.....:::::¡Bienvenido a mi trivia!:::::.....\n"+RESET)
time.sleep(1)
print(CYAN+"...:::Pondremos a prueba tus conocimientos:::...\n"+RESET+"\033[0m")
time.sleep(1)
print("Comenzarás con",puntaje,"puntos\n")
time.sleep(1)
nombre = input(BLUE+"Ingresa tu nombre: "+RESET)
time.sleep(1)
print(YELLOW+"\n+============================================================+")
print("\t¡ Hola,",nombre+"!")
print ("Responde las siguientes preguntas escribiendo la letra de la\nalternativa y presionando 'Entrer' para enviar tu respuesta: ")
print("+============================================================+\n"+RESET)
time.sleep(2)
print(RED+"Aviso:"+RESET,"\n- Los puntos ganados o perdidos varian entre el 0 al 10")
print("- Algunas respuestas te pueden '+', '-', '*' o '/' tu puntaje total")
print("- Hay mensajes secretos que te permitiran ganar entre 10 a 100 puntos")
time.sleep(2)
while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  lista_puntos = []
  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar\n")
  for numero_carga in range (5,0,-1):
    print(numero_carga)
    time.sleep(1)      
  #Pregunta 1
  print(YELLOW+"\n1. ¿De qué nacionalidad era Juana de Arco?"+RESET)
  print('''
a. Inglesa
b. Italiana
c. Francesa
d. Alemana\n''')
  time.sleep(2)
  respuesta_1 = input(BLUE+"Tu respuesta: "+RESET) 
  respuesta_1 = respuesta_1.lower()
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input(GREEN+"\nDebes responder 'a', 'b', 'c' o 'd'. \nIngresa nuevamente tu respuesta: "+RESET)
    respuesta_1 = respuesta_1.lower()
  if respuesta_1 == "c":
    punto = random.randint(0, 10)
    lista_puntos.append(punto)
    puntaje += punto
    print("\nCorrecto", nombre, "!")
    print("\nGanastes",punto,"puntos")
    print("Puntaje actual: ",puntaje)
  else:
    punto = random.randint(-10,0)
    lista_puntos.append(punto)
    puntaje += punto
    print("\nIncorrecto", nombre, "!")
    print("\nPerdistes",punto,"puntos")
    print("Puntaje actual: ",puntaje)
  time.sleep(2)
  #Pregunta 2
  print(YELLOW+"\n2. ¿Quién dibujo al famoso Hombre de Vitruvio?\n"+RESET)
  print('''
a. Miguel Angel
b. Leonardo da Vinci
c. Ruben
d. Donatello\n''')
  time.sleep(2)
  respuesta_2 = input(BLUE+"Tu respuesta: "+RESET) 
  respuesta_2 = respuesta_2.lower()
  while respuesta_2 not in ("a", "b", "c", "d", "x"):
    respuesta_2 = input(GREEN+"\nDebes responder 'a', 'b', 'c' o 'd'. \nIngresa   nuevamente tu respuesta: "+RESET)
    respuesta_2 = respuesta_2.lower()
  if respuesta_2 == "a":
    punto = random.randint(-10,0)
    lista_puntos.append(punto)
    puntaje += punto
    print("\nIncorrecto!", nombre, "\nMiguel Angel pintó la creación de Adán")
    print("\nPerdistes",punto,"puntos")
    print("Puntaje actual: ",puntaje,)
  elif respuesta_2 == "c":
    punto = random.randint(-10,0)
    lista_puntos.append(punto)
    puntaje += punto
    print("\nIncorrecto!", nombre, "\nPablo Rubens pinto el juicio de Paris")
    print("\nPerdistes",punto,"puntos")
    print("Puntaje actual: ",puntaje,)
  elif respuesta_2 == "d":
    punto = random.randint(-10,0)
    lista_puntos.append(punto)
    puntaje += punto
    print("\nIncorrecto!", nombre, "\nDonatello hizo el Festín de Herodes en un relieve en bronce")
    print("\nPerdistes",punto,"puntos")
    print("Puntaje actual: ",puntaje,)
  elif respuesta_2 == "x":
    punto = random.randint(10, 100)
    lista_puntos.append(punto)
    puntaje += punto
    print("\nEncontrastes el mensaje secreto!!\nEl hombre de vitruvio fue dibujado por Leonardo Da Vinci")
    print("\nGanastes",punto,"puntos!!")
    print("Puntaje actual: ",puntaje,)
  else:
    punto = random.randint(0, 10)
    lista_puntos.append(punto)
    puntaje += punto
    print("\nMuy bien", nombre, "!")
    print("\nGanastes",punto,"puntos")
    print("Puntaje actual: ",puntaje,)
  time.sleep(2)
  #Pregunta3
  print(YELLOW+"\n3. ¿Qué famoso filósofo fue maestro de Alejandro Magno durante cinco años?"+RESET)
  print('''
a. Sócrates
b. Aristóteles
c. Platón
d. René Descartes\n''')
  time.sleep(2)
  respuesta_3 = input(BLUE+"Tu respuesta: "+RESET) 
  respuesta_3 = respuesta_3.lower()
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input(GREEN+"\nDebes responder 'a', 'b', 'c' o 'd'. \nIngresa nuevamente tu respuesta: "+RESET)
    respuesta_3 = respuesta_3.lower()
  if respuesta_3 == "a":
    puntaje += 5
    lista_puntos.append(5)
    print("\n...No es correcto", nombre,"\nPero.. te daré unos puntos\n")
    print("Obtuviste 5 puntos")
    print("Puntaje actual: ",puntaje,)
  elif respuesta_3 == "c":
    puntaje -= 5
    lista_puntos.append(-5)
    print("\nIncorrecto!...", nombre)
    print("\nPerdistes -5 puntos")
    print("Puntaje actual: ",puntaje,)
  elif respuesta_3 == "d":
    if puntaje <= 0:
      puntaje *= 2
      lista_puntos.append("Puntaje * 2")
    else: 
      puntaje /=2
      lista_puntos.append("Puntaje / 2")
    print("\nTotalmente incorrecto!...", nombre)
    print("")
    print("Puntaje actual: ",puntaje,)
  else:
    if puntaje <= 0:
      puntaje /=2
      lista_puntos.append("Puntaje / 2")
    else:
      puntaje *= 2
      lista_puntos.append("Puntaje * 2")
    print("\nCorrecto!", nombre)
    print("Lo hiciste bien!")
    print("\nPuntaje actual: ",puntaje,)
  time.sleep(2)
  print(YELLOW+"\n4. ¿Quién fue el último zar de Rusia?"+RESET)
  print('''
a. Nicolas II
b. Predo I el Grande
c. Alejandro II
d. Pablo I''')
  time.sleep(2)
  respuesta_4 = input(BLUE+"\nTu respuesta: "+RESET) 
  respuesta_4 = respuesta_4.lower()
  while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input(GREEN+"\nDebes responder 'a', 'b', 'c' o 'd'. \nIngresa nuevamente tu respuesta: "+RESET)
    respuesta_4 = respuesta_4.lower()
  if respuesta_4 == "a":
    punto = random.randint(0, 10)
    lista_puntos.append(punto)
    puntaje += punto
    print("\nCorrecto", nombre, "!")
    print("\nGanastes",punto,"puntos")
    print("Puntaje actual: ",puntaje)
  else:
    punto = random.randint(-10,0)
    lista_puntos.append(punto)
    puntaje += punto
    print("\nIncorrecto", nombre, "!")
    print("\nPerdistes",punto,"puntos")
    print("Puntaje actual: ",puntaje)
  time.sleep(2)
  print(MAGENTA+"\033[1m"+"\nLista de puntajes obtenidos por pregunta"+"\033[0m"+RESET)
  time.sleep(2)
  print("\nIntento: ", intentos,"\n")
  time.sleep(2)
  lista_pregunta = ["Pregunta 1","Pregunta 2","Pregunta 3","Pregunta 4"]
  print(MAGENTA+"▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
  print("█ "+"\t"+"\t"+"\t"+"\t"+"█"+"\t"+"\t"+"\t"+"  █ ")
  if (lista_puntos[0] <= -10):
    print("█ ",lista_pregunta[0],"  █    "+RESET,lista_puntos[0],MAGENTA+"    █ ")
    # El negativo de dos digitos
  elif (lista_puntos[0] < 0):
    print("█ ",lista_pregunta[0],"  █    "+RESET,lista_puntos[0],MAGENTA+"     █ ")
    # El negativo de un digito
  elif (lista_puntos[0]==0):
    print("█ ",lista_pregunta[0],"  █     "+RESET,lista_puntos[0],MAGENTA+"     █ ")
    # Si es igual a cero 
  elif (lista_puntos[0]>=10):
    print("█ ",lista_pregunta[0],"  █    "+RESET,lista_puntos[0],MAGENTA+"     █ ")
    #El positivo de dos digitos
  else:
    print("█ ",lista_pregunta[0],"  █     "+RESET,lista_puntos[0],MAGENTA+"     █ ")
    #El positivo de un digito
  print("█ "+"\t"+"\t"+"\t"+"\t"+"█"+"\t"+"\t"+"\t"+"  █ ")
  print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
  time.sleep(2)
  print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
  print("█ "+"\t"+"\t"+"\t"+"\t"+"█"+"\t"+"\t"+"\t"+"  █ ")
  if (lista_puntos[1] <= -10):
    print("█ ",lista_pregunta[1],"  █    "+RESET,lista_puntos[1],MAGENTA+"    █ ")
    # El negativo de dos digitos
  elif (lista_puntos[1] < 0):
    print("█ ",lista_pregunta[1],"  █    "+RESET,lista_puntos[1],MAGENTA+"     █ ")
    # El negativo de un digito 
  elif (lista_puntos[1] == 0):
    print("█ ",lista_pregunta[1],"  █      "+RESET,lista_puntos[1],MAGENTA+"    █ ")
    # Si es cero 
  elif(lista_puntos[1]>=100):
    print("█ ",lista_pregunta[1],"  █    "+RESET,lista_puntos[1],MAGENTA+"    █ ")
    #El positivo de tres digitos
  elif(lista_puntos[1]>=10):
    print("█ ",lista_pregunta[1],"  █    "+RESET,lista_puntos[1],MAGENTA+"     █ ")
    #El positivo de dos digitos
  else:
    print("█ ",lista_pregunta[1],"  █     "+RESET,lista_puntos[1],MAGENTA+"     █ ")
    #El positivo de un digito 
  print("█ "+"\t"+"\t"+"\t"+"\t"+"█"+"\t"+"\t"+"\t"+"  █ ")
  print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
  time.sleep(2)
  print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
  print("█ "+"\t"+"\t"+"\t"+"\t"+"█"+"\t"+"\t"+"\t"+"  █ ")
  if (lista_puntos[2] == "Puntaje / 2"):
    print("█ ",lista_pregunta[2],"  █"+RESET,lista_puntos[2],MAGENTA+"█ ")
    # Las palabras
  elif (lista_puntos[2] == "Puntaje * 2"):
    print("█ ",lista_pregunta[2],"  █"+RESET,lista_puntos[2],MAGENTA+"█ ")
    # Las palabras
  elif (lista_puntos[2] < 0):
    print("█ ",lista_pregunta[2],"  █    "+RESET,lista_puntos[2],MAGENTA+"     █ ")
    #El negativo 
  else:
    print("█ ",lista_pregunta[2],"  █     "+RESET,lista_puntos[2],MAGENTA+"     █ ")
    #El positivo 
  print("█ "+"\t"+"\t"+"\t"+"\t"+"█"+"\t"+"\t"+"\t"+"  █ ")
  print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
  time.sleep(2)
  print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
  print("█ "+"\t"+"\t"+"\t"+"\t"+"█"+"\t"+"\t"+"\t"+"  █ ")
  if (lista_puntos[3] <= -10):
    print("█ ",lista_pregunta[3],"  █    "+RESET,lista_puntos[3],+MAGENTA+"    █ ")
    # El negativo de dos digitos
  elif (lista_puntos[3] < 0):
    print("█ ",lista_pregunta[3],"  █    "+RESET,lista_puntos[3],MAGENTA+"     █ ")
    # El negativo de un digito
  elif (lista_puntos[3]==0):
    print("█ ",lista_pregunta[3],"  █     "+RESET,lista_puntos[3],MAGENTA+"     █ ")
    # Si es igual a cero
  elif (lista_puntos[3]>=10):
    print("█ ",lista_pregunta[3],"  █    "+RESET,lista_puntos[3],MAGENTA+"     █ ")
    # El positivo de dos digito 
  else:
    print("█ ",lista_pregunta[3],"  █      "+RESET,lista_puntos[3],MAGENTA+"    █ ")
    # El positivo de un digito
  print("█ "+"\t"+"\t"+"\t"+"\t"+"█"+"\t"+"\t"+"\t"+"  █ ")
  print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
  time.sleep(2)
  print (YELLOW+"\nGracias por jugar mi trivia!", nombre,"!")
  print("\nAlcanzaste", puntaje, "puntos"+RESET)
  time.sleep(2)
  print("\n¿Deseas intentar la trivia nuevamente?")
  time.sleep(2)
  repetir_trivia = input("\nIngresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":  
    print("\nEspero",nombre, "que lo hayas pasado bien, hasta pronto!") 
    iniciar_trivia = False
  else:
    print(CYAN+"\033[1m\n...:::¡Hola de nuevo",nombre+"!:::...\033[0m"+RESET)
    puntaje = random.randint(0, 10)
    print("\nEsta vez comenzarás con",puntaje,"puntos")