#Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida,
#exibir o número de índice (ou seja, posição na lista) desse item na tupla.
print("Isabella Carolina de Souza")
paises = ('brasil','chile','venezuela','espanha','EUA')
print(paises)
digite_pais = (input("Digite um país: "))
if digite_pais in paises:
    ind = paises.index(digite_pais)
    print("O indice do pais é: ", ind)
else: 
    print("Pais este pais nao esta registrado")