cont=0
somador=0
while cont<4:
     cont = cont + 1
     nota = float(input('Digite a ' + str(cont)+'º nota:'))
     somador = somador + nota
     print ('Soma atual das notas:', somador)
media = somador /4
print('A sua media é',media)
