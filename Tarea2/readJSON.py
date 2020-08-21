import json

def readJson():
    file = open('registro.json',)
    data =json.load(file)
    file.close()
    return data

def imprimirJSON():
    dict = readJson()
    print("-------TIPO---------------")
    print(dict)
    Print("-----------------------")
    for element in dict:
        print("nombre: " + element.get('nombre', ''))
        print("edad: " + str(element.get('edad', '')) )
        print("activo: " + str(element.get('activo', '')))
        print("promedio: " + str(element.get('promedio', ''))+ "\n")


