print('='*40)
print('{:^40}'.format('Contador de Cédulas'))
print('='*40)
valor = int(input('Digite o valor a ser sacado: '))
nota50 = nota20 = nota10 = nota01 = 0
while valor >= 50:
    valor -= 50
    nota50 += 1
if nota50 != 0:
    print(f'Total de {nota50} cédulas de R$50')
while valor >= 20:
    valor -= 20
    nota20 += 1
if nota20 != 0:
    print(f'Total de {nota20} cédulas de R$20')
while valor >= 10:
    valor -= 10
    nota10 += 1
if nota10 != 0:
    print(f'Total de {nota10} cédulas de R$10')
while valor >= 1:
    valor -= 1
    nota01 += 1
if nota01 != 0:
    print(f'Total de {nota01} cédulas de R$1')

''' SISTEMA NOVO EM CONSTRUÇÃO
r = (int(input('Cédula número um')),int(input('Cédula número dois')),int(input('Cédula número três')))
valor = int(input('Valor '))
c1 = c2 = c3 = 0

while valor >= r[0]:
    valor -= r[0]
    c1 += 1
if c1 != 0:
    print(f'Total de {c1} notas de {r[0]}')'''