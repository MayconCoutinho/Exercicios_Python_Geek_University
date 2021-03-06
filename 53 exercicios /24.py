# Leia um valor de área metros quadrados m² e apresente-o convertido em acres. A 
# fórmula de conversão é: A = M * 0,000247, sendo M a área em metros quadrados e A
# a área em acres 


M = int(input('Digite o valor em metros quadrados m² para converte em acres: '))
A = M*0.000247
print('{0} metros quadrados = {1} acres'.format(M,A))