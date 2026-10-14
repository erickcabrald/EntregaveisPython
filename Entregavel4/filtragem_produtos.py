
produtos = [
    {"nome": "Teclado", "preco": 120.00, "categoria": "Periféricos"},
    {"nome": "Mouse", "preco": 80.00, "categoria": "Periféricos"},
    {"nome": "Monitor", "preco": 950.00, "categoria": "Monitores"},
    {"nome": "Headset", "preco": 180.00, "categoria": "Áudio"},
]

valor = float(input("Informe o preço de referência: R$ ").replace(",", "."))
operacao = input("Filtrar acima ou abaixo? ").strip().lower()

if operacao not in ("acima", "abaixo"):
    print("Operação inválida.")
else:
    encontrados = []

    for produto in produtos:
        if operacao == "acima" and produto["preco"] > valor:
            encontrados.append(produto)
        elif operacao == "abaixo" and produto["preco"] < valor:
            encontrados.append(produto)

    print(f"\nProdutos com preço {operacao} de R$ {valor:.2f}:")

    if encontrados:
        for produto in encontrados:
            print(f"{produto['nome']}: R$ {produto['preco']:.2f}")
    else:
        print("Nenhum produto encontrado.")
