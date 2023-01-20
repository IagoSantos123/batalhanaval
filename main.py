from constantes import *
from funcoes import *


from time import sleep

# Espaço para colocar mensagem de boas vindas
print('-=-' * 30)
print(' ' * 35, '''
██████╗░░█████╗░████████╗░█████╗░██╗░░░░░██╗░░██╗░█████╗░  ███╗░░██╗░█████╗░██╗░░░██╗░█████╗░██╗░░░░░
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░██║░░██║██╔══██╗  ████╗░██║██╔══██╗██║░░░██║██╔══██╗██║░░░░░
██████╦╝███████║░░░██║░░░███████║██║░░░░░███████║███████║  ██╔██╗██║███████║╚██╗░██╔╝███████║██║░░░░░
██╔══██╗██╔══██║░░░██║░░░██╔══██║██║░░░░░██╔══██║██╔══██║  ██║╚████║██╔══██║░╚████╔╝░██╔══██║██║░░░░░
██████╦╝██║░░██║░░░██║░░░██║░░██║███████╗██║░░██║██║░░██║  ██║░╚███║██║░░██║░░╚██╔╝░░██║░░██║███████╗
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝''')
print('-=-' * 30)
# Espaço para colocar mensagem de boas vindas


#ESPAÇO PARA MENU
while True:
    resposta = input('\n[1]. Começar o jogo\n[2]. Manual\n[3]. Creditos\n\nSua Resposta: ')
    while resposta.isnumeric() == False or int(resposta)<1 or int(resposta)>3:
        resposta = input('\nResposta inválida. Tente novamente!\n\n[1]. Começar o jogo\n[2]. Manual\n[3]. Creditos\n\nSua Resposta: ')
    resposta = int(resposta)
    
    

    if resposta == 1:
        break
    
    elif resposta == 2:
        print('\n\nBem vindo ao Batalha Naval!\nNovo por aqui? sem problemas, vou te ensinar como jogar este jogo!')
        print('\n1. Este é um jogo de tabuleiro, em que o objetivo principal é afundar TODAS as embarcações inimigas, acertando a posições das mesmas.')
        print('\n2. O tabuleiro tem tamanho 10 X 10 e o usuário deve posicionar as suas embarcações nesse espaço.')
        print(f'\n3. O usuário tem a sua disposição 10 embarcações, sendo:\n        4 {SUBMARINO_ESCRITO} (ocupando 1 casa)\n        3 {CORVETA_ESCRITO} (ocupando 2 casas)\n        2 {ENCOURACADO_ESCRITO} (ocupando 3 casas)\n        1 {PORTA_AVIOES_ESCRITO} (ocupando 4 casas)\n\n')
    elif resposta == 3:
        print('\nEste jogo foi desenvolvido por IAGO LUCENA e GUSTAVO ATAIDE\npara o projeto da disciplina: LABORATÓRIO DE ALGORITMOS E PROGRAMAÇÃO\n do primeiro periodo do curso de ENGENHARIA DE COMPUTAÇÃO do IFPB.\n')
#ESPAÇO PARA MENU


# criar tabuleiro
tabuleiro_usuario = criar_tabuleiro(TAMANHO_TABULEIRO)
tabuleiro_PC = criar_tabuleiro(TAMANHO_TABULEIRO)
tabuleiro_PC_para_o_usuario = criar_tabuleiro(TAMANHO_TABULEIRO)
# criar tabuleiro


#preencher o tabuleiro da maquina
posiciona_barcos_PC(tabuleiro_PC, PORTA_AVIOES, portaavioes_pc,TAMANHO_PORTAAVIOES)
posiciona_barcos_PC(tabuleiro_PC,ENCOURACADO, encouracados_pc, TAMANHO_ENCOURACADOS)
posiciona_barcos_PC(tabuleiro_PC, CORVETA, corveta_pc, TAMANHO_CORVETA)
posiciona_barcos_PC(tabuleiro_PC, SUBMARINO, submarinos_pc, TAMANHO_SUBMARINO)


#preencher o tabuleiro do usuário
#preencher_tabuleiro_usuario(submarino_possiveis_usuario,corveta_possiveis_usuario,encouracados_possiveis_usuario,portaavioes_possiveis_usuario,tabuleiro_usuario)
posiciona_barcos_usuario(tabuleiro_usuario,PORTA_AVIOES,PORTA_AVIOES_ESCRITO,portaavioes_usuario,TAMANHO_PORTAAVIOES)
posiciona_barcos_usuario(tabuleiro_usuario,ENCOURACADO,ENCOURACADO_ESCRITO,encouracados_usuario,TAMANHO_ENCOURACADOS)
posiciona_barcos_usuario(tabuleiro_usuario,CORVETA,CORVETA_ESCRITO,corveta_usuario,TAMANHO_CORVETA)
posiciona_barcos_usuario(tabuleiro_usuario,SUBMARINO,SUBMARINO_ESCRITO,submarino_usuario,TAMANHO_SUBMARINO)


#JOGADAS
print('\n\n\033[1;33mHORA DE JOGAR!\n\nComeçando em:', end=' ')
for c in range(3,0,-1):
    sleep(1)
    print(f'{c}...', end=' ')
print('\033[m')


tiro, linha, coluna = jogada_aleatoria(tabuleiro_usuario)
tabuleiro_PC, tabuleiro_PC_para_o_usuario = jogada_usuario(tabuleiro_PC, tabuleiro_PC_para_o_usuario)

while total_embarcacoes_pc>0 and total_embarcacoes_usuario>0:
    while tiro == '0':
        if total_embarcacoes_pc ==0:
            break
        print('\n\n\033[7mPC NÃO ATINGIU NADA\033[m\n')
        print('\nTABULEIRO DO USUARIO')
        printar_tabuleiro(tabuleiro_usuario)
        tiro, linha, coluna = jogada_aleatoria(tabuleiro_usuario)
        tabuleiro_PC, tabuleiro_PC_mostrar = jogada_usuario(tabuleiro_PC, tabuleiro_PC_para_o_usuario)

    if tiro == SUBMARINO:
        if total_embarcacoes_pc ==0:
            break
        print(f'\n\033[7mPC ATINGIU {SUBMARINO_ESCRITO}\033[m')
        
        tabuleiro_usuario[linha][coluna] = f'\033[41mX\033[m'
        print('\nTABULEIRO DO USUARIO')
        printar_tabuleiro(tabuleiro_usuario)
        total_embarcacoes_usuario-=1
        tabuleiro_PC, tabuleiro_PC_mostrar = jogada_usuario(tabuleiro_PC, tabuleiro_PC_para_o_usuario)
        
        tiro, linha, coluna = jogada_aleatoria(tabuleiro_usuario)

    elif tiro == CORVETA or tiro == ENCOURACADO or tiro == PORTA_AVIOES:
        if total_embarcacoes_pc ==0:
            break
        tabuleiro, orientacao = continua_pra_esquerda(tabuleiro_usuario, tiro, linha, coluna,tabuleiro_PC, tabuleiro_PC_para_o_usuario)
        if orientacao == 'h':
            tabuleiro, orientacao = continua_pra_direita(tabuleiro, tiro, linha, coluna, tabuleiro_PC, tabuleiro_PC_para_o_usuario)
        else:
            tabuleiro, orientacao = continua_pra_baixo(tabuleiro, tiro, linha, coluna,tabuleiro_PC, tabuleiro_PC_para_o_usuario)    
            tabuleiro, orientacao = continua_pra_cima(tabuleiro, tiro, linha, coluna,tabuleiro_PC, tabuleiro_PC_para_o_usuario)
            
        total_embarcacoes_usuario-=1
            

        tiro, linha, coluna = jogada_aleatoria(tabuleiro_usuario)
        
    else:
        if total_embarcacoes_pc ==0:
            break
        tiro, linha, coluna = jogada_aleatoria(tabuleiro_usuario)

        if tiro!='0':
            print(f'\n\033[7mPC ATINGIU {tiro}\033[m')
            tabuleiro_usuario[linha][coluna] = f'\033[41mX\033[m'
            print('\nTABULEIRO DO USUARIO')
            printar_tabuleiro(tabuleiro_usuario)
            
        else:
            print(f'PC atirou na podição [{linha}][{coluna}] e errou.')
            print('\nTABULEIRO DO USUARIO')
            printar_tabuleiro(tabuleiro_usuario)
        #
        #
        tabuleiro_PC, tabuleiro_PC_mostrar = jogada_usuario(tabuleiro_PC, tabuleiro_PC_para_o_usuario)
    
#JOGADAS

if total_casas_pc>0:
    print(f'\n\n\033[0;32;40mFim de jogo, o PC destruiu todas as embarcações inimigas\033[m')
elif total_casas_usuario>0:
    print(f'\n\n\033[0;32;40mFim de jogo, o USUÁRIO destruiu todas as embarcações inimigas\033[m')