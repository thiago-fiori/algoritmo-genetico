from genetic_algorithm import new_population, evolve
from utils import binary_to_real, create_animation
from config import INF_LIMIT, SUP_LIMIT, f, POP_SIZE, MAX_GENERATIONS


def main():
    population_history = []

    start_pop = new_population(POP_SIZE)
    real_values = [binary_to_real(x) for x in start_pop]
    population_history.append(real_values)

    current_pop = start_pop
    for gen in range(MAX_GENERATIONS):
        current_pop = evolve(current_pop)  # Evolve for one generation
        real_values = [binary_to_real(x) for x in current_pop]
        population_history.append(real_values)
        best = sorted(real_values)[0]

        print(f"Generation {gen + 1}:")
        print(f"Melhor indivíduo: {best}")

    create_animation(f, (INF_LIMIT - 10, SUP_LIMIT + 10), 400, population_history, interval=500,
                     filename='evolution.gif')


if __name__ == "__main__":
    main()