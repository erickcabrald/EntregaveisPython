
import csv
import re
from datetime import datetime


class DadoInvalidoError(Exception):
    """Erro para dados inválidos."""


def validar_email(email):
    return re.fullmatch(r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}", email) is not None


def validar_cpf(cpf):
    return re.fullmatch(r"\d{11}", cpf) is not None


def validar_telefone(telefone):
    return re.fullmatch(r"\d{10,11}", telefone) is not None


def validar_data(data):
    if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", data):
        return False

    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def analisar_dados():
    registros = []
    erros = []

    try:
        with open("dados.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for numero_linha, linha in enumerate(leitor, start=2):
                try:
                    nome = linha["nome"].strip()
                    email = linha["email"].strip()
                    cpf = linha["cpf"].strip()
                    telefone = linha["telefone"].strip()
                    data = linha["data"].strip()

                    if not validar_email(email):
                        raise DadoInvalidoError("Email inválido")

                    if not validar_cpf(cpf):
                        raise DadoInvalidoError("CPF inválido")

                    if not validar_telefone(telefone):
                        raise DadoInvalidoError("Telefone inválido")

                    if not validar_data(data):
                        raise DadoInvalidoError("Data inválida")

                    valor = float(linha["valor"])

                    registros.append({
                        "nome": nome,
                        "email": email,
                        "cpf": cpf,
                        "telefone": telefone,
                        "data": data,
                        "valor": valor
                    })

                except (DadoInvalidoError, ValueError, KeyError) as erro:
                    erros.append(f"Linha {numero_linha}: {erro}")

        if registros:
            total = sum(registro["valor"] for registro in registros)
            media = total / len(registros)

            print("\nRELATÓRIO DE ANÁLISE")
            print("=" * 35)
            print(f"Registros válidos: {len(registros)}")
            print(f"Total dos valores: R$ {total:.2f}")
            print(f"Média dos valores: R$ {media:.2f}")

            for registro in registros:
                print(
                    f"Nome: {registro['nome']} | "
                    f"Email: {registro['email']} | "
                    f"Valor: R$ {registro['valor']:.2f}"
                )

        print(f"\nRegistros com erros: {len(erros)}")

        for erro in erros:
            print(erro)

    except FileNotFoundError:
        print("Arquivo dados.csv não encontrado.")
    except (OSError, csv.Error) as erro:
        print(f"Erro ao ler o arquivo: {erro}")
    finally:
        print("Análise finalizada.")


analisar_dados()
