import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from config import *

def binary_to_real(binary_vector):
    # Converte o vetor binário para um número inteiro
    integer_value = int(''.join(map(str, binary_vector)), 2)
    MAX_VALUE = 2**BIT_SIZE - 1
    SLICE = (SUP_LIMIT - INF_LIMIT) / MAX_VALUE
    return INF_LIMIT + SLICE * integer_value

def plot_function_with_markers(fn, x_range, num_points, markers, title='Plot of f(x)', ax=None):
    # Função de criação e definição da função e dos pontos no gráfico
    if ax is None:
        ax = plt.gca()

    x = np.linspace(x_range[0], x_range[1], num_points)
    y = fn(x)

    ax.clear()  # Clear the previous plot
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.grid(True)

    for x_marker in markers:
        y_marker = fn(x_marker)
        ax.plot(x_marker, y_marker, 'ro')

    return ax

def create_animation(fn, x_range, num_points, population_history, interval=1000, filename='evolution.gif'):
    fig, ax = plt.subplots(figsize=(10, 6))
    # Função de criação da animação .gif para visualizar os indivíduos de cada geração no gráfico

    def update(frame):
        markers = population_history[frame]
        plot_function_with_markers(fn, x_range, num_points, markers, f'Generation {frame}', ax)

    anim = FuncAnimation(fig, update, frames=len(population_history), interval=interval, repeat=False)
    anim.save(filename, writer='pillow')
    plt.close(fig)


def fitness(x):
    real_x = binary_to_real(x) # Necessário fazer essa conversão, já que o indivíduo está codificado em bits
    return f(real_x) * (-1) # Invertemos pois, quanto menor o valor, melhor