c = float(input('Valor do saldo inicial R$: '))
time = float(input('Tempo de rendimento (meses): '))
fees = float(input('Taxa de juros (a.m): '))

result = c * (1 + fees / 100) ** time

print('O valor final será de: ', round(result, 2))
