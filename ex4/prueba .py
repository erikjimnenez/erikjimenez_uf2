
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

separador(4.6)

 
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

