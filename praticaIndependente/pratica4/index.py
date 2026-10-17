
nomes = []

while True:
    nome = input("Digite um nome ou 'fim' para terminar: ")

    if nome.lower() == "fim":
        break

    if nome.strip():
        nomes.append(nome.strip())

nomes_unicos = list(set(nomes))
nomes_unicos = sorted(nomes_unicos, key=str.lower)

if len(nomes_unicos) > 0:
    primeiro_nome = nomes_unicos[0]
    ultimo_nome = nomes_unicos[-1]
    tupla_nomes = (primeiro_nome, ultimo_nome)
else:
    tupla_nomes = ()

print("\nRelatório final")
print(f"Nomes digitados: {len(nomes)}")
print(f"Nomes únicos: {len(nomes_unicos)}")
print(f"Lista ordenada: {nomes_unicos}")
print(f"Tupla: {tupla_nomes}")
