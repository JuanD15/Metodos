# Importacion de librerias necesarias
import math as mat

# Variables necesarias
init = True
X0 = 2.000
imax = 20
ErrStop = 0.001
gx = lambda x: mat.sqrt((x + 5) / 2)

#Metodo para carlcular el error relativo
def ErrRel(Vante, Vactual):
    return round(abs(Vactual - Vante)/Vante,3)

#Metodo para calcular el error aproximado
def ErrAprox(Vante, Vactual):
    return round(abs(Vactual - Vante),3)
#----------------------------------------------------------------
#Calculo con limite de error
def LimiErr(X0, ErrStop):
    ErrApr =100
    i = 0
    #Fila inicial
    result = "||  i   ||   Xi   ||   ErrAprox%   ||   ErrRel%   ||\n"
    result += "------------------------------------------------------\n"
    while(ErrApr > ErrStop):
        X1 = round(gx(X0),3)
        ErrApr = ErrAprox(X0, X1)
        ErrRela = ErrRel(X0, X1)
        result += f"||  {i}  ||  {X0}  ||  {ErrApr}  ||  {ErrRela}  ||\n"
        X0 = X1
        i+=1
    return result
#----------------------------------------------------------------
#Calculo con Limite de iteraciones
def LimitIteracion(X0, imax):
    #Fila inicial
    result = "||  i   ||   Xi   ||   ErrAprox%   ||   ErrRel%   ||\n"
    result += "------------------------------------------------------\n"
    for i in range(0, imax):
        X1 = round(gx(X0),3)
        ErrApr = ErrAprox(X0, X1)
        ErrRela = ErrRel(X0, X1)
        result += f"||  {i}  ||  {X0}  ||  {ErrApr}  ||  {ErrRela}  ||\n"
        X0 = X1
    return result

#Menu inicial
while(init):
    option = float(input("Ingrese 1 si quiere usar limite por error\nIngrese 0 si quiere usar limite por iteraciones:\n"))
    if(option==1):
        X0 = float(input("Ingrese el X0 para la funcion: "))
        ErrStop = float(input("Ingrese el error que quiere usar como limite: "))
        print(LimiErr(X0, ErrStop))
        init = False
    elif(option==0):
        X0 = float(input("Ingrese el X0 para la funcion: "))
        imax = int(input("Ingrese el numero maximo de iteraciones"))
        print(LimitIteracion(X0, imax))
        init = False