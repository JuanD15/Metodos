# Importacion de librerias necesarias
import math as mat
from sympy.parsing.sympy_parser import parse_expr
from sympy import lambdify

# Variables necesarias
entrada_usuario = input("Ingrese la funcion iterativa: ")
fx = lambdify(x, parse_expr(entrada_usuario)) #(2*(x)**3 -11.7*(x)**2 -5)/-17.7
X0 = float(input("Ingrese el X0 para la funcion: "))
rond = int(input("Ingrese las cifras deseadas: "))
ErrStop = float(input("Ingrese el error que quiere usar como limite: "))

#Metodo para carlcular el error relativo
def ErrRel(Vante, Vactual):
    return round(abs((Vante - Vactual)/Vactual)*100, 2)

#Metodo para calcular el error aproximado
def ErrAprox(Vante, Vactual):
    return round(abs(Vante - Vactual)*100, 2)
#----------------------------------------------------------------
#Calculo con limite de error
def LimiErr(X0, ErrStop):
    ErrApr = 100
    i = 0
    #Fila inicial
    result = "||  i   ||   Xi   ||  Xi+1  ||   ErrAprox%   ||   ErrRel%   ||\n"
    result += "--------------------------------------------------------------\n"
    while(ErrApr > ErrStop):
        X1 = round(fx(X0), rond)
        ErrApr = ErrAprox(X0, X1)
        ErrRela = ErrRel(X0, X1)
        result += f"||  {i}  ||  {X0}  ||  {X1}  ||  {ErrApr}%  ||  {ErrRela}%  ||\n"
        X0 = X1
        i += 1
    return result
#----------------------------------------------------------------
print(LimiErr(X0, ErrStop))