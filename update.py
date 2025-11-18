#Mosias - update.py
#Função para atualizar filmes

def atualizar(filmes_series):
    while True:
        print(f"Filmes já adicionados:")
        #mecanismo de print, ele busca cada titulo, genero... em um loop for na matriz por indice
        for filme in filmes_series:
            print(f"{filme[0]} ({filme[2]}) - Gênero: {filme[1]}   Plataforma: {filme[3]}")
        #Pedindo Titulo do filme para a localização pelo titulo
        resposta = input("Coloque o titulo do filme que deseja editar (1 - Sair):  ").lower()
        #saindo e voltando pro menu
        if resposta == "1":
            print("Voltando ao menu...\n")
            break
        #nesse elif ele confere se a resposta seja diferente de nada ele passa para o resto do codigo
        elif resposta != "":
            T_G_A_P = int(input("O que você deseja editar?: [1] Titulo [2] Genêro [3] Ano de Lançamento [4] Plateforma: "))
            #se T_G_A_P igual a 1 vai proceguir
            if T_G_A_P == 1:
                #vou utilizar essa variavel para quebrar o loop mais externo do for aninhado
                a = False
                #primeiro for percorrendo a lista de listas
                for i in filmes_series:
                    #utilizando a variavel que vai ser declarado como True talvez mais a frente para a quebra do for
                    if a == True:
                        break
                    #for que percorre a lista encontrada no for externo    
                    for j in i:
                        nova_lista = []
                        #pega o titulo
                        if j == resposta:
                            #esse for coloca os itens na nova lista
                            for k in i:
                                nova_lista.append(k)
                            #removendo titulo errado da lsita    
                            nova_lista.remove(j)
                            novo_titulo = input("Informe o titulo novo: ")
                            #colocando novo titulo na mesma pocição de antes
                            nova_lista.insert(0, novo_titulo)
                            #pegando posição da lista antiga
                            position = filmes_series.index(i)
                            #removendo lista antiga
                            filmes_series.remove(i)
                            #colocando lista nova  na exata mesma posição da lista antiga
                            filmes_series.insert(position, nova_lista)
                            print(f"Veja se a lista foi atualizada corretamente:")
                            # sistema de print
                            for filme in filmes_series:
                                print(f"{filme[0]} ({filme[2]}) - Gênero: {filme[1]}   Plataforma: {filme[3]}")
                            #aqui esta pedindo se a informação ataulziada esta correta
                            r_s_n = int(input("[1] Sim  [2] Não: "))
                            
                            if r_s_n == 1:
                                #se sim vai quebrar o for aninhado
                                a = True
                            else:
                                #se não vai retomar o processo e como guardado vai adicionar a lista antiga sendo uma medida de segurança
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


