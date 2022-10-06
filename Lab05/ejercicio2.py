
try:
    namefile = input("Ingrese el nombre del archivo\n>>>")
    file1 = open(namefile, "r", encoding="UTF-8")

    for linea in file1:
        print(linea.upper())
except:
    print("Ingrese un archivo existente")