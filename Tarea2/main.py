import readCSV
import readJSON
import readXML


def pedirNumeroEntero():

    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')

    return num

salir = False
opcion = 0

while not salir:

    print("------------------------------------------------------------------------------------------")
    print("Elija el tipo de archivo que desea ver")
    print ("1. .JSON")
    print ("2. .XML")
    print ("3. .CSV")
    print ("4. Salir")
    print("~~~~~~")
    print ("Elige una opcion")
    opcion = pedirNumeroEntero()

    if opcion == 1:
        readJSON.imprimirJSON()
    elif opcion == 2:
        readXML.imprimirXML()
    elif opcion == 3:
        readCSV.imprimirCSV()
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")

print ("Fin")