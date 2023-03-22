# %%
a=[18,20,21,21,19,22,24,17]

promedio = sum(a) / len(a)

print("El promedio es: [", promedio,"]")



def moda(dataset):
    frequency = {}

    for value in dataset:
        frequency[value] = frequency.get(value, 0) + 1

    most_frequent = max(frequency.values())

    moda = [key for key, value in frequency.items()
                      if value == most_frequent]

    return moda
print("La moda es:", moda(a))

desviacion = (sum((x - promedio) ** 2 for x in a) / (len(a) - 1)) ** 0.5
print("La desviación es: [", desviacion,"]")
print("hola")
#hola