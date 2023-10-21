#Faça um cardapio com os seguintes itens Pizza | Macarronada | Lanche
#Faça um cardapio com os seguintes itens Água | Refri | Vinho

comida = input('Escolha entre:\n 1 Pizza\n 2 Macarronada\n 3 Lanche\n')
bebida = input('Escolha entre:\n 1 Água\n 2 Refri\n Vinho\n')

def com(x):
    if comida == 1:
        return x('Pizza')
    elif comida == 2:
        return x('Macarronada')
    elif comida == 3:
        return x('Lanche')
    else:
        return 'Nenhum'
    
def beb(x):
    if comida == 1:
        return x('Água')
    elif comida == 2:
        return x('Refri')
    elif comida == 3:
        return x('Vinho')
    else:
        return 'Nenhum'
    
print()
