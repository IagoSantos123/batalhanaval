from constantes import *
import random
#captura a linha e coluna para posicionar o barco, previnindo de erros
def captura_lin_col(tam_barco,nome_barco, orientacao):
    linha = input(f'Em qual LINHA você deseja posicionar a {nome_barco}?\nSua resposta: ')
    while linha not in ('0','1','2','3','4','5','6','7','8','9'):
        linha = input(f'\n\nResposta inválida! Tente novamente.\n\nEm qual LINHA você deseja posicionar a {nome_barco}?\n\nSua resposta: ').lower().strip()
    linha = int(linha)
    
    coluna = input(f'Em qual COLUNA você deseja posicionar a {nome_barco}?\nSua resposta: ')
    while coluna not in ('0','1','2','3','4','5','6','7','8','9'):
        coluna = input(f'\n\nResposta inválida! Tente novamente.\n\nEm qual LINHA você deseja posicionar a {nome_barco}?\n\nSua resposta: ').lower().strip()
    coluna = int(coluna)
    
    if orientacao == 'v':

        while linha+tam_barco-1>9:
            linha= input(f'\033[7mLembre-se que o(a) {nome_barco} ocupa {tam_barco} posições e não pode ser colocado nesse lugar\033[m\n\nLINHA: ')
            while linha not in ('0','1','2','3','4','5','6','7','8','9'):
                linha = input(f'\n\nResposta inválida! Tente novamente.\n\nEm qual LINHA você deseja posicionar a {nome_barco}?\n\nSua resposta: ').lower().strip()
            linha = int(linha)

    elif orientacao == 'h':
        while coluna+tam_barco-1>9:
            coluna = input(f'\n\033[1mLembre-se que o {nome_barco}\033[1m ocupa {tam_barco} posições e não pode ser colocado nesse lugar\033[m\n\nCOLUNA: ')
            while coluna not in ('0','1','2','3','4','5','6','7','8','9'):
                coluna = input(f'\n\nResposta inválida! Tente novamente.\n\nEm qual LINHA você deseja posicionar a {nome_barco}?\n\nSua resposta: ').lower().strip()
            coluna = int(coluna)

    return linha, coluna


#jogada do usuario
def jogada_usuario(tabuleiro_PC, tabuleiro_PC_mostrar):
    print('\n\033[1mChegou sua vez de jogar, agora escolha:\033[m')
    global lista_jogadas
    global total_casas_pc
    #valida o input
    while(1):
        try:
            linha = int(input('LINHA: '))
            while linha<0 or linha>9:
                linha = int(input('\nResposta inválida.\nLINHA: '))
            break
        except ValueError:
            print("Resposta inválida.\nboa tentativa, Henrique.")
    while(1):
        try:
            coluna = int(input('\nCOLUNA: '))
            while coluna<0 or coluna>9:
                coluna = int(input('\nResposta inválida.\nLINHA: '))
            break
        except ValueError:
            print("Resposta inválida.\nboa tentativa, Henrique.")


    tiro = tabuleiro_PC[linha][coluna]
    
    jogada = f'{linha},{coluna}'
    while jogada in lista_jogadas:
        while(1):
            try:
                linha = int(input('Você já jogou nesse lugar!Tente outro.\nLINHA: '))
                while linha<0 or linha>9:
                    linha = int(input('\nResposta inválida.\nLINHA: '))
                break
            except ValueError:
                print("Resposta inválida.\nboa tentativa, Henrique.")
        while(1):
            try:
                coluna = int(input('Você já jogou nesse lugar!Tente outro.\nLINHA:COLUNA: '))
                while coluna<0 or coluna>9:
                    coluna = int(input('\nResposta inválida.\COLUNA: '))
                break
            except ValueError:
                print("Resposta inválida.\nboa tentativa, Henrique.")
        jogada = f'{linha},{coluna}'
    lista_jogadas.append(jogada)
    tiro = tabuleiro_PC[linha][coluna]

    if tiro == SUBMARINO:
        embarcacao_atingida = SUBMARINO_ESCRITO
        tabuleiro_PC_mostrar[linha][coluna] = f'\033[41m{tiro}\033[m'
        total_casas_pc-=1
    elif tiro == CORVETA:
        embarcacao_atingida = CORVETA_ESCRITO
        tabuleiro_PC_mostrar[linha][coluna] = f'\033[41m{tiro}\033[m'
        total_casas_pc-=1
    elif tiro == ENCOURACADO:
        embarcacao_atingida = ENCOURACADO_ESCRITO
        tabuleiro_PC_mostrar[linha][coluna] = f'\033[41m{tiro}\033[m'
        total_casas_pc-=1
    elif tiro == PORTA_AVIOES:
        embarcacao_atingida = PORTA_AVIOES_ESCRITO
        tabuleiro_PC_mostrar[linha][coluna] = f'\033[41m{tiro}\033[m'
        total_casas_pc-=1
    else:
        embarcacao_atingida = 'AGUA'
        tabuleiro_PC_mostrar[linha][coluna] = f'\033[44m0\033[m'
    print(f'\n\n\033[7mVOCE ATINGIU: {embarcacao_atingida}\033[m')

    print('\n\n  TABULEIRO DO PC')
    printar_tabuleiro(tabuleiro_PC_mostrar)

    return tabuleiro_PC, tabuleiro_PC_mostrar


#jogada do pc quando não tem nenhum acerto previo
def jogada_aleatoria(tabuleiro):
    linha = random.randint(0,9)
    coluna = random.randint(0,9)
    tiro = tabuleiro[linha][coluna]
    while tiro == f'\033[41mX\033[m':
        linha = random.randint(0,9)
        coluna = random.randint(0,9)
        tiro = tabuleiro[linha][coluna]

    return (tiro, linha, coluna)

#jogada do pc quando se tem acerto previo, dando continuidade para direita
def continua_pra_direita(tabuleiro, tiro, linha, coluna, tabuleiro_PC, tabuleiro_PC_mostrar):


    conta_ocorrencias = 0
    while tiro != '0':
        #jogada do usuario
        tabuleiro_PC, tabuleiro_PC_mostrar = jogada_usuario(tabuleiro_PC, tabuleiro_PC_mostrar)
        if total_embarcacoes_pc ==0:
            break
        conta_ocorrencias +=1
        acertou = True
        tabuleiro[linha][coluna] = f'\033[41mX\033[m'
        print(f'\n\033[7mPC ATINGIU {tiro}\033[m')

        #Mostra a situação do tabuleiro do usuario
        print('\nTABULEIRO DO USUARIO')
        printar_tabuleiro(tabuleiro)

        #printando visao do pc

        linha = linha
        coluna +=1
        if coluna>9:
            break
        
        tiro = tabuleiro[linha][coluna]
    
    #conta as ocorrencias para descobbrir a orientacao
    if conta_ocorrencias>=1: orientacao = 'h'
    else: orientacao = ''

    return (tabuleiro,orientacao)
#jogada do pc quando se tem acerto previo, dando continuidade para direita





#jogada do pc quando se tem acerto previo, dando continuidade para esquerda
def continua_pra_esquerda(tabuleiro, tiro, linha, coluna, tabuleiro_PC, tabuleiro_PC_mostrar):
    conta_ocorrencias = 0
    while tiro != '0':
        #jogada do usuario
        tabuleiro_PC, tabuleiro_PC_mostrar = jogada_usuario(tabuleiro_PC, tabuleiro_PC_mostrar)
        if total_embarcacoes_pc ==0:
            break
        conta_ocorrencias +=1


        tabuleiro[linha][coluna] = f'\033[41mX\033[m'
        print(f'\n\033[7mPC atingiu {tiro}\033[m')

        #Mostra a situação do tabuleiro do usuario
        print('\nTABULEIRO DO USUARIO')
        printar_tabuleiro(tabuleiro)
        

        

        linha = linha
        coluna -= 1
        #condição de parada para não sair da lista
        if coluna<0:            
            break
        tiro = tabuleiro[linha][coluna]
    
    #conta as ocorrencias para descobbrir a orientacao
    if conta_ocorrencias>=1: orientacao = 'h'
    else: orientacao = ''

    return (tabuleiro,orientacao)
#jogada do pc quando se tem acerto previo, dando continuidade para esquerda




#jogada do pc quando se tem acerto previo, dando continuidade para cima
def continua_pra_cima(tabuleiro, tiro, linha, coluna, tabuleiro_PC, tabuleiro_PC_mostrar):
    conta_ocorrencias = 0
    while tiro != '0':
        #jogada do usuario
        tabuleiro_PC, tabuleiro_PC_mostrar = jogada_usuario(tabuleiro_PC, tabuleiro_PC_mostrar)
        if total_embarcacoes_pc ==0:
            break
        conta_ocorrencias +=1


        tabuleiro[linha][coluna] = f'\033[41mX\033[m'
        
        print(f'\n\033[7mPC atingiu {tiro}\033[m')

        #Mostra a situação do tabuleiro do usuario
        print('\nTABULEIRO DO USUARIO')
        printar_tabuleiro(tabuleiro)

        linha -=1
        coluna = coluna
        #condição de parada para não sair da lista
        if linha<0:
            break
        tiro = tabuleiro[linha][coluna]
        
    #conta as ocorrencias para descobbrir a orientacao
    if conta_ocorrencias>1: orientacao = 'v'
    else: orientacao = ''
        
    return (tabuleiro,orientacao)
#jogada do pc quando se tem acerto previo, dando continuidade para cima



#jogada do pc quando se tem acerto previo, dando continuidade para baixo
def continua_pra_baixo(tabuleiro, tiro, linha, coluna, tabuleiro_PC, tabuleiro_PC_mostrar):
    conta_ocorrencias = 0
    while tiro != '0':
        #jogada do usuario
        tabuleiro_PC, tabuleiro_PC_mostrar = jogada_usuario(tabuleiro_PC, tabuleiro_PC_mostrar)
        if total_embarcacoes_pc ==0:
            break

        conta_ocorrencias +=1

        tabuleiro[linha][coluna] = f'\033[41mX\033[m'
        print(f'\n\033[7mPC atingiu {tiro}\033[m')
        #Mostra a situação do tabuleiro do usuario
        print('\nTABULEIRO DO USUARIO')
        printar_tabuleiro(tabuleiro)
        
        
        linha +=1
        coluna = coluna

        #condição de parada para não sair da lista
        if linha>9:
            break
        tiro = tabuleiro[linha][coluna]

        
    #conta as ocorrencias para descobbrir a orientacao
    if conta_ocorrencias>=1: orientacao = 'v'
    else: orientacao = ''
 

    return (tabuleiro,orientacao)
#jogada do pc quando se tem acerto previo, dando continuidade para baixo


#printar_tabuleiro
def printar_tabuleiro(tabuleiro):
    print()
    for linha in range(10):
        for coluna in range(10):
            print(tabuleiro[linha][coluna], end=' ')
        print()  
    return 0 
#printar_tabuleiro

#verifica entorno
def verifica_entorno(tabuleiro_pc,tam_barco, orientacao, linha, coluna):
    pode_posicionar = True
    
    if orientacao =='h':
        inicio_linha = linha-1
        final_linha = linha+2
        inicio_coluna = coluna-1
        final_coluna = coluna+tam_barco+1

        if inicio_linha<= 0:
            inicio_linha = 0
        if final_linha>10:
            final_linha = 10
        if inicio_coluna <= 0:
            inicio_coluna = 0
        if final_coluna>10:
            final_coluna = 10

        for lin in range(inicio_linha, final_linha):
            if lin == linha:
                for col in range(inicio_coluna, final_coluna, tam_barco+1):
                    if tabuleiro_pc[lin][col] != '0':
                        pode_posicionar = False
                        
            else:
                for col in range(inicio_coluna, final_coluna):
                    if tabuleiro_pc[lin][col] != '0':
                        pode_posicionar = False
                    

    elif orientacao =='v':
        inicio_linha = linha-1
        final_linha = linha+tam_barco+1
        inicio_coluna = coluna-1
        final_coluna = coluna+2

        if inicio_linha<= 0:
            inicio_linha = 0
        if final_linha>10:
            final_linha = 10
        if inicio_coluna <= 0:
            inicio_coluna = 0
        if final_coluna>10:
            final_coluna = 10
        for lin in range(inicio_linha, final_linha):
            for col in range(inicio_coluna, final_coluna):
                if col == coluna:
                    if lin < linha or lin >= final_linha:
                        if tabuleiro_pc[lin][col] != '0':
                            pode_posicionar = False
                            
                        
                else:
                    if tabuleiro_pc[lin][col] != '0':
                        pode_posicionar = False
                        
    
    return pode_posicionar            
#verifica entorno

#validando entradas
def teste_de_entrada(entrada, objeto_de_captura, intervaloi, intervalof):
    entrada = str(entrada)
    while entrada.isalpha() or (int(entrada)<intervaloi or int(entrada) >intervalof):
        entrada = input(f'\033[7mResposta inválida, tente novamente!\nLembre-se que as {objeto_de_captura} variam de {intervaloi} a {intervalof}\033[m\n\nSua Resposta: ')
    entrada = int(entrada)
    
    
    return int(entrada)
#validando entradas

#criar tabuleiro
def criar_tabuleiro(tamanho_do_tabuleiro):
    tabuleiro = []
    for c in range(TAMANHO_TABULEIRO):
        tabuleiro.append(['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
    return tabuleiro
#criar tabuleiro

#posicionar barcos do pc
def posiciona_barcos_PC(tabuleiro_PC,nome_barco, quant_barcos, tam_barco):
    while quant_barcos != 0:
        orientacao = random.choice(['h', 'v'])
        posicao_linha = random.randint(0, 10-tam_barco)
        posicao_coluna = random.randint(0, 10-tam_barco)
        while verifica_entorno(tabuleiro_PC,tam_barco,orientacao, posicao_linha, posicao_coluna) == False:
            orientacao = random.choice(['h', 'v'])
            posicao_linha = random.randint(0, 10-tam_barco)
            posicao_coluna = random.randint(0, 10-tam_barco)
        if orientacao == 'h':
            pode_posicionar = True
            for i in range(tam_barco):
                if tabuleiro_PC[posicao_linha][posicao_coluna+i] != '0':
                    pode_posicionar = False
            if pode_posicionar:
                for i in range(tam_barco):
                    tabuleiro_PC[posicao_linha][posicao_coluna + i] = nome_barco
                quant_barcos -= 1
        elif orientacao == 'v':
            pode_posicionar = True
            for i in range(tam_barco):
                if tabuleiro_PC[posicao_linha+i][posicao_coluna] != '0':
                    pode_posicionar = False
            if pode_posicionar:
                for i in range(tam_barco):
                    tabuleiro_PC[posicao_linha+i][posicao_coluna] = nome_barco
                quant_barcos -= 1
    
    return tabuleiro_PC
#posicionar barcos do pc


#preenchendo tabuleiro do usuário



def posiciona_barcos_usuario(tabuleiro,letra_barco,nome_barco, quant_barcos, tam_barco):
    while quant_barcos != 0:
        print(f'\n\nAgora, Adicione o(a) {nome_barco} , que ocupa {tam_barco} posições.')
        printar_tabuleiro(tabuleiro)
        if tam_barco>1:
            orientacao = input(f'\nEm qual orientação você deseja posicionar o(a) {nome_barco}, [H] Horizontal ou [V] Vertical?\n\nSua resposta: ').lower().strip()
            while orientacao not in ('h','v'):
                orientacao = input(f'\n\nResposta inválida! Tente novamente.\n\nEm qual orientação você deseja posicionar o(a) {nome_barco}, [H] Horizontal ou [V] Vertical?\n\nSua resposta: ').lower().strip()
        else:
            orientacao = 'h'
        posicao_linha, posicao_coluna = captura_lin_col(tam_barco,nome_barco, orientacao)
        
        while verifica_entorno(tabuleiro,tam_barco,orientacao, posicao_linha, posicao_coluna) == False:
            print('\nLembre-se que as embarcações não podem estar em posições vizinhas ou na mesma posição!\nTente novamente!\n\n')
            if tam_barco>1:
                orientacao = input(f'Em qual orientação você deseja posicionar a {nome_barco}, [H] Horizontal ou [V] Vertical?\n\nSua resposta: ').lower()
                while orientacao not in ('h','v'):
                    orientacao = input(f'\n\nResposta inválida! Tente novamente.\n\nEm qual orientação você deseja posicionar o(a) {nome_barco}, [H] Horizontal ou [V] Vertical?\n\nSua resposta: ').lower().strip()
            else:
                orientacao='h'
            posicao_linha, posicao_coluna = captura_lin_col(tam_barco,nome_barco, orientacao)
        
        if orientacao == 'h':
            pode_posicionar = True
            for i in range(tam_barco):
                if tabuleiro[posicao_linha][posicao_coluna+i] != '0':
                    pode_posicionar = False
            
            while pode_posicionar == False:
                pode_posicionar = True
                print('Este espaço já está ocupado, por favor escolha outro.\n')
                posicao_linha, posicao_coluna = captura_lin_col(tam_barco,nome_barco, orientacao)
                for i in range(tam_barco):
                    if tabuleiro[posicao_linha][posicao_coluna+i] != '0':
                        pode_posicionar = False
                while verifica_entorno(tabuleiro,tam_barco,orientacao, posicao_linha, posicao_coluna) == False:
                    print('\nLembre-se que as embarcações não podem estar em posições vizinhas ou na mesma posição!\nTente novamente!\n\n')
                    orientacao = input(f'Em qual orientação você deseja posicionar o(a) {nome_barco}, [H] Horizontal ou [V] Vertical?\n\nSua resposta: ').lower()
                    while orientacao not in ('h','v'):
                        orientacao = input(f'\n\nResposta inválida! Tente novamente.\n\nEm qual orientação você deseja posicionar o(a) {nome_barco}, [H] Horizontal ou [V] Vertical?\n\nSua resposta: ').lower().strip()
                    posicao_linha, posicao_coluna = captura_lin_col(tam_barco,nome_barco, orientacao)
                    for i in range(tam_barco):
                        if tabuleiro[posicao_linha][posicao_coluna+i] != '0':
                            pode_posicionar = False
                
            if pode_posicionar:
                for i in range(tam_barco):
                    tabuleiro[posicao_linha][posicao_coluna + i] = letra_barco
                quant_barcos -= 1


        elif orientacao == 'v':
            pode_posicionar = True
            for i in range(tam_barco):
                if tabuleiro[posicao_linha+i][posicao_coluna] != '0':
                    pode_posicionar = False
            

            while pode_posicionar == False:
                pode_posicionar = True
                print('Este espaço já está ocupado, por favor escolha outro.\n')
                posicao_linha = int(input('Em qual LINHA você deseja posicionar o submarino?\n'))
                posicao_coluna = int(input('Em qual COLUNA você deseja posicionar o submarino?\n'))
                for i in range(tam_barco):
                    if tabuleiro[posicao_linha+i][posicao_coluna] != '0':
                        pode_posicionar = False
                while verifica_entorno(tabuleiro,tam_barco,orientacao, posicao_linha, posicao_coluna) == False:
                    print('\nLembre-se que as embarcações não podem estar em posições vizinhas ou na mesma posição!\nTente novamente!\n\nSua resposta:  ')
                    orientacao = input(f'Em qual orientação você deseja posicionar o(a) {nome_barco}, [H] Horizontal ou [V] Vertical?\n\nSua resposta: ').lower()
                    posicao_linha, posicao_coluna = captura_lin_col(tam_barco,nome_barco, orientacao)
                    for i in range(tam_barco):
                        if tabuleiro[posicao_linha][posicao_coluna+i] != '0':
                            pode_posicionar = False

            if pode_posicionar:
                for i in range(tam_barco):
                    tabuleiro[posicao_linha+i][posicao_coluna] = letra_barco
                quant_barcos -= 1
    
    return tabuleiro     

#preenchendo tabuleiro do usuário
