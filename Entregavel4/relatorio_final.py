
produtos = [
    {"nome": "Teclado", "preco": 120.00, "categoria": "Periféricos"},
    {"nome": "Mouse", "preco": 80.00, "categoria": "Periféricos"},
    {"nome": "Monitor", "preco": 950.00, "categoria": "Monitores"},
    {"nome": "Headset", "preco": 180.00, "categoria": "Áudio"},
]

print("=" * 45)
print("         RELATÓRIO DE PRODUTOS")
print("=" * 45)

print("\n1. PRODUTOS CADASTRADOS")

for produto in produtos:
    print(
        f"{produto['nome']:<15} "
        f"R$ {produto['preco']:>8.2f} "
        f"| {produto['categoria']}"
    )

precos = [produto["preco"] for produto in produtos]

print("\n2. ORDENAÇÃO CRESCENTE")
produtos.sort(key=lambda produto: produto["preco"])

for produto in produtos:
    print(f"{produto['nome']}: R$ {produto['preco']:.2f}")

print("\n3. ORDENAÇÃO DECRESCENTE")
for produto in sorted(
    produtos,
    key=lambda produto: produto["preco"],
    reverse=True
):
    print(f"{produto['nome']}: R$ {produto['preco']:.2f}")

categorias = {produto["categoria"] for produto in produtos}

print("\n4. CATEGORIAS ÚNICAS")
for categoria in sorted(categorias):
    print(f"- {categoria}")

if precos:
    estatisticas = (
        min(precos),
        max(precos),
        sum(precos) / len(precos)
    )

    print("\n5. ESTATÍSTICAS")
    print(f"Menor preço: R$ {estatisticas[0]:.2f}")
    print(f"Maior preço: R$ {estatisticas[1]:.2f}")
    print(f"Média dos preços: R$ {estatisticas[2]:.2f}")

print("\n" + "=" * 45)
print("           FIM DO RELATÓRIO")
print("=" * 45)
