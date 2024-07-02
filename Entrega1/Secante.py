from sympy.parsing.sympy_parser import parse_expr
import sympy as sp

x = sp.symbols('x')
inp = input("Ingrese la funcion iterativa: ")
funcion = parse_expr(inp)
X0 = float(input("Ingrese el Xi-1 para la funcion: "))
X1 = float(input("Ingrese el Xi para la funcion: "))
rond = int(input("Ingrese las cifras deseadas: "))
ErrStop = float(input("Ingrese el error aproximado que quiere usar como limite: "))

#Metodo para carlcular el error relativo
def ErrRel(Vante, Vactual):
    return round(abs((Vante - Vactual)/Vactual)*100, 2)

#Metodo para calcular el error aproximado
def ErrAprox(Vante, Vactual):
    return round(abs(Vante - Vactual)*100, 2)

#
def Secante(X0, X1, ErrStop):
    ErrApr = 100
    i = 0
    #Fila Inicial
    result = "||  i   ||   Xi-1   ||  Xi  ||  Xi+1  ||   ErrAprox%   ||   ErrRel%   ||\n"
    result += "------------------------------------------------------------------------\n"
    while(ErrApr > ErrStop):
        fX0 = round(funcion.subs(x, X0), rond)
        fX1 = round(funcion.subs(x, X1), rond)
        X2 = round(X1 - fX1 *((X1-X0)/(fX1-fX0)), rond)
        ErrApr = ErrAprox(X1, X2)
        ErrRela = ErrRel(X1, X2)
        result += f"||  {i}  ||  {X0}  ||  {X1}  ||  {X2}  ||  {ErrApr}%  ||  {ErrRela}%  ||\n"
        X0 = X1
        X1 = X2
        i += 1
    return result
try:
    print(Secante(X0, X1, ErrStop))
except Exception as e:
    print("La operacion no se pudo realizar")