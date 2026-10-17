
produtos = []

quantidade = int(input("Quantos produtos deseja cadastrar? "))

for i in range(quantidade):
    print(f"\nProduto {i + 1}")

    nome = input("Nome: ")
    preco = float(input("Preço: R$ "))
    categoria = input("Categoria: ")

    produtos.append({
        "nome": nome,
        "preco": preco,
        "categoria": categoria
    })

print("\nFiltrar produtos por preço")
limite = float(input("Digite o preço limite: R$ "))

acima = [produto for produto in produtos if produto["preco"] > limite]
abaixo = [produto for produto in produtos if produto["preco"] < limite]

print("\nProdutos acima do limite")

for produto in acima:
    print(f"{produto['nome']} - R$ {produto['preco']:.2f}")

print("\nProdutos abaixo do limite")

for produto in abaixo:
    print(f"{produto['nome']} - R$ {produto['preco']:.2f}")

crescente = sorted(produtos, key=lambda produto: produto["preco"])
decrescente = sorted(produtos, key=lambda produto: produto["preco"], reverse=True)

print("\nPreços em ordem crescente")

for produto in crescente:
    print(f"{produto['nome']} - R$ {produto['preco']:.2f}")

print("\nPreços em ordem decrescente")

for produto in decrescente:
    print(f"{produto['nome']} - R$ {produto['preco']:.2f}")

categorias = {produto["categoria"] for produto in produtos}

print("\nCategorias sem repetição")

for categoria in sorted(categorias):
    print(categoria)

if produtos:
    precos = [produto["preco"] for produto in produtos]

    menor_preco = min(precos)
    maior_preco = max(precos)
    media_precos = sum(precos) / len(precos)

    estatisticas = (menor_preco, maior_preco, media_precos)

    print("\nRelatório final")
    print(f"Quantidade de produtos: {len(produtos)}")
    print(f"Menor preço: R$ {estatisticas[0]:.2f}")
    print(f"Maior preço: R$ {estatisticas[1]:.2f}")
    print(f"Média dos preços: R$ {estatisticas[2]:.2f}")
    print(f"Categorias: {categorias}")
else:
    print("\nNenhum produto foi cadastrado.")
