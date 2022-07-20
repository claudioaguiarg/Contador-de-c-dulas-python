print('='*40)
print('{:^40}'.format('BANCO LADRÃO'))
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
