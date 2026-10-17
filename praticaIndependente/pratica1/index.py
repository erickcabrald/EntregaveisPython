print("1 - Calculadora de troco")
compra = float(input("Digite o valor da compra: R$ "))
pago = float(input("Digite o valor pago: R$ "))
troco = pago - compra
print(f"Troco: R$ {troco:.2f}")

print("\n2 - Conversor de tempo")
segundos = int(input("Digite a quantidade de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundosRestantes = segundos % 60
print(f"{horas} horas, {minutos} minutos e {segundosRestantes} segundos")

print("\n3 - Par ou ímpar")
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

print("\n4 - Média de notas")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"Média: {media:.2f}")

print("\n5 - Calculadora de desconto")
preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto: "))
valorDesconto = preco * desconto / 100
precoFinal = preco - valorDesconto
print(f"Valor do desconto: R$ {valorDesconto:.2f}")
print(f"Preço final: R$ {precoFinal:.2f}")

print("\n6 - Inversor de nome")
nome = input("Digite seu nome: ")
print(f"Nome invertido: {nome[::-1]}")

