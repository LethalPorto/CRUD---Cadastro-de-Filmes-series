# main.py
import app_filmes
# Se não salvou nada ainda
filme_series = []

while True:
    print("="*30)
    print("            Menu")
    print("=" * 30, '\n')

    while True:
        try:
            print("[1] Cadastrar filme/serie \n[2] Atualizar filme \n[3] Leitura dos filmes  \n[4] Deletar um filme \n[0] Sair\n")
            opcao = int(input("Opção: "))
            if opcao < 0 or opcao > 4:
                print('Erro: Digite apenas números entre 0 e 4...\n')
            else:
                break
        except ValueError:
            print('Erro: Digite apenas números...\n')

    if opcao == 1:
        app_filmes.adicionar(filme_series)
    elif opcao == 2:
        app_filmes.atualizar(filme_series)
    elif opcao == 3:
        app_filmes.ler(filme_series)
    elif opcao == 4:
        app_filmes.deletar(filme_series)
    elif opcao == 0:
        print("Adeus!")
        break

