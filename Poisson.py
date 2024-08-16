import math

print("---------------------CALCULADORA DE PROBABILIDADE POISSON---------------------\n")

l = float(input("Qual é a média de ocorrência (λ)? "))
k = int(input("Qual é o valor desejado (K)? "))
a = int(input("O valor desejado (K) é acumulado (1- SIM | 2 - NÃO)? "))



resultadototal = 0
while a != 1 and a != 2:
    print("Valor digitado incorretamente")
    a = int(input("O valor desejado (K) é acumulado (1- SIM | 2 - NÃO)? "))


if a == 2:
    base1 = 2.71828182845904523536028747135266249
    expo1 = -(l)
    e_l = math.pow(base1, expo1)

    base2 = l
    expo2 = k
    l_k = math.pow(base2, expo2)

    partedecima = e_l * l_k
    partedebaixo = math.factorial(k)
    resultado = (partedecima / partedebaixo) * 100
    print("O resultado dessa Probabilidade Poisson é : %.2f%%" % (resultado))
else:
    for i in range (k, -1, -1):
        base1 = 2.71828182845904523536028747135266249
        expo1 = -(l)
        e_l = math.pow(base1, expo1)

        base2 = l
        expo2 = i
        l_i = math.pow(base2, expo2)
        partedecima = e_l * l_i
        partedebaixo = math.factorial(i)
        resultado = (partedecima / partedebaixo) * 100
        resultadototal = resultadototal + resultado
    print("O resultado dessa Probabilidade Poisson é : %.2f%%" % (resultadototal))
        
wait = input("")
    
    
