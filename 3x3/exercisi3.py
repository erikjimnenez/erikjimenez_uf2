print("Erik Jimenez")

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador(3.1) 
# Pedir al usuario que introduzca su nombre
nombre = input("Por favor, introduce tu nombre: ")

# Mostrar el saludo con el nombre introducido
print(f"¡Hola \"{nombre}\"!")

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador(3.2) 
# El var es para saber que es una variable
Juan = 3
Maria = 5
Adán = 6

print(Juan, Maria, Adán)

Totaldemanzanas = Juan + Maria + Adán
print(Totaldemanzanas)
# Experimenta con tu código
Erik = 5
Nelson = 2
Yosue = 8

print(Erik, Nelson, Yosue)

Skins = Erik * Nelson / Yosue
print(Skins)

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador(3.3) 
kilometras = 1.61
milla = 1
# Conversión de millas a kilómetros
milla_to_kilometras = milla * 1.61

# Conversión de kilómetros a millas
kilometras_to_milla = kilometras / 1
# Impresión
print(milla, "millas son", round(milla_to_kilometras,2), "kilometras")
print(kilometras , "kilometras son", round(kilometras_to_milla,2), "milla")

# Solicitar al usuario los valores miles_to_kilometers y kilometers_to_miles
miles_to_kilometers = float(input("Ingresa la cantidad de millas a convertir a kilómetros: ")) ###
kilometers_to_miles = float(input("Ingresa la cantidad de kilómetros a convertir a millas: ")) ###

# Conversión de millas a kilómetros usando el valor proporcionado por el usuario
miles_to_kilometers_result = miles_to_kilometers * 1.61 ###

# Conversión de kilómetros a millas usando el valor proporcionado por el usuario
kilometers_to_miles_result = kilometers_to_miles / 1.61 ###

# Impresión de los resultados proporcionados por el usuario
print(miles_to_kilometers, "millas son", miles_to_kilometers_result, "kilómetros.")
print(kilometers_to_miles, "kilómetros son", kilometers_to_miles_result, "millas.")

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador(3.4)

# Lee un valor flotante
x = float(input("Ingresa un valor para x: "))

# Evalúa la expresión 3x^3 - 2x^2 + 3x - 1 y asigna el resultado a la variable y
y = 3 * x**3 - 2 * x**2 + 3 * x - 1

# Imprime el resultado
print("El resultado de la expresión 3x^3 - 2x^2 + 3x - 1 para x =", x, "es y =", y)




separador(3.5)

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
coste_por_hora = float(input("Ingrese el coste por hora: "))

# Calcular la paga multiplicando las horas trabajadas por el coste por hora
paga = horas_trabajadas * coste_por_hora

# Mostrar por pantalla la paga correspondiente
print("La paga correspondiente es:", paga)

separador(3.6)

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

# Solicitar un entero positivo y al usuario 
n = int(input("Ingrese un entero positivo: "))


if n <= 0:
    print("Por favor, ingrese un entero positivo.")
else:
    
    suma = 0

    # Calcular la suma de los enteros desde 1 hasta n
    for i in range(1, n + 1):
        suma += i

  
    print("La suma de los enteros desde 1 hasta", n, "es:", suma)


separador(3.7)

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))


imc = peso / (estatura ** 2)

imc = round(imc, 2)

# Mostrar el resultado en la consola
print(f"Tu índice de masa corporal es {imc}.")


separador(3.8)

# Solicitar al usuario la cantidad a invertir, el interés anual y el número de años
cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual en porcentaje: "))
num_anios = int(input("Ingrese el número de años de la inversión: "))

# Convertir el interés anual de porcentaje a decimal
interes_decimal = interes_anual / 100

# Calcular el capital obtenido en la inversión
capital_obtenido = cantidad_invertir * (1 + interes_decimal)**num_anios

# Mostrar el resultado en la consola
print(f"El capital obtenido después de {num_anios} años es: {capital_obtenido:.2f}")



def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)



separador(3.9)



# Solicitar  bytes de la IP
byte1 = input("Introduce el primer byte de la IP: ")
byte2 = input("Introduce el segundo byte de la IP: ")
byte3 = input("Introduce el tercer byte de la IP: ")
byte4 = input("Introduce el cuarto byte de la IP: ")

#  dirección IP en formato xxx.xxx.xxx.xxx
ip_address = f"{byte1}.{byte2}.{byte3}.{byte4}"

#  dirección IP
print("La dirección IP es:", ip_address)

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador(10.)

def calcular_tiempo_final(inicio_horas, inicio_minutos, duracion, dia):

    duracion_total_minutos = inicio_minutos + duracion

    
    horas_finales = (inicio_horas + duracion_total_minutos // 60) % 24
    minutos_finales = duracion_total_minutos % 60

    dia_final = dia + (inicio_horas + duracion_total_minutos // 60) // 24

    return horas_finales, minutos_finales, dia_final

# Solicitar la hora de inicio
inicio_horas = int(input("Introduce la hora de inicio (0 a 23): "))
#Solicitaremos el inicio de los minutos 
inicio_minutos = int(input("Introduce los minutos de inicio (0 a 59): "))
#solicitaremos la duracion del dia
duracion = int(input("Introduce la duración en minutos: "))
#ahora solicitaremos un dia entre el 1 al 30
dia = int(input("Introduce el día (1 a 30): "))

# tiempo final
horas_finales, minutos_finales, dia_final = calcular_tiempo_final(inicio_horas, inicio_minutos, duracion, dia)

#  resultado en la consola
print(f"El evento comenzando a las {inicio_horas:02d}:{inicio_minutos:02d} y durando {duracion} minutos, finalizará el día {dia_final}, a las {horas_finales:02d}:{minutos_finales:02d}.")

