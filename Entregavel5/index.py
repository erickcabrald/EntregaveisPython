
import csv
import re
from datetime import datetime


class FormatoInvalidoError(Exception):
    pass


def validar_email(email):
    return re.fullmatch(r"[\w.-]+@[\w.-]+\.\w+", email) is not None


def validar_cpf(cpf):
    return re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf) is not None


def validar_telefone(telefone):
    return re.fullmatch(r"\(?\d{2}\)?\s?9?\d{4}-?\d{4}", telefone) is not None


def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def analisar_dados():
    validos = 0
    invalidos = 0
    arquivo = None

    try:
        arquivo = open("dados.csv", "r", encoding="utf-8")
        leitor = csv.DictReader(arquivo)

        for linha, dados in enumerate(leitor, start=2):
            try:
                if (
                    validar_email(dados["email"])
                    and validar_cpf(dados["cpf"])
                    and validar_telefone(dados["telefone"])
                    and validar_data(dados["data"])
                ):
                    validos += 1
                    print(f"Linha {linha}: {dados['nome']} - Válido")
                else:
                    raise FormatoInvalidoError("Formato incorreto")

            except FormatoInvalidoError as erro:
                invalidos += 1
                print(f"Linha {linha}: {dados['nome']} - Inválido: {erro}")

            except KeyError as erro:
                print(f"Coluna ausente: {erro}")
                raise

    except FileNotFoundError:
        print("Erro: arquivo dados.csv não encontrado.")

    except KeyError:
        print("Verifique as colunas do arquivo CSV.")

    except ValueError as erro:
        print(f"Erro nos dados: {erro}")

    else:
        print("\nAnálise concluída!")

    finally:
        if arquivo:
            arquivo.close()
        print("Arquivo fechado.")

    total = validos + invalidos

    try:
        with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("RELATÓRIO DE ANÁLISE\n")
            arquivo.write(f"Total: {total}\n")
            arquivo.write(f"Válidos: {validos}\n")
            arquivo.write(f"Inválidos: {invalidos}\n")

        print(f"\nTotal: {total}")
        print(f"Válidos: {validos}")
        print(f"Inválidos: {invalidos}")

    except OSError as erro:
        print(f"Erro ao salvar relatório: {erro}")


analisar_dados()
