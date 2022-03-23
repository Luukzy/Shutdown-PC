#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
n=int(input('Digite um número: '))
sucessor=n+1
antecessor=n-1
print('O sucessor do número {} é igual a {}.'.format(n, sucessor))
print('O antecessor do número {} é igual a {}.'.format(n, antecessor))