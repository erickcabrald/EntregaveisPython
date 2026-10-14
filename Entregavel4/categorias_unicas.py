
produtos = [
    {"nome": "Teclado", "preco": 120.00, "categoria": "Periféricos"},
    {"nome": "Mouse", "preco": 80.00, "categoria": "Periféricos"},
    {"nome": "Monitor", "preco": 950.00, "categoria": "Monitores"},
    {"nome": "Headset", "preco": 180.00, "categoria": "Áudio"},
    {"nome": "Webcam", "preco": 200.00, "categoria": "Periféricos"},
]

categorias = set()

for produto in produtos:
    categorias.add(produto["categoria"])

print("--- CATEGORIAS ÚNICAS ---")

for categoria in sorted(categorias):
    print(categoria)
