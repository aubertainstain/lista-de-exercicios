lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # Verifica o tipo de triângulo
    if lado1 == lado2 == lado3:
        print("Os lados informados formam um triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Os lados informados formam um triângulo isósceles.")
    else:
        print("Os lados informados formam um triângulo escaleno.")
else:
    print("Os lados informados não podem formar um triângulo.")