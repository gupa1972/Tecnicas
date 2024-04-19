Nombre= input("Ingrese su Nombre: ")
Peso=float(input("Ingresa su Peso: "))
Altura=float(input("Ingresa su Altura: "))
Indice=((Peso)/((Altura)*(Altura)))
if Indice<20:
    print("El IPC es " , Indice,  " Poca Nutricion")
elif Indice>25:
     print("El IPC es " , Indice,  " Va para Obeso")
else :
     print("El IPC es " ,Indice,  " Peso Normal")