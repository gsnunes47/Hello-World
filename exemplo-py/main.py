def fat(n):
    fatorial = 1
    for fat in range(1, numero + 1):
        fatorial *= fat
    return fatorial


numero = int(input('Digite um número para ver seu fatorial: '))
print(f"O fatorial de {numero} é {fat(numero)}.")
