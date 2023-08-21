numero = int(input('Digite um número para ver seu fatorial: '))
fatorial = 1
for fat in range(1, numero + 1):
    fatorial *= fat
print(f'O fatorial de {numero} é {fatorial}.')
