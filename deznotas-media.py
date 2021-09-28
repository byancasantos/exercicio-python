soma = 0
nota=0
cont=1
while cont <11:
    nota = float(input('Qual a sua '+str(cont)+'º nota? '))
    soma = soma+ nota
    cont = cont +1
media = soma/10
print('Sua média é:',media)
