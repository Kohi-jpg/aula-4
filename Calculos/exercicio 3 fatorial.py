num = int(input('Digite um numero:\n'))
fat = int(input('Digite o fatorial:\n'))
reajuste = fat + 1

for fat in range(1,reajuste):
    resultado = fat[-1] * num
    print(resultado)