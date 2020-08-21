from xml.dom import minidom

def imprimirXML(): 
    doc = minidom.parse("registro.xml")

    nombre = doc.getElementsByTagName("nombre")[0]

    print(nombre.firstChild.data)
    empleados = doc.getElementsByTagName("empleado")
    print("---------TIPO----------------------")
    print(type(empleados))
    print("--------------------------------")
    for empleado in empleados:
        sid = empleado.getAttribute("id")
        username = empleado.getElementsByTagName("username")[0]
        password = empleado.getElementsByTagName("password")[0]
        carnet = empleado.getElementsByTagName("carnet")[0]
        print("id:%s " % sid)
        print("username:%s" % username.firstChild.data)
        print("password:%s" % password.firstChild.data)
        print("carnet:%s" % carnet.firstChild.data +"\n")