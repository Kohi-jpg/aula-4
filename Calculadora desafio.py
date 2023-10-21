def calculadora():
    operacao = int(input('Escolha o calculo\n 1: Soma\n 2: Subtração\n 3: Multiplicação\n 4: Divisão\n 5: Comparação\n'))
    x = float(input('Escolha o primeiro número\n'))
    y = float(input('Escolha o segundo Número\n'))
    
    som = x + y
    sub = x - y
    mul = x * y
    div = x / y

    if operacao == 1:
        print(f'O resultado é: {som}')
    elif operacao == 2:
        print(f'O resultado é: {sub}')
    elif operacao == 3:
        print(f'O resultado é: {mul}')
    elif operacao == 4:
        if y == 0:
            print(f'é impossível dividir qualquer número por 0')
        else:
            print(f'O resultado é: {div}')
    elif operacao == 5:
        if x == y:
            print(f'O número {x} igual a {y}')
        elif x <= y:
            print(f'O número {x} é menor que {y}')
        elif x >= y:
            print(f'O número {x} é maior que {y}')
    else:
        print('opção invalida')

calculadora()