print("Erik Jimenez")

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador(4.1) 

# mod 18:33
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
if renta_anual < 10000
:
    print("5%")
elif  10000 < renta_anual < 20000:
    print("15%")
elif  20000 < renta_anual < 35000:
    print("20%")
elif 35000 < renta_anual < 60000:
    print("30%")
else:
    print("45%")

