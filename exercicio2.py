#Faça um programa que o usuário insira 10 produtos numa tupla. 
#Exiba todos os produtos, solicite ao usuário para digitar um nome de produto e exiba a posição dele,
#em seguida peça para digitar número entre 0 e 9 e exiba o produto da tupla.
print("Isabella Carolina de Souza")
pdt= ()
adcionar_pdt= list(pdt)
for i in range(10):
    pdt = input("Qual produto você deseja inserir? ")
    adcionar_pdt.append(pdt)
    pdt = tuple(adcionar_pdt)
print(pdt)
nome = input("Qual produto você deseja inserir? ")

if nome in pdt:
    for i in range(len(pdt)):
        if pdt[i] == nome:
            print(i)
else:
    print("Esse produto não foi cadastrado!")

num = int(input("Digite um numero entre 0 e 9: "))
print(pdt(num))
