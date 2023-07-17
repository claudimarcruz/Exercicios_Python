print("DIGITE DOIS NÙMEROS")
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))

print(f"{'#' * 5} {'MENU'} {'#' * 5}")
print("1. Média ponderada, com pesos 2 e 3, respectivamente")
print("2. Quadrado da soma dos dois números")
print("3. Cubo de menor número")

opcao = int(input("Escolha uma opção: "))

if opcao < 1 or opcao > 3:
    print("Opção Inválida!")
elif opcao == 1:
    peso2 = 2
    peso3 = 3

    media_ponderada = ((num1 * peso2) + (num2 * peso3)) / (peso2 + peso3)
    print(f"A média ponderada é {media_ponderada:.2f}")
elif opcao == 2:
    soma = num1 + num2
    quadrado_soma = pow(soma, 2)
    print(f"O quadrado da soma e: {quadrado_soma:.2f}")
else:
    if num1>num2:
        cubo_menor = pow(num2, 3)
        print(f"O cubo de {num2} é: {cubo_menor}")
    elif num2>num1: 
        cubo_menor = pow(num1, 3)
        print(f"O cubo de {num1} é: {cubo_menor}")
    else:
        print("Valores iguais!")



