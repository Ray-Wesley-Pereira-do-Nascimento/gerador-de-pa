print('Gerador de PA')
print('=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
quant = 0
mais = 10
while mais != 0:
    quant += mais
    while cont <= quant:
        print(f'{termo} ->', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais vc quer ver? '))
    while cont <= (quant):
        print(f'{termo} ->', end='')
        termo += razao
        cont += 1
print('FIM')
