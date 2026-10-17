
cadastros = []
quantidade_alunos = 0
quantidade_professores = 0
quantidade_funcionarios = 0

while True:
    comando = input("\nDigite 'cadastrar' ou 'sair': ").lower()

    if comando == "sair":
        break

    if comando != "cadastrar":
        print("Comando inválido.")
        continue

    quantidade = int(input("Quantos cadastros deseja realizar? "))

    for i in range(quantidade):
        print(f"\nCadastro {i + 1}")

        nome = input("Nome: ")
        idade = int(input("Idade: "))

        if idade < 18:
            print("Cadastro permitido somente para maiores de idade.")
            continue

        print("1 - Aluno")
        print("2 - Professor")
        print("3 - Funcionário")

        tipo = int(input("Escolha o tipo de cadastro: "))

        match tipo:
            case 1:
                categoria = "Aluno"
                quantidade_alunos += 1
            case 2:
                categoria = "Professor"
                quantidade_professores += 1
            case 3:
                categoria = "Funcionário"
                quantidade_funcionarios += 1
            case _:
                print("Tipo inválido.")
                continue

        cadastros.append({
            "nome": nome,
            "idade": idade,
            "categoria": categoria
        })

        print("Cadastro realizado!")

print("\nRelatório final")
print(f"Total de cadastros: {len(cadastros)}")
print(f"Alunos: {quantidade_alunos}")
print(f"Professores: {quantidade_professores}")
print(f"Funcionários: {quantidade_funcionarios}")

print("\nNomes cadastrados")

for cadastro in cadastros:
    print(cadastro["nome"])
