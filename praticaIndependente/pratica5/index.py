
import csv
import json
import re


class ClienteInvalidoError(Exception):
    pass


def validar_email(email):
    return re.fullmatch(r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}", email) is not None


def validar_cpf(cpf):
    cpf = re.sub(r"\D", "", cpf)
    return len(cpf) == 11


def cadastrar_clientes():
    clientes = []

    try:
        with open("clientes.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                nome = linha["nome"].strip()
                email = linha["email"].strip()
                cpf = linha["cpf"].strip()

                if not validar_email(email):
                    raise ClienteInvalidoError(
                        f"Email inválido para {nome}"
                    )

                if not validar_cpf(cpf):
                    raise ClienteInvalidoError(
                        f"CPF inválido para {nome}"
                    )

                clientes.append({
                    "nome": nome,
                    "email": email,
                    "cpf": cpf
                })

        with open("clientes.json", "w", encoding="utf-8") as arquivo:
            json.dump(clientes, arquivo, ensure_ascii=False, indent=4)

        print(f"Clientes cadastrados: {len(clientes)}")

        for cliente in clientes:
            print(
                f"Nome: {cliente['nome']} | "
                f"Email: {cliente['email']} | "
                f"CPF: {cliente['cpf']}"
            )

    except FileNotFoundError:
        print("Arquivo clientes.csv não encontrado.")
    except (KeyError, csv.Error) as erro:
        print(f"Erro no arquivo CSV: {erro}")
    except ClienteInvalidoError as erro:
        print(f"Erro de validação: {erro}")
    except OSError as erro:
        print(f"Erro ao acessar arquivo: {erro}")
    finally:
        print("Processamento finalizado.")


cadastrar_clientes()
