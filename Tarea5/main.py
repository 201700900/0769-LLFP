import re

letra = "[a-z]"
guion = "_"
numero = "[0-9]"

def adf(entrada):
    estado=0
    caracter = list(entrada)
    for x in caracter:
        
        if estado==0:
            
            if re.match(guion, x):
                estado = 1
            elif re.match(letra, x):
                estado = 2    
            else:
                print("Error! ", entrada,"no es valido")
                break  
        elif estado==1:
            if re.match(guion, x):
                estado = 1
            elif re.match(letra, x):
                estado = 3    
            else:
                print("Error! ", entrada,"no es valido")
                break
        elif estado==2:
            if re.match(letra, x):
                estado = 2
            elif re.match(numero, x):
                estado = 4    
            else:
                print("Error! ", entrada,"no es valido")
                break
        elif estado==3:
            if re.match(letra, x):
                estado = 3
            elif re.match(numero, x):
                estado = 4    
            else:
                print("Error! ", entrada,"no es valido") 
                break
    
    
    if estado==4:
        print("************************")
        print(entrada + " sí es válida")   
        print("************************")     
        
adf("__servidor1")
print("--------------")
adf("3servidor")            