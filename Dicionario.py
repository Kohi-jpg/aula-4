sinonimos = my_dict = {
    'fogo' : 'Brasa',
    'margem' : 'Borda',
    'comida' : 'Alimento',
    'felino' : 'Gato',
    'premio' : 'Premiação'
}

resultante = input('Digite uma palavra:\n')
if resultante in sinonimos:
    i = sinonimos[resultante]
    print(f'A palavra {resultante} é semelhante a {i}')
else:
    print('essa palavra não existe no dicionario')