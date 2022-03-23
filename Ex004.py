#Faça um programa que leia algo pelo teclado e mostre 
#na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
random=input('Digite algo: ')
print('Tipo primitivo desse valor é: {}'.format(type(random)))
print('É um número? {}.'.format(random.isnumeric()))
print('É alfabético? {}.'.format(random.isalpha()))
print('É alfanumérico? {}.'.format(random.isalnum()))
print('Só tem espaços? {}.'.format(random.isspace()))
print('Está capitalizada? {}.'.format(random.istitle()))
print('Está em maiúsculas? {}.'.format(random.isupper()))
print('Está em minúsculas? {}.'.format(random.islower()))