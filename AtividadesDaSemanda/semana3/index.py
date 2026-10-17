
"""Programa para testar estatísticas, fatorial e relatório."""

import estatistica as est


def fatorial(numero):
    """Calcula o fatorial usando recursão."""
    if numero < 0:
        raise ValueError("O número não pode ser negativo.")

    if numero == 0 or numero == 1:
        return 1

    return numero * fatorial(numero - 1)


def relatorio(titulo, *linhas, **config):
    """Monta um relatório com título, linhas e configurações."""
    separador = config.get("separador", "-")
    resultado = [titulo, separador * len(titulo)]

    for linha in linhas:
        resultado.append(str(linha))

    return "\n".join(resultado)


numeros = [2, 4, 4, 6, 9]

print("Média:", est.media(numeros))
print("Mediana:", est.mediana(numeros))
print("Moda:", est.moda(numeros))

numero = int(input("\nDigite um número para calcular o fatorial: "))
print(f"Fatorial de {numero}: {fatorial(numero)}")

texto = relatorio(
    "Relatório de resultados",
    f"Média: {est.media(numeros)}",
    f"Mediana: {est.mediana(numeros)}",
    f"Moda: {est.moda(numeros)}",
    separador="="
)

print()
print(texto)
