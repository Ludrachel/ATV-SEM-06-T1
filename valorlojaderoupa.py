def compra(valor):
    valor = valor - (valor*9/100)
    return valor
def compra_2(valor_2):
    valor_2 = valor_2/5
    return valor_2
def compra_3(valor_3):
    valor_3 = (valor_3 + (valor_3 *17/100))/10
    return valor_3
preco = float(input())
print(f'{compra(preco):1.2f}')
print(f'{compra_2(preco):1.2f}')
print(f'{compra_3(preco):1.2f}')
    
