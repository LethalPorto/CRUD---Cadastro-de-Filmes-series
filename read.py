# Vitor e Henrique
# E Gustavo Cavarzan
# read.py
# index 0 = Titulo  1 = Genero  2 = Ano  3 = Plataforma
# se tem ele dá true (verdadeiro) caso contrario, mostra mensagem de erro
def mostrar_filme_serie(filme):
    print('-' * 80)
    print(f"{filme[0]} ({filme[2]})")
    print(f"Gênero: {filme[1]}   Plataforma: {filme[3]}")


def ler(filme_series):
    while True:
        while True:
            try:
                print("[1] Ver todos os filmes\n[2] Ver filmes de uma plataforma\n[3] Ver filmes entre certos anos\n[4] Ver filmes por gênero\n[5] Buscar um filme específico\n[0] Voltar ao menu principal\n")
                opcao = int(input("Opção: "))
                if opcao < 0 or opcao > 5:
                    print('Erro: Digite apenas números entre 0 e 5...')
                else:
                    break
            except ValueError:
                print('Erro: Digite apenas números...')
        if opcao == 0:
            break


        elif opcao == 1:
            for filme in filme_series:
                mostrar_filme_serie(filme)
            print('-' * 80)
        elif opcao == 2:
            tem = False
            plataforma = input("digite o nome do plataforma: ")
            for filme in filme_series:
                if plataforma.lower().strip() == filme[3].lower().strip():
                    tem = True

                    mostrar_filme_serie(filme)
            if tem == False:
                print("Erro: Não há filmes/series nessa plataforma...")


            print('-' * 80)

        elif opcao == 3:
            tem = False
            ano1 = int(input("digite o ano para começar : "))
            ano2 = int(input("digite o ano para terminar : "))
            if ano1 > ano2:
                for filme in filme_series:
                    if filme[2] >= ano2 and filme[2] <= ano1:
                        tem = True
                        mostrar_filme_serie(filme)
                if tem == False:
                    print("Erro: Não há filmes/series nessa faxa de ano...")
                print('-' * 80)
            if ano1 < ano2:
                for filme in filme_series:
                    if filme[2] <= ano2 and filme[2] >= ano1:
                        tem = True
                        mostrar_filme_serie(filme)
                if tem == False:
                    print("Erro: Não há filmes/series nessa faxa de ano...")
                print('-' * 80)

        elif opcao == 4:
            tem = False
            genero = input("digite o genero dos filmes: ")
            for filme in filme_series:
                if genero.lower().strip() == filme[1].lower().strip():
                    tem = True
                    mostrar_filme_serie(filme)
            if tem == False:
                 print("Erro: Não há filmes/series com esse gênero...")
            print('-' * 80)
                    
        elif opcao == 5:
            tem = False
            titulo = input("digite o nome do filme: ")
            for filme in filme_series:
                if titulo.lower().strip() == filme[0].lower().strip():
                    tem = True
                    mostrar_filme_serie(filme)
            if tem == False:
                print("Erro: Não há filmes/series com esse nome...")
            print('-' * 80)
                    
if __name__ == "__main__":
    ler ([['Teste','qualquer', 2000,'Prime Video'],['Up','Desenho',2010,'Netflix',]])
