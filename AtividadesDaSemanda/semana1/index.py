
import math

print("1 - Conversor de tempo")

segundos = int(input("Digite a quantidade de segundos: "))

dias = segundos // 86400
horas = (segundos % 86400) // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print(f"Dias: {dias}")
print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos_restantes}")

print("\n2 - Calculadora de círculo")

raio = float(input("Digite o raio do círculo: "))

area = math.pi * raio ** 2
circunferencia = 2 * math.pi * raio

print(f"Área: {area:.2f}")
print(f"Circunferência: {circunferencia:.2f}")

print("\n3 - Analisador de frase")

frase = input("Digite uma frase: ")

quantidade_caracteres = len(frase)
quantidade_palavras = len(frase.split())
frase_maiuscula = frase.upper()

print(f"Quantidade de caracteres: {quantidade_caracteres}")
print(f"Quantidade de palavras: {quantidade_palavras}")
print(f"Frase em maiúsculas: {frase_maiuscula}")
