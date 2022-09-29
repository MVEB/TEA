maximo = 0
minimo = 0

while True:
 try:
    numero = input("Ingrese numero:")
    if (numero == "fin"):
        break
    else:
     if int(maximo) < int(numero):
        maximo = numero
     if int(minimo) > int(numero):
        minimo = numero
 except:
       print("ingrese numeros")
       
print("maximo:", maximo)
print("minimo:", minimo)