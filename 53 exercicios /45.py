# Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tavela 
# ASCII para resover o problema.


'''letra = str(input('Digite a letra em maiúscula para converte em minúscula: '))
converte = chr(ord(letra)-32)
print(converte)''' # Um modo de converte letras por numero de tabela 


letra_minuscula = str(input('Digite em letras minúsculas para converte em letras maiúscula: '))
print(letra_minuscula.swapcase())