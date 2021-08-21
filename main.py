def calculo_multiple(a, b):
    sum= a + b
    res= a - b
    mul= a * b
    return (sum, res, mul, a/b, a ** b)

def main():
    print("Introduce los dos valores sobre los que se haran los calculos:")
    num1 = eval(input("numero 1: "))
    num2 = eval(input("numero 2: "))
    suma, resta, multiplicacion, division, potencia = calculo_multiple(num1, num2)

    print("la suma es:    ", suma)
    print("la resta es:   ", resta)
    print("la multiplicacion es:   ", multiplicacion)
    print("la division es:    ", division)
    print("la potencia es:    ", potencia)

main()