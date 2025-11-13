#Mosias - update.py
#Função para atualizar filmes

def atualizar(filmes_series):
    while True:
        print(f"Filmes já adicionados:")
        
        for filme in filmes_series:
            print(f"{filme[0]} ({filme[2]}) - Gênero: {filme[1]}   Plataforma: {filme[3]}")
            
        resposta = input("Coloque o titulo do filme que deseja editar (1 - Sair):  ").lower()
        
        if resposta == "1":
            print("Voltando ao menu...\n")
            break
            
        elif resposta != "":
            T_G_A_P = int(input("O que você deseja editar?: [1] Titulo [2] Genêro [3] Ano de Lançamento [4] Plateforma: "))
            
            if T_G_A_P == 1:
                a = False
                
                for i in filmes_series:
                    
                    if a == True:
                        break
                        
                    for j in i:
                        nova_lista = []
                        
                        if j == resposta:
                            for k in i:
                                nova_lista.append(k)
                            nova_lista.remove(j)
                            novo_titulo = input("Informe o titulo novo: ")
                            nova_lista.insert(0, novo_titulo)
                            position = filmes_series.index(i)
                            filmes_series.remove(i)
                            filmes_series.insert(position, nova_lista)
                            print(f"Veja se a lista foi atualizada corretamente:")
                            
                            for filme in filmes_series:
                                print(f"{filme[0]} ({filme[2]}) - Gênero: {filme[1]}   Plataforma: {filme[3]}")
                            r_s_n = int(input("[1] Sim  [2] Não: "))
                            
                            if r_s_n == 1:
                                a = True
                            else:
                                filmes_series.remove(nova_lista)
                                filmes_series.append(i)
                                continue
                                
            elif T_G_A_P == 2:
                b = False
                
                for i in filmes_series:
                    
                    if b == True:
                        break
                        
                    for j in i:
                        
                        if j == resposta:
                            novo_genero = input("Informe o novo gênero do filme: ")
                            nova_lista2 = []
                            
                            for k in i:
                                nova_lista2.append(k)
                                
                            nova_lista2.pop(1)
                            nova_lista2.insert(1, novo_genero)
                            position2 = filmes_series.index(i)
                            filmes_series.remove(i)
                            filmes_series.insert(position2, nova_lista2)
                            print(f"Veja se a lista foi atualizada corretamente:")
                            
                            for filme in filmes_series:
                                print(f"{filme[0]} ({filme[2]}) - Gênero: {filme[1]}   Plataforma: {filme[3]}")
                                
                            r_s_n2 = int(input("[1] Sim  [2] Não: "))
                            
                            if r_s_n2 == 1:
                                b = True
                            else:
                                filmes_series.remove(nova_lista2)
                                filmes_series.append(i)
                                continue
                                
            elif T_G_A_P == 3:
                c = False
                
                for i in filmes_series:
                    
                    if c == True:
                        break
                        
                    for j in i:
                        
                        if j == resposta:
                            novo_Ano = input("Informe o novo ano de lançamento do filme: ")
                            nova_lista3 = []
                            
                            for k in i:
                                nova_lista3.append(k)
                                
                            nova_lista3.pop(2)
                            nova_lista3.insert(2, novo_Ano)
                            position3 = filmes_series.index(i)
                            filmes_series.remove(i)
                            filmes_series.insert(position3, nova_lista3)
                            print(f"Veja se a lista foi atualizada corretamente:")
                            
                            for filme in filmes_series:
                                print(f"{filme[0]} ({filme[2]}) - Gênero: {filme[1]}   Plataforma: {filme[3]}")
                                
                            r_s_n3 = input("[1] Sim  [2] Não: ")
                            
                            if r_s_n3 == 1:
                                c = True
                            else:
                                filmes_series.remove(nova_lista3)
                                filmes_series.append(i)
                                continue
                                
            elif T_G_A_P == 4:
                d = False
                
                for i in filmes_series:
                    if d == True:
                        break
                        
                    for j in i:
                        if j == resposta:
                            nova_Plataforma = input("Informe a nova plataforma do filme: ")
                            nova_lista4 = []
                            
                            for k in i:
                                nova_lista4.append(k)
                                
                            nova_lista4.pop(3)
                            nova_lista4.insert(3, nova_Plataforma)
                            position4 = filmes_series.index(i)
                            filmes_series.remove(i)
                            filmes_series.insert(position4, nova_lista4)
                            print(f"Veja se a lista foi atualizada corretamente:")
                            
                            for filme in filmes_series:
                                print(f"{filme[0]} ({filme[2]}) - Gênero: {filme[1]}   Plataforma: {filme[3]}")
                                
                            r_s_n4 = input("[1] Sim  [2] Não: ")
                            
                            if r_s_n4 == 1:
                                d = True
                            else:
                                filmes_series.remove(nova_lista4)
                                filmes_series.append(i)
                                continue
        else:
            print("Informe um título valido.")
            continue
