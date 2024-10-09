print ("gerencia")
name = input("Tú nommbre es: ")
lastname = input ("Tú apellido es: ")
clave = int(input("La  clave es: "))
antiguedad = float(input("Tú año de antiguedad:  "))
    
if clave == 1:
    if antiguedad == 1 and antiguedad <2:
        print("El/La trabajador(a)",name,lastname,"merece 6 dias de vacaciones")
    elif antiguedad >= 2 and antiguedad <=6:
        print("El/La trabajador(a)",name,lastname,"merece 14 dias de vacaciones")
    elif antiguedad >= 7:
        print("El/La trabajador(a)",name,lastname,"merece 20 dias de vacaciones")
    else:
        print("Sin derecho a vacaciones")
if clave == 2:
    
    if antiguedad ==1 and  antiguedad <2:
        print("El/La trabajador(a)",name,lastname,"merece 7 dias de vacaciones")
    elif antiguedad >=2 and antiguedad <=6:
        print("El/La trabajador(a)",name,lastname,  "merece 15 dias de vacaciones")
    elif antiguedad  >= 7:
        print("El/La trabajador(a)",name,lastname, "merece 22 dias de vacaciones")
    else:
        print("Sin derecho a vacaciones")

if clave == 3:
    if antiguedad ==1 and antiguedad <2:
        print("El/La trabajador(a)",name,lastname, "merece 10 dias de vacaciones")
    elif antiguedad >=2 and antiguedad <=6:
        print("El/La trabajador(a)",name,lastname, "merece 20 dias de vacaciones")
    elif antiguedad >= 7:
        print("El/La trabajador(a)",name,lastname, "merece 30 dias de vacaciones")
    else:
        print("Sin derecho a vacaciones")
