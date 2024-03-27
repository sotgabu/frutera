import os

def limpar():
    os.system("cls")

limpar()
produtos = ["morango","maracujá","Limão","Lima","Abacate","uva","carambola","melancia","abacaxi"]
compra = []
precos = [7.0,13.0,2.0,5.0,4.0,10.0,90.0,2.0,10.0]
desc = 0.15
soma = 0

escolha = int(input("Você que desconto?\n1.Sim\n2.Não\nR:"))
limpar()
if escolha == 1:
    for i in range(len(produtos)):
        precos[i] *= (100 - desc)/100

for i in range(len(produtos)):
    print(i+1,"º produto",produtos[i]," custa R$ ",round(precos[i],2))

compra = list(map(int,input("Quais produtos você gostaria de comprar? Escreva o número referente ao produto separado por espaço.\n").split(" ")))
for i  in range(len(compra)):
    compra[i] = produtos[compra[i]-1]
limpar() 
print("Seu Carrinho:\n")

for i in range(len(compra)):
    print(produtos.index(compra[i])+1,"º produto",compra[i]," custa R$ ",round(precos[produtos.index(compra[i])],2))

for i in range(len(compra)):
    soma+= round(precos[produtos.index(compra[i])])
print("\n Seu total é: ",soma)
