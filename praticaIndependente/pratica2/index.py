print("1 - Classificação de cliente")

idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda mensal: "))

if idade < 18:
    print("Cliente menor de idade")
elif renda < 2000:
    print("Cliente Bronze")
elif renda < 5000:
    print("Cliente Prata")
elif renda < 10000:
    print("Cliente Ouro")
else:
    print("Cliente Diamante")


print("\n2 - Menu de operações")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha uma operação: "))
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

match opcao:
    case 1:
        print(f"Resultado: {numero1 + numero2}")
    case 2:
        print(f"Resultado: {numero1 - numero2}")
    case 3:
        print(f"Resultado: {numero1 * numero2}")
    case 4:
        if numero2 != 0:
            print(f"Resultado: {numero1 / numero2}")
        else:
            print("Não é possível dividir por zero")
    case _:
        print("Opção inválida")


print("\n3 - Cálculo de cinco números")

soma = 0
maior = None
menor = None

for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    soma += numero

    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < menor:
        menor = numero

media = soma / 5

print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")


print("\n4 - Sistema de senha")

senhaCorreta = "1234"
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")

    if senha == senhaCorreta:
        print("Acesso permitido")
        break
    else:
        tentativas += 1
        print("Senha incorreta")

if tentativas == 3:
    print("Acesso bloqueado")