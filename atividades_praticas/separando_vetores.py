numeros = [0] * 10
pares = []
impares = []

for i in range(10):
    numeros[i] = int(input('Digite os números: '))

for valor in numeros:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print('Números pares: {}'.format(pares))
print('Números ímpares: {}'.format(impares))
