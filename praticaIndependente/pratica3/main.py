
def celsius_para_fahrenheit(c):
    return (c * 9 / 5) + 32


def validar_senha(senha):
    return len(senha) >= 8


def caixa(*precos):
    if len(precos) == 0:
        return 0, 0, 0

    total = sum(precos)
    maior = max(precos)
    media = total / len(precos)

    return total, maior, media


def ficha_aluno(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


def lista_segura(lista, item):
    nova_lista = lista.copy()
    nova_lista.append(item)
    return nova_lista


print("1 - Conversor")
print(celsius_para_fahrenheit(30))

print("\n2 - Validador")
senha = input("Digite uma senha: ")
print(validar_senha(senha))

print("\n3 - Caixa")
total, maior, media = caixa(10, 25, 40, 15)
print(f"Total: R$ {total:.2f}")
print(f"Item mais caro: R$ {maior:.2f}")
print(f"Média: R$ {media:.2f}")

print("\n4 - Ficha do aluno")
ficha_aluno(nome="Erick", idade=17, curso="ADS")

print("\n5 - Módulo de utilidades")
from ultilidades import somar, multiplicar, dividir

print(somar(10, 5))
print(multiplicar(10, 5))
print(dividir(10, 5))

print("\n6 - Lista segura")
lista = [1, 2, 3]
nova_lista = lista_segura(lista, 4)
print(f"Original: {lista}")
print(f"Nova: {nova_lista}")
