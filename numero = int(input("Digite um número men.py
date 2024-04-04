numero = int(input("Digite um número menor que 100: "))
if numero >= 100:
    print("O número inserido não é menor que 100.")
else:
    # Separa os dígitos do número
    dezena = numero // 10
    unidade = numero % 10
    soma = dezena + unidade
    print("A soma dos dígitos de", numero, "é:", soma) 