#modulo de python que genera numeros aleatorios
import random

tamanio = 4
num = ('0','1','2','3','4','5','6','7','8','9')
num_ale = random.choice(num)
print (num_ale)
cifra='' 

for i in range(tamanio):
    while num_ale in cifra:
        num_ale = random.choice(num)
    cifra = cifra + num_ale
    print ('cifra=', cifra)

print ('Hola ADIVINADOR tienes que acertar el numero de', tamanio, 'cifras que estoy pensando')
num_adivinador = input('Adivinador:')
print('Adivinador:', num_adivinador) 