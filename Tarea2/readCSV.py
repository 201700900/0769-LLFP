import csv

def imprimirCSV():
    with open('registro.csv') as f:
        reader = csv.reader(f)
        print(reader)
        for row in reader:
            print("Nombre: {0}\n Nickname: {1}\n Rol: {2}\n Telefono {3}\n ".format(row[0], row[1], row[2], row[3]))