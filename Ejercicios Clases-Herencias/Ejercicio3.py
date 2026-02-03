# Realizar un programa en el cual se declaren dos valores enteros por teclado Calcular
# después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir
# los resultados obtenidos. Llamar a la clase Calculadora.
# Entrada: dos valores enteros
# Salida: suma, resta, multiplicación y división


class Calculadora: # Define la clase Calculadora
    def __init__(self, num1, num2): # Define el constructor
        self.num1 = num1 # Define el atributo num1
        self.num2 = num2 # Define el atributo num2

    def suma(self): # Define el metodo suma
        return self.num1 + self.num2 # Devuelve la suma de num1 y num2

    def resta(self): # Define el metodo resta
        return self.num1 - self.num2 # Devuelve la resta de num1 y num2

    def multiplicacion(self): # Define el metodo multiplicacion
        return self.num1 * self.num2 # Devuelve la multiplicacion de num1 y num2

    def division(self): # Define el metodo division
        if self.num2 != 0: # Si num2 es diferente de 0
            return self.num1 / self.num2 # Devuelve la division de num1 y num2
        else:
            return "Error: Division por cero" # Devuelve un error si num2 es 0

num1 = int(input("Ingrese el primer numero: ")) # Pide el primer numero
num2 = int(input("Ingrese el segundo numero: ")) # Pide el segundo numero
calculadora = Calculadora(num1, num2) # Crea el objeto calculadora

print("Suma:", calculadora.suma()) # Imprime la suma
print("Resta:", calculadora.resta()) # Imprime la resta
print("Multiplicacion:", calculadora.multiplicacion()) # Imprime la multiplicacion
print("Division:", calculadora.division()) # Imprime la division

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 03/02/2026
# Hora: 10:25