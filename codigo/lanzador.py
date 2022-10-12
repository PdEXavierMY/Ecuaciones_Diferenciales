from codigo.ecuaciones import ecuacion1, ecuacion2, ecuacion3, ecuacion4
from introducir.numero import solicitar_introducir_numero_extremo

def ejercicio():
    eleccion = solicitar_introducir_numero_extremo("¿Qué ecuación deseas resolver?", 1, 4)
    if eleccion == 1:
        print("La solución a la primera ecuación propuesta es: \n")
        ecuacion1()
    elif eleccion == 2:
        print("La solución a la segunda ecuación propuesta es: \n")
        ecuacion2()
    elif eleccion == 3:
        print("La solución a la tercera ecuación propuesta es: \n")
        ecuacion3()
    elif eleccion == 4:
        print("La solución a la cuarta ecuación propuesta es: \n")
        ecuacion4()