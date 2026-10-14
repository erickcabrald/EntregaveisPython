
produtos = []

quantidade = int(input("Quantos produtos deseja cadastrar? "))

for i in range(quantidade):
    print(f"\nCadastro do produto {i + 1}")

    nome = input("Nome: ").strip()
    preco = float(input("Preço: R$ ").replace(",", "."))
    categoria = input("Categoria: ").strip()

    produto = {
        "nome": nome,
        "preco": preco,
        "categoria": categoria
    }

    produtos.append(produto)

print("\n--- PRODUTOS CADASTRADOS ---")

for produto in produtos:
    print(
        f"Nome: {produto['nome']} | "
        f"Preço: R$ {produto['preco']:.2f} | "
        f"Categoria: {produto['categoria']}"
    )
