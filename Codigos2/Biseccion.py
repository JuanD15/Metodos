from tabulate import tabulate
import sympy as sp

#Variables necesarias
x = sp.symbols('x')
inp = input("Ingrese la funcion: ")
funcion = sp.parse_expr(inp)
#sp.lambdify(sp.parse_expr(inp))
#(667.38/x)*(1 -exp((-x/68.1)*10)) -40
Xinf = float(input("Ingrese el Xinf: "))
Xsup = float(input("Ingrese el Xsup: "))
rond = int(input("Ingrese las cifras deseadas: "))
ErrLimit = float(input("Ingrese el error limite: "))
verific = (funcion.subs(x, Xinf)*funcion.subs(x, Xsup))>0
headers = ["i", "Xinf", "Xsup", "Xr", "Eap", "f(Xinf)", "f(Xsup)", "f(Xr)"]
rows = []

while (verific):
    print("la raiz no se encuentra en el intervalo, intente con otros valores")
    Xinf = float(input("Ingrese el Xinf: "))
    Xsup = float(input("Ingrese el Xsup: "))
    verific = (funcion.subs(x, Xinf)*funcion.subs(x, Xsup))>0

#Metodo para calcular el error aproximado
def ErrAprox(Vante, Vactual):
    result = round(abs(Vante - Vactual), rond)
    if Vante == 0 or Vactual == 0:
        result = 1010101
    return result

#Verificacion de error aproxim
def VerErrAp(ErrAp):
    if ErrAp == 1010101:
        return'-'
    else: 
        return ErrAp

def Biseccion(Xinf, Xsup, ErrStop):
    data = []
    ErrAp = 1
    i = 0
    Xaux = 0
    while ErrAp > ErrLimit:
        Xr = (Xinf+Xsup)/2
        ErrAp = ErrAprox(Xaux, Xr)
        fXinf = round(funcion.subs(x, Xinf), rond)
        fXsup = round(funcion.subs(x, Xsup), rond)
        fXr = round(funcion.subs(x, Xr), rond)
        rows.append([i, Xinf,Xsup,Xr,VerErrAp(ErrAp), fXinf, fXsup, fXr])
        if(fXinf*fXr)<0:
            Xsup = Xr
            Xaux = Xr
            i += 1
        elif(fXinf*fXr)>0:
            Xinf = Xr
            Xaux = Xr
            i += 1
        else:
            print(f"La raiz es: {Xr}")
            break
try:
    Biseccion(Xinf, Xsup, ErrLimit)
    print(tabulate(rows, headers=headers, numalign='center', stralign='center',tablefmt='fancy_grid'))
except Exception as e:
    print(f"No se pudo realizar la operacion, {e}")