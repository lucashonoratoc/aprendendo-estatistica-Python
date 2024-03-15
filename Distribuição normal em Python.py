from scipy.stats import norm

# Conjunto de objetos numa cesta, a média é 8 e o desvio padrão é 2
# Qual a probalidade de tirar um objeto que peso é menor que 6 kgs?


norm.cdf(6, 8, 2)


# Qual a probabilidade de tirar um objeto que o peso é maior que 6 kgs?

norm.sf(6, 8, 2)

# OU 

1- norm.cdf(6, 8, 2)

# Qual a probabilidade de tirar um objeto que o peso é menor que 6 kgs ou
# maior que 10 kgs?

norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)


# Qual a probabilidade de tirar um objeto menor que 10 e maior que 8 quilos?

norm.cdf(10, 8, 2) - norm.cdf(8, 8, 2)
