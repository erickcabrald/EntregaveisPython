
"""Funções para calcular estatísticas."""

from statistics import mean, median, mode


def media(numeros):
    """Calcula a média dos números."""
    return mean(numeros)


def mediana(numeros):
    """Calcula a mediana dos números."""
    return median(numeros)


def moda(numeros):
    """Calcula a moda dos números."""
    return mode(numeros)
