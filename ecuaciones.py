#crea una funcion que resuelva una ecuacion diferencial
import sympy as sp
import math
def ecuacion1():
    x = sp.Symbol('x')
    y = sp.Function('y')
    f = ((x**2)*(y(x))-(y(x)))/((y(x))+1)
    sp.Eq(y(x).diff(), f)
    ics = {y(3): -1}
    sol = sp.dsolve(y(x).diff(x) - f)
    print(sol)

ecuacion1()

def ecuacion2():
    x = sp.Symbol('x')
    y = sp.Function('y')
    f = y(x)*float(math.log(y(x)))
    sp.Eq(y(x).diff()*math.sin(x), f)
    sol = sp.dsolve(y(x).diff(x) - f)
    print(sol)


def ecuacion3():
    x = sp.Symbol('x')
    y = sp.Function('y')
    f = 2*(x-2)**2
    sp.Eq(y(x).diff()-(y(x)/x-2), f)
    sol = sp.dsolve(y(x).diff(x) - f)
    print(sol)

ecuacion3()