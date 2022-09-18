import random
import time
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[39m'

puntaje = random.randint(0,10)
iniciar_trivia = True
intentos = 0
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print(RED+"=== Bienvenido a mi trivia sobre Python ==="+RESET)
print("Pondremos a prueba tus conocimientos")
print ("\nRecuerda que por cada buena son", GREEN+"+10"+RESET,"puntos y por cada mala", RED+"-5"+RESET,"puntos, si aciertas la respuesta secreta te llevas",YELLOW+"+50"+RESET,"puntos \n")
print ("Tienes", puntaje, "puntos")
# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable
while iniciar_trivia == True:
  intentos += 1
  nombre = input(YELLOW+"Ingresa tu nombre: " +RESET)
  
  # Es importante dar instrucciones sobre cómo jugar:
  print("\nHola", nombre,"responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
  
  # Temporizador
  for tiempo_inicio in range(5,0,-1):
    print(tiempo_inicio)
    time.sleep(1)
  
  
  # Pregunta 1
  print("\n1) ¿Quién fue el creador de Python?")
  print("a) Linus Torvalds")
  print("b) Bill Gates")
  print("c) Guido van Rossum")
  print("d) Dennis Ritchie")
  print ("\n Prueba con poner la primera letra del primer apellido del creador de python, veremos que pasa...")
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")
  
  while respuesta_1 not in ("a", "b", "c", "d","v"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_1 == "a":
    puntaje -= 5
    print("\n Incorrecto!", nombre, "Linus Torvalds es el desarrollador de Linux")
  elif respuesta_1 == "b":
    puntaje -= 5
    print("\n Incorrecto!", nombre, "Bill Gates es uno de los fundadores de Microsoft")
  elif respuesta_1 == "d":
    puntaje -= 5
    print("\n Incorrecto!", nombre, "Dennis Ritchie es el desarrollador del Lenguaje C")
  elif respuesta_1 == "v":
    puntaje += 50
    print(nombre, "\n Eres un crack, sabias la respuesta!")
  else:
    puntaje += 10
    print("Excelente", nombre,"!")
  
  print ("\n Genial", nombre, "mira que tan bueno eres bueno, hasta el momento alcanzaste", puntaje, "puntos, ¡sigue asi!")
  
  time.sleep(2)
  print ("Continuamos con la siguiente pregunta! ;)")
  
  # Pregunta 2
  print ("\n¿En qué área se usa python para análisis de datos?")
  print ("a) Data scientist")
  print ("b) Machine Learning")
  print ("c) Deep Learning")
  print ("d) Back End")
  print ("\n Extra: Y si pruebas con poner la abreviatura del Aprendizaje de Maquina, veremos que pasa...")
  respuesta_2 = input("\nTu respuesta: ")
  
  while respuesta_2 not in ("a", "b", "c", "d","ML"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_2 == "b":
    puntaje -= 5
    print("\n Incorrecto!", nombre, "Linus Torvalds es el desarrollador de Linux")
  elif respuesta_2 == "c":
    puntaje -= 5
    print("\n Incorrecto!", nombre, "Bill Gates es uno de los fundadores de Microsoft")
  elif respuesta_2 == "d":
    puntaje -= 5
    print("\n Incorrecto!", nombre, "Dennis Ritchie es el desarrollador del Lenguaje C")
  elif respuesta_2 == "ML":
    puntaje += 50
    print(nombre, "\n Eres un crack, sabias la respuesta!")
  else:
    puntaje += 10
    print("Excelente", nombre,"!")
  
  print ("\n Genial", nombre, "mira que tan bueno eres bueno, hasta el momento alcanzaste", puntaje, "puntos, ¡sigue asi!")
  
  time.sleep(5)
  print ("Continuamos con la siguiente pregunta! ;)")
  
  # Pregunta 3
  print ("\n¿Cual de las empresas usan python? Digita tu respuesta:\n")
  print ("a) Instagram")
  print ("b) Facebook")
  print ("c) Netflix")
  print ("d) Todas las anteriores")
  
  respuesta_3 = input("\nTu respuesta: ")
    
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_1 == "a":
    print("\n Incorrecto!", nombre, "Linus Torvalds es el desarrollador de Linux")
    puntaje = puntaje + 10
  elif respuesta_1 == "b":
    print("\n Incorrecto!", nombre, "Bill Gates es uno de los fundadores de Microsoft")
    puntaje = puntaje + 10
  elif respuesta_1 == "c":
    print("\n Incorrecto!", nombre, "Dennis Ritchie es el desarrollador del Lenguaje C")
    puntaje = puntaje + 10
  else:
    print("Excelente", nombre,"!")
    puntaje = puntaje * 2
  print ("\n Genial", nombre, "mira que tan bueno eres bueno, hasta el momento alcanzaste", puntaje, "puntos, ¡sigue asi!")

  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero",nombre,"que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.