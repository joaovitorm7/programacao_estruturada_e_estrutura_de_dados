mediaAnual = [0] * 3
mediaTurma = 0
soma = 0

for i in range(3):
    mediaAnual = float(input('Nota {}: '.format(i + 1)))
    soma += mediaAnual

mediaTurma = (soma/3)
print('Média da turma: {:.2f} '.format(mediaTurma))