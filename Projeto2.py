from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    print(f'jogador {jogador}')
    print(f'computador {computador}')
    total = jogador + computador
    print('Total '+ str(total))
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar?: [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. total {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Ganhou!!')
            v += 1
        else:
            print('Você Perdeu!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Ganhou!!')
            v += 1
        else:
            print('Você Perdeu!!')
            break
        print('Vamos jogar Novamente!?: ')
print(f'GAME OVE! Você venceu {v} vezes!')






