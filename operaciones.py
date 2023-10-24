def add (num_1, num_2):
    result = num_1 + num_2
    print (f' {num_1} + {num_2} is equal to {result}')
    return result
  
def multiplicar(numero_1, numero2):
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es: {resultado}")
    return resultado

#operaciones con producto

def producto():
    base = float(input("Ingresa la base: "))
    exponente = int(input("Ingresa el exponente: "))
    resultado = base ** exponente
    print(f"{base} elevado a la {exponente} es igual a: {resultado}")

#operaciones con modulo 
def modulo():
    dividendo = int(input("Ingresa el dividendo: "))
    divisor = int(input("Ingresa el divisor: "))
    resultado = dividendo % divisor
    print(f"El módulo de {dividendo} entre {divisor} es igual a: {resultado}")


