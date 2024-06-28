from sympy.parsing.sympy_parser import parse_expr
import sympy as sp

#Variables necesarias
x = sp.symbols('x')
inp = input("Ingrese la funcion iterativa: ")
funcion = parse_expr(inp)
#2*(x)**3 -11.7*(x)**2 +17.7*(x) -5
derivada = sp.diff(funcion, x)
X0 = float(input("Ingrese el X0 para la funcion: "))
rond = int(input("Ingrese las cifras deseadas: "))
ErrStop = float(input("Ingrese el error que quiere usar como limite: "))

#Metodo para carlcular el error relativo
def ErrRel(Vante, Vactual):
    return round(abs((Vante - Vactual)/Vactual)*100, 2)

#Metodo para calcular el error aproximado
def ErrAprox(Vante, Vactual):
    return round(abs(Vante - Vactual)*100, 2)

#Calculo limite de error Newton - Raphson
def NewtonRaphson(X0, ErrStop):
    ErrApr = 100
    i = 0
    #Fila Inicial
    result = "||  i   ||   Xi   ||  Xi+1  ||   ErrAprox%   ||   ErrRel%   ||\n"
    result += "--------------------------------------------------------------\n"
    while(ErrApr > ErrStop):
        fXi = round(funcion.subs(x, X0), rond)
        gXi = round(derivada.subs(x, X0), rond)
        X1 = round(X0 - (fXi / gXi), rond)
        ErrApr = ErrAprox(X0, X1)
        ErrRela = ErrRel(X0, X1)
        result += f"||  {i}  ||  {X0}  ||  {X1}  ||  {ErrApr}%  ||  {ErrRela}%  ||\n"
        X0 = X1
        i += 1
    return result
print(NewtonRaphson(X0, ErrStop))