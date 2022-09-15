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
  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar\n")
  for numero_carga in range (5,0,-1):
    print(numero_carga)
    time.sleep(1)      
  #Pregunta 1
  print("\n1. ¿De qué nacionalidad era Juana de Arco?")
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
    puntaje += punto
    print("\nCorrecto", nombre, "!")
    print("\nGanastes",punto,"puntos")
    print("Puntaje actual: ",puntaje)
  else:
    punto = random.randint(0, 10)
    puntaje -= punto
    print("\nIncorrecto", nombre, "!")
    print("\nPerdistes",punto,"puntos")
    print("Puntaje actual: ",puntaje)
  time.sleep(2)
  #Pregunta 2
  print('''\n2. ¿Quién dibujo al famoso Hombre de Vitruvio?\n
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
    punto = random.randint(0, 10)
    puntaje -= punto
    print("\nIncorrecto!", nombre, "\nMiguel Angel pintó la creación de Adán")
    print("\nPerdistes",punto,"puntos")
    print("Puntaje actual: ",puntaje,)
  elif respuesta_2 == "c":
    punto = random.randint(0, 10)
    puntaje -= punto
    print("\nIncorrecto!", nombre, "\nPablo Rubens pinto el juicio de Paris")
    print("\nPerdistes",punto,"puntos")
    print("Puntaje actual: ",puntaje,)
  elif respuesta_2 == "d":
    punto = random.randint(0, 10)
    puntaje -= punto
    print("\nIncorrecto!", nombre, "\nDonatello hizo el Festín de Herodes en un relieve en bronce")
    print("\nPerdistes",punto,"puntos")
    print("Puntaje actual: ",puntaje,)
  elif respuesta_2 == "x":
    punto = random.randint(10, 100)
    puntaje += punto
    print("\nEncontrastes el mensaje secreto!!\nEl hombre de vitruvio fue dibujado por Leonardo Da Vinci")
    print("\nGanastes",punto,"puntos!!")
    print("Puntaje actual: ",puntaje,)
  else:
    punto = random.randint(0, 10)
    puntaje += punto
    print("\nMuy bien", nombre, "!")
    print("\nGanastes",punto,"puntos")
    print("Puntaje actual: ",puntaje,)
  time.sleep(2)
  #Pregunta3
  print('''\n3. ¿Qué famoso filósofo fue maestro de Alejandro Magno durante cinco años?\n
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
    print("\n...No es correcto", nombre,"\nPero.. te daré unos puntos")
    print("\n"+punto,"puntos")
    print("Puntaje actual: ",puntaje,)
  elif respuesta_3 == "c":
    puntaje -= 5
    print("\nIncorrecto!...", nombre)
    print("\nPerdistes",punto,"puntos")
    print("Puntaje actual: ",puntaje,)
  elif respuesta_3 == "d":
    puntaje /= 2
    print("\nTotalmente incorrecto!...", nombre)
    print("\nSe te dividirán tus puntos")
    print("Puntaje actual: ",puntaje,)
  else:
    puntaje *= 2
    print("\nCorrecto!", nombre)
    print("Lo hiciste bien! Se multiplicará tu puntaje!")
    print("\nPuntaje actual: ",puntaje,)
  time.sleep(2)
  print("\n4. ¿Quién fue el último zar de Rusia?")
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
    puntaje += punto
    print("\nCorrecto", nombre, "!")
    print("\nGanastes",punto,"puntos")
    print("Puntaje actual: ",puntaje)
  else:
    punto = random.randint(0, 10)
    puntaje -= punto
    print("\nIncorrecto", nombre, "!")
    print("\nPerdistes",punto,"puntos")
    print("Puntaje actual: ",puntaje)
  time.sleep(2)
  print (YELLOW+"\nGracias por jugar mi trivia ", nombre, ", \nalcanzaste", puntaje, "puntos"+RESET)
  time.sleep(2)
  print("\n¿Deseas intentar la trivia nuevamente?")
  time.sleep(2)
  repetir_trivia = input("\nIngresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":  
    print("\nEspero",nombre, "que lo hayas pasado bien, hasta pronto!") 
    iniciar_trivia = False
  else:
    print(CYAN+"\033[1m\n¡Hola de nuevo",nombre+"!\033[0m"+RESET)