nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome em maiúsculo é {}' .format(nome.upper()))
print('Seu nome em minúsculo é {}' .format(nome.lower()))
print('Seu nome ao todo tem {} letras' .format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))



