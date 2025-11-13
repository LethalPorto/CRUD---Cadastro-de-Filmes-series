# Henrique - create.py
# Função para criar novo filme
def adicionar(filmes_series):
    filme_serie = []
    # Pegando os dados
    while True:
        titulo = input("Título: ")
        tem = False
        for item in filmes_series:
            if item[0].lower().strip() == titulo.lower().strip():
                tem = True
                break
        if tem == True:
            print("Esse filme/serie já existe...")
        else:
            break

    genero = input("Gênero: ")

    while True:
        try:
            ano = int(input("Ano de Lançamento: "))
            break
        except ValueError:
            print("Digite um número válido...")

    plataforma = input("Plataforma: ").strip()

    # colocando os valores na linha
    filme_serie.append(titulo)
    filme_serie.append(genero)
    filme_serie.append(ano)
    filme_serie.append(plataforma)

    # Jogando na matriz
    filmes_series.append(filme_serie)

    print(f"\nNovo filme/serie adicionado com sucesso!")
    print(f"{filme_serie[0]} ({filme_serie[2]})")
    print(f"Gênero: {filme_serie[1]}   Plataforma: {filme_serie[3]}\n")

if __name__ == "__main__":
    adicionar([['teste', 'qualquer', 2025, 'exemplo']])