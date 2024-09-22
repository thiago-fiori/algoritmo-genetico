# Parâmetros
POP_SIZE = 20
BIT_SIZE = 64
MUTATION_CHANCE = 0.01
CROSSOVER_CUT_POINTS = 2
SELECTION_STRATEGY = "ROULETTE" # pode ser trocado por "TOURNAMENT"
INF_LIMIT = -10
SUP_LIMIT = 10
TOURNAMENT_SIZE = 5
ELITISM_PERCENTAGE = 0.1 # 0 para nao usar
MAX_GENERATIONS = 10

#Função para mapear array de 0/1 e converter pra um real dentro de um intervalo
MAX_VALUE = 2**BIT_SIZE - 1
SLICE = (SUP_LIMIT - INF_LIMIT) / MAX_VALUE

def f(x):
    return x**3 - 6*x + 14