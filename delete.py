def deletar(filmes_series):
    while True:
        print("Filmes já adicionados:")
        for filme in filmes_series:
            print(f"{filme[0]} ({filme[2]}) - Gênero: {filme[1]}   Plataforma: {filme[3]}")

        resp = input("\nDigite o título do filme que deseja deletar algo (1 - sair): ").lower()

        if resp == "1":
            print("Voltando ao menu...")
            break

        # Procurar o filme
        encontrado = False
        for item in filmes_series:
            if item[0].lower() == resp:
                encontrado = True
                break

        if encontrado == False:
            print("Erro: Título não encontrado.\n")
            continue

        print(f"\nFilme encontrado: {encontrado[0]}")
        print("O que você quer deletar?")
        print("[1] Título\n[2] Gênero\n[3] Ano\n[4] Plataforma\n")

        try:
            TGAP = int(input("Opção: "))
            if TGAP < 1 or TGAP > 4:
                print("Erro: Opção inválida.\n")
                continue
        except ValueError:
            print("Erro: Digite um número válido.\n")
            continue

        if TGAP == 1:
            filmes_series.remove(encontrado)
            print("Filme removido por completo!")
        elif TGAP == 2:
            encontrado[1] = ""
        elif TGAP == 3:
            encontrado[2] = ""
        elif TGAP == 4:
            encontrado[3] = ""

        print("Alteração feita!\n")
