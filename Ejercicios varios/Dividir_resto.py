# Pedir dos numero enteros y muestre por pantalla la división (n1) entre (n2), de cociente (c) y resto (r).

n1 = int(input("Introduce el primer número entero : "))
n2 = int(input("Introduce el segundo número entero : "))
c = n1 // n2 #La doble barra solo devuelve el cociente, si fuese con una barra daría los decimales y no daría el resto.
r = n1 % n2 #El porcentaje devuelve el resto de la división.
print(f"{n1} entre {n2} da un cociente de {c} y un resto de {r}")

# La f es para que se muestre el valor de las variables
