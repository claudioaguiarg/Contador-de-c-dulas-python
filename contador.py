ced = []
ced2 = [0]
tip = int(input('Quantos tipos de cédulas terão?'))

for cont in range(1,tip+1):
    ced.append(int(input(f'Digite o valor da {cont}º cédula: ')))
ced.sort(reverse=True)

for c in range (0,tip):
    ced2.append(0)
valor = int(input('Valor a ser sacado: '))
for z in range(0,tip):
    while valor >= ced[z]:
        valor -= ced[z]
        ced2[z] += 1
    if ced2[z] != 0:
        print(f'Total de {ced2[z]} cédulas de R${ced[z]}')