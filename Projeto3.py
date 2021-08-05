c = 0
while True:
    t = int(input('Digite um valor inteiro para saber sua tabuada: '))
    if t < 0:
        break
    while c < 10:
        c += 1
        print(f'{t} * {c} = {t*c}')
    c = 0
print('Programa encerrado')
