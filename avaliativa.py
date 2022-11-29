'''Uma loja utiliza o código V para transação à vista e P para transação a prazo. Faça um programa que receba o código e o valor de quinze transações, calcule e mostre:
a. O valor total das compras à vista;
b. O valor total das compras à prazo;
c. O valor total das compras efetuadas;
d. O valor da primeira prestação das compras a prazo juntas, sabendo-se que serão pagas em três vezes;
e. O maior valor entre todas as compras a prazo;  
f. O menor valor entre todas as compras a vista;'''
valtotal = 0
valtotalv = 0
valtotalp = 0
valtotparcela = 0
maiorvalorp= 0
menorvalorv = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
for compra in range(4):
    print ('Digite o código da compra V= A vista e P= A prazo')
    codigo = input()
    print ("Digite o valor da compra")
    valor = int(input())
    parcela = valor/3
    valtotal = valtotal + valor
    for bla in range(1):
        if codigo == "p"or codigo == "P":
            valtotparcela = valtotparcela + parcela  
            valtotalp = valtotalp + valor
            if valor > maiorvalorp:
                maiorvalorp = valor
        if codigo == "v" or codigo == "V":
                valtotalv = valtotalv + valor
                if valor < menorvalorv:
                    menorvalorv = valor
print ('A soma das compras a vista é de: R$', valtotalv)
print ('A soma das compras a Prazo é de:R$', valtotalp )
print ('valor total das compras é de:R$', valtotal)
print ('O valor da primeira prestação das compras a prazo juntas é de:R$: R$', valtotparcela)
print ("O maior valor entre todas as compras a prazo é de: R$", maiorvalorp)
print ('O menor valor entre todas as compras a vista é de: R$', menorvalorv)

'''professor, eu usei o numero exorbitante pra ser comparado com o valor pra saber qual
 a menor compra a vista, pq não me lembrei a logica por tras do outro modo. Eu podia so 
 copiar mas como não entendi a logica usei esse geito ai msm '''