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
        else: # Si el divisor es 0
            return "Error: Division por cero" # Devuelve un error si num2 es 0

    def getNum1(self): # Definimos el metodo getNum1
        return self.num1 # Devuelve el primer numero

    def getNum2(self): # Definimos el metodo getNum2
        return self.num2 # Devuelve el segundo numero

    def setNum1(self, num1): # Definimos el Setter de num1
        self.num1 = num1 # Asigna el valor

    def setNum2(self, num2): # Definimos el Setter de num2
        self.num2 = num2 # Asigna el valor


print("Prueba 1") # Imprime encabezado
n1 = int(input("Ingrese el primer numero: ")) # Pide el primer numero
n2 = int(input("Ingrese el segundo numero: ")) # Pide el segundo numero
c1 = Calculadora(n1, n2) # Crea el objeto c1
print(f"Valores actuales: {c1.getNum1()} y {c1.getNum2()}") # Imprime los valores actuales
print("Suma:", c1.suma()) # Imprime la suma
print("Division:", c1.division()) # Imprime la division

print("\n") # Salto de linea

print("Prueba2 ") # Imprime encabezado
c1.setNum1(100) # Cambiamos num1 a 100
c1.setNum2(50) # Cambiamos num2 a 50
print(f"Nuevos valores tras set: {c1.getNum1()} y {c1.getNum2()}") # Imprime los nuevos valores
print("Multiplicacion:", c1.multiplicacion()) # Imprime la multiplicacion
print("Resta:", c1.resta()) # Imprime la resta

print("\n") # Salto de linea

print("Prueba 3") # Imprime encabezado
c1.setNum2(0) # Cambiamos el divisor a 0
print(f"Valor 1: {c1.getNum1()}, Valor 2: {c1.getNum2()}") # Imprime los valores
print("Resultado division:", c1.division()) # Imprime el resultado de la division

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 03/02/2026
# Hora: 10:25