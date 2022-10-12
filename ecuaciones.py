#crea una funcion que resuelva una ecuacion diferencial
import sympy as sp
def ecuacion():
    x = sp.Symbol('x')
    y = sp.Function('y')
    f = (x**2*(y(x))-(y(x)))/(y(x)+1)
    sp.Eq(y(x).diff(x), f)
    sol = sp.dsolve(y(x).diff(x) - f)
    print(sol)

ecuacion()