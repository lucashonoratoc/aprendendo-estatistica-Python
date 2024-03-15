from scipy.stats import binom


# Probabilidade de dar cara 3x
prob = binom.pmf(3, 5, 0.5)


# Passar por 4 sinais de 4 tempos e pegar o sinal verde
# nenhuma, 1, 2, 3, 4 vezes.
binom.pmf(0, 4, 0.25)
binom.pmf(1, 4, 0.25)
binom.pmf(2, 4, 0.25)
binom.pmf(3, 4, 0.25)
binom.pmf(4, 4, 0.25)

# E se forem sinais de 2 tempos
binom.pmf(4, 4, 0.5)

# Probabilidade cumulativa
binom.cdf(4, 4, 0.25)


# Concurso com 12 questões, qual a probabilidade de acertar 7 questões considerando
# cada questão tem 4 alternativas
binom.pmf(7, 12, 0.25) * 100

binom.pmf(12, 12, 0.25) * 100