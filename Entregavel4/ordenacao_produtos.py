
produtos = [
    {"nome": "Teclado", "preco": 120.00},
    {"nome": "Mouse", "preco": 80.00},
    {"nome": "Monitor", "preco": 950.00},
    {"nome": "Headset", "preco": 180.00},
]

# sort() modifica a lista original.
produtos.sort(key=lambda produto: produto["preco"])

print("--- ORDEM CRESCENTE ---")

for produto in produtos:
    print(f"{produto['nome']}: R$ {produto['preco']:.2f}")

# sorted() cria uma nova lista em ordem decrescente.
produtos_decrescente = sorted(
    produtos,
    key=lambda produto: produto["preco"],
    reverse=True
)

print("\n--- ORDEM DECRESCENTE ---")

for produto in produtos_decrescente:
    print(f"{produto['nome']}: R$ {produto['preco']:.2f}")
