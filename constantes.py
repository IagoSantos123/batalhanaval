

# TAMANHO DAS EMBARCAÇOES
TAMANHO_SUBMARINO = 1
TAMANHO_CORVETA = 2
TAMANHO_ENCOURACADOS = 3
TAMANHO_PORTAAVIOES = 4

# TAMANHO DA MATRIZ
TAMANHO_TABULEIRO = 10
# Navios possíveis
submarino_possiveis_usuario = submarinos_possiveis_pc = 4
corveta_possiveis_usuario = corveta_possiveis_pc = 3
encouracados_possiveis_usuario = encouracados_possiveis_pc = 2
portaavioes_possiveis_usuario = portaavioes_possiveis_pc = 1
lista_jogadas = []
# Navios possíveis

#Representação das embarcações com cores
SUBMARINO = '\033[0;33mS\033[m'
SUBMARINO_ESCRITO = '\033[0;33mSubmarino\033[m'
CORVETA = '\033[0;32mC\033[m'
CORVETA_ESCRITO = '\033[0;32mCorveta\033[m'
ENCOURACADO = '\033[0;35mE\033[m'
ENCOURACADO_ESCRITO = '\033[0;35mEncouraçado\033[m'
PORTA_AVIOES = '\033[0;31mP\033[m'
PORTA_AVIOES_ESCRITO = '\033[0;31mPorta_aviões\033[m'
#Representação das embarcações com cores

#Embarcações dos usuários
submarino_usuario = submarinos_pc = 4
corveta_usuario = corveta_pc = 3
encouracados_usuario = encouracados_pc = 2
portaavioes_usuario = portaavioes_pc = 1
total_embarcacoes_usuario = total_embarcacoes_pc = 10

#Casas ocupadas
CASAS_SUBMARINO = TAMANHO_SUBMARINO * submarino_possiveis_usuario
CASAS_CORVETA = TAMANHO_CORVETA * corveta_possiveis_usuario
CASAS_ENCOURACADO = TAMANHO_ENCOURACADOS * encouracados_possiveis_usuario
CASAS_PORTAAVIOES = TAMANHO_PORTAAVIOES * portaavioes_possiveis_usuario
total_casas_pc = total_casas_usuario = CASAS_SUBMARINO + CASAS_CORVETA + CASAS_ENCOURACADO + CASAS_PORTAAVIOES

print((100*0.15)+(100*0.15)+(100*0.15)+(100*0.15)+(80*0.4))