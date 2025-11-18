def deletar(filmes_series):

    while True:

        print(f"Filmes já adicionados:")

        for filme in filmes_series:

            print(f"{filme[0]} ({filme[2]}) - Gênero: {filme[1]}   Plataforma: {filme[3]}")

        resp = input("\nColoque o título do filme que se deseja deletar algo (1 - sair): ").lower()



        if resp == "1":

            print("Voltando ao menu...")

            break



        # Procurar o filme pelo título

        for item in filmes_series:

            if item[0].lower() == resp:



                print(f"Filme encontrado: {resp}")

                print("\nO que você quer deletar?")

                print("[1] Título\n[2] Gênero\n[3] Ano\n[4] Plataforma\n")

                TGAP = int(input("Opção: "))



                if TGAP == 1:

                    filmes_series.remove(item)

                elif TGAP == 2:

                    item[1] = ""

                elif TGAP == 3:

                    item[2] = ""

                elif TGAP == 4:

                    item[3] = ""



                print("\nAlteração feita!")



            else:

                print("Título não encontrado.")
