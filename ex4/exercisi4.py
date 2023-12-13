print("Erik Jimenez")

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador(4.1) 


ingreso = float(input("Ingresa la cantidat de tu ingreso: "))


exencion_fiscal = 556.02


if ingreso <= 85528: impuesto = round(0.18 * ingreso - exencion_fiscal)
else: impuesto = round(14839.02 + 0.32 * (ingreso - 85528))


impuesto = max(0, impuesto)


print("El impuesto calculado es:", impuesto, "pesos")


def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador(4.2) 

año = int(input("ingresa un  año "))

if año < 1582:
      print("No esta dentro del periodo del calendario Gregoriano.")
else: 
     if (año % 4!= 0) or ((año % 100 == 0) and (año % 400 !=0)):
        print("Año comun")
     else:
         print("Año bisiesto")   

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

separador(4.3)

secret_number = 33

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

adivinanza = int(input("Coloque un numero pra adivinar el numeo secreto"))

while adivinanza != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    adivinanza = int(input("Inténtalo de nuevo: "))

    print("¡Bien hecho, muggle! Eres libre ahora.")

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

separador(4.4)


numero = int(input("Ingresa un número entero: "))


if numero % 2 == 0:
    print("El número", numero, "es par.")
else:
    print("El número", numero, "es impar.")

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

separador(4.5)

edat = int(input("Ingresa tu edat"))
ingresos = float (input("ingrese su sueldo mensual"))

if edat > 16 and ingresos >= 1000:
    print("Si puedes tributar")

else: 
    print("no puedes tributar")

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

separador(4.6)
nom = str(input("Pon tu nombre: "))

sexo = str(input("Escribe tu sexo(La H para hombre i la M para mujer): "))


if (sexo == 'M' and nom < 'M') or (sexo == 'H' and nom > 'N'):
    Grupo = 'A'
else:
    Grupo = 'B'

print (f"Tu perteneces al grupo {Grupo}.")


def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

separador(4.7)

renta_anual = int(input("Indique tu renta anual:"))
if renta_anual < 10000:
    print("5%")
elif  10000 < renta_anual < 20000:
    print("15%")
elif  20000 < renta_anual < 35000:
    print("20%")
elif 35000 < renta_anual < 60000:
    print("30%")
else:
    print("45%")


def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

separador(4.8)

# Función para determinar el nivel de rendimiento y calcular el dinero recibido
def evaluar_rendimiento(puntuacion):
    if puntuacion == 0.0:
        nivel = "Inaceptable"
    elif puntuacion == 0.4:
        nivel = "Aceptable"
    elif puntuacion >= 0.6:
        nivel = "Meritorio"
    else:
        nivel = "Puntuación no válida"

    dinero_recibido = 2400 * puntuacion
    return nivel, dinero_recibido

# Pedir la puntuación al usuario
try:
    puntuacion = float(input("Ingrese la puntuación del empleado (0.0, 0.4, 0.6 o más): "))
    if puntuacion == 0.0 or puntuacion == 0.4 or puntuacion >= 0.6:
        nivel, dinero_recibido = evaluar_rendimiento(puntuacion)
        print(f"Nivel de rendimiento: {nivel}")
        print(f"Cantidad de dinero recibida: {dinero_recibido}€")
    else:
        print("Puntuación no válida. Por favor, ingrese 0.0, 0.4, o 0.6 o más.")
except ValueError:
    print("Error: Ingrese un valor numérico válido.")

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

separador(4.9)

# Pedir la edad al usuario
try:
    edad = int(input("Ingrese la edad del cliente: "))

    # Calcular el precio de entrada según la edad
    if edad < 4:
        precio_entrada = 0
    elif 4 <= edad <= 18:
        precio_entrada = 5
    else:
        precio_entrada = 10

    # Mostrar el precio de entrada al usuario
    print(f"El precio de entrada es: {precio_entrada}€")
except ValueError:
    print("Error: Ingrese una edad válida (número entero).")

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

separador(4.10)

# Preguntar al usuario si quiere una pizza vegetariana o no
tipo_pizza = input("¿Desea una pizza vegetariana? (sí/no): ").lower()

# Definir ingredientes disponibles
ingredientes_vegetarianos = ["pimiento", "tofu"]
ingredientes_no_vegetarianos = ["peperoni", "jamón", "salmón"]

# Mostrar menú de ingredientes según la elección del usuario
if tipo_pizza == "sí":
    print("Ingredientes vegetarianos disponibles:")
    print("1. Pimiento")
    print("2. Tofu")
else:
    print("Ingredientes no vegetarianos disponibles:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")

# Pedir al usuario que elija un ingrediente
try:
    opcion_ingrediente = int(input("Elija un ingrediente (1, 2, 3): "))
    
    # Validar la elección del usuario y mostrar los ingredientes de la pizza
    if tipo_pizza == "sí" and 1 <= opcion_ingrediente <= 2:
        pizza = "Vegetariana"
        ingrediente_elegido = ingredientes_vegetarianos[opcion_ingrediente - 1]
    elif tipo_pizza == "no" and 1 <= opcion_ingrediente <= 3:
        pizza = "No Vegetariana"
        ingrediente_elegido = ingredientes_no_vegetarianos[opcion_ingrediente - 1]
    else:
        pizza = "Desconocida"
        ingrediente_elegido = "Desconocido"

    # Mostrar la información de la pizza elegida
    print(f"\n¡Ha elegido una pizza {pizza} con los siguientes ingredientes:")
    print("- Mozzarella")
    print("- Tomate")
    print(f"- {ingrediente_elegido}")

except ValueError:
    print("Error: Por favor, ingrese un número válido.")

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

separador(4.11)

import ipaddress

def validar_ip(ip):
    try:
        octetos = map(int, ip.split(b'.'))
        return len(octetos) == 4 and all(0 <= octeto <= 255 for octeto in octetos)
    except ValueError:
        return False

def determinar_clase_ip(ip):
    primer_octeto = int(ip.split(b'.')[0])
    if 1 <= primer_octeto <= 126:
        return 'A'
    elif 128 <= primer_octeto <= 191:
        return 'B'
    elif 192 <= primer_octeto <= 223:
        return 'C'
    elif 224 <= primer_octeto <= 239:
        return 'D (Multicast)'
    elif 240 <= primer_octeto <= 255:
        return 'E (Reservada)'
    return 'Desconocida'

def determinar_tipo_ip(ip):
    privadas = [ipaddress.IPv4Network(b'10.0.0.0/8'), ipaddress.IPv4Network(b'172.16.0.0/12'), ipaddress.IPv4Network(b'192.168.0.0/16')]
    return 'Privada' if any(ipaddress.IPv4Address(ip) in red for red in privadas) else 'Pública'

while True:
  
    try:
        ip_usuario = input("Ingrese una dirección IP en formato byte (ejemplo: b'192.168.1.1'): ").encode('utf-8')
    except UnicodeDecodeError:
        print("Error: La entrada no es un formato de byte válido.")
        continue

   
    if validar_ip(ip_usuario):
        clase_ip = determinar_clase_ip(ip_usuario)
        tipo_ip = determinar_tipo_ip(ip_usuario)
        print(f"La dirección IP {ip_usuario.decode('utf-8')} es de Clase {clase_ip} y es {tipo_ip}.")
        break
    else:
        print("La dirección IP ingresada no es válida.")

