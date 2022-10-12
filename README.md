# Ecuaciones_Diferenciales
<h1 align="center">Ecuaciones diferenciles propuestas en exámen</h1>

En este [repositorio](https://github.com/Xavitheforce/Ecuaciones_Diferenciales) quedan resuletos las cuatro ecuaciones diferenciales con python.

El código empleado para resolverlo es el siguiente:

```python
import sympy as sp
import math

def ecuacion1():
    x = sp.Symbol('x')
    y = sp.Function('y')
    f = ((x**2)*(y(x))-(y(x)))/((y(x))+1)
    ecuacion = sp.Eq(y(x).diff(), f)
    ics = {y(3): -1}
    sol = sp.dsolve(ecuacion, y(x), ics=ics)
    print(sol, "\n")
    sp.pprint(sol)
    print("\n")

def ecuacion2():
    x = sp.Symbol('x')
    y = sp.Function('y')
    f = y(x)*sp.log(y(x))
    ecuacion = sp.Eq(y(x).diff()*sp.sin(x), f)
    ics = {y(math.pi/2): math.e}
    sol = sp.dsolve(ecuacion, y(x), ics=ics)
    print(sol, "\n")
    sp.pprint(sol)
    print("\n")

def ecuacion3():
    x = sp.Symbol('x')
    y = sp.Function('y')
    f = 2*(x-2)**2
    ecuacion = sp.Eq(y(x).diff()-(y(x)/x-2), f)
    sol = sp.dsolve(ecuacion, y(x))
    print(sol, "\n")
    sp.pprint(sol)
    print("\n")

def ecuacion4():
    x = sp.Symbol('x')
    y = sp.Function('y')
    f = 3*x**2
    ecuacion = sp.Eq(2*x*y(x).diff()-y(x), f)
    sol = sp.dsolve(ecuacion, y(x))
    print(sol, "\n")
    sp.pprint(sol)
    print("\n")
```
