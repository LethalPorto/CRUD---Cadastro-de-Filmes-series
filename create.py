# Henrique - create.py
# função de tratamento (otimização)
def tratamento_vazio(entrada):
    while True:
        valor = input(entrada).strip()
        if valor != "":
            return valor
        print("Erro: Obrigatório inserir dados...")

# Função para criar novo filme
def adicionar(filmes_series):
    print('-' * 30)
    print('          Adicionar')
    print('-' * 30)
    # Pegando os dados
    while True:
        titulo = tratamento_vazio("Título: ")

        tem = False
        for item in filmes_series:
            if item[0].lower().strip() == titulo.lower().strip():
                tem = True
                break
        if tem == True:
            print("Erro: Esse filme/serie já existe...")
        else:
            break

    genero = tratamento_vazio("Gênero: ")

    while True:
        ano_str = tratamento_vazio("Ano de Lançamento: ")
        try:
            ano = int(ano_str)
            break
        except ValueError:
            print("Erro: Digite um número válido...")

    plataforma = tratamento_vazio("Plataforma: ")

    # colocando os valores na linha
    filme_serie = [titulo, genero, ano, plataforma]
    # Jogando na matriz
    filmes_series.append(filme_serie)

    print(f"\nNovo filme/serie adicionado com sucesso!")
    print(f"{filme_serie[0]} ({filme_serie[2]})")
    print(f"Gênero: {filme_serie[1]}   Plataforma: {filme_serie[3]}")

if __name__ == "__main__":
    adicionar([['teste', 'qualquer', 2025, 'exemplo']])

if __name__ == "__main__":
    adicionar([['teste', 'qualquer', 2025, 'exemplo']])

