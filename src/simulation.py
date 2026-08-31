import random


def simulate_two_dice():
    """Simula o lançamento de dois dados e retorna a soma."""

    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)

    return die_1 + die_2


def run_simulation(iterations):
    """Executa a simulação várias vezes."""

    results = []

    for _ in range(iterations):
        result = simulate_two_dice()
        results.append(result)

    return results


# Executa 10.000 simulações
results = run_simulation(10000)

# Exibe os primeiros resultados
print(results[:10])

# Calcula a média
average = sum(results) / len(results)

print(f"Average: {average}")