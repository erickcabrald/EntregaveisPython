
produtos = [
    {"nome": "Teclado", "preco": 120.00},
    {"nome": "Mouse", "preco": 80.00},
    {"nome": "Monitor", "preco": 950.00},
    {"nome": "Headset", "preco": 180.00},
]

precos = [produto["preco"] for produto in produtos]

if precos:
    menor_preco = min(precos)
    maior_preco = max(precos)
    media_precos = sum(precos) / len(precos)

    estatisticas = (menor_preco, maior_preco, media_precos)

    print("--- ESTATÍSTICAS ---")
    print(f"Menor preço: R$ {estatisticas[0]:.2f}")
    print(f"Maior preço: R$ {estatisticas[1]:.2f}")
    print(f"Preço médio: R$ {estatisticas[2]:.2f}")
else:
    print("Não há produtos cadastrados.")
