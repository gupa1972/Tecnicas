#se ponen las 3 notas de los alumnos
n1= float(input("Ingrese primera nota: ")) 
n2= float(input("Ingrese segunda nota: ")) 
n3= float(input("Ingrese tercera nota: ")) 

prom=(n1+n2+n3)/3

if prom<=7:
    print("promociona")
elif prom<=3:
    print("recursa")
else :
    print("Va a examen final")
