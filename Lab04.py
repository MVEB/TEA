def calcula_calificacion(notas):
 if notas >= 0 and notas <= 1:
    if notas >= 0.9:
        calificacion = print("Sobresaliente")
    elif notas == 1.0:
        calificacion = print("Sobresaliente")
    elif notas >=0.8 and notas <=9:
        calificacion = print("Notable")
    elif notas >=0.7 and notas <=8:
        calificacion = print("Bien")
    elif notas >=0.6 and notas <=7:
        calificacion = print("Suficiente")
    elif notas <=0.6:
        calificacion = print("Insuficiente")
    else:
        print("error")
    return calificacion
try:
 notas = float(input("Ingrese la calificacion : "))
 calcula_calificacion(notas)
except:
 print("Error ")