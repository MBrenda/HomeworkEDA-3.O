#modulo de python que genera numeros aleatorios
import random

tamanio = 4
num = ('0','1','2','3','4','5','6','7','8','9')
num_ale = random.choice(num)
#print (num_ale)
cifra='' 

for i in range(tamanio):
    while num_ale in cifra:
        num_ale = random.choice(num)
    cifra = cifra + num_ale
    #print ('cifra=', cifra)

print ('Hola ADIVINADOR tienes que acertar el numero de', tamanio, 'cifras que estoy pensando')
num_adivinador = input('Adivinador:')
#print('Adivinador:', num_adivinador) 

while len(num_adivinador) != len(cifra):
    print("Numero invalido, ingrese otro numero de", tamanio, "cifras")
    num_adivinador = input(":")

while num_adivinador != cifra:
    orden_igual = 0
    num_igual = 0
        
    for i in range(tamanio):
        if num_adivinador[i] == cifra[i]:
            orden_igual = orden_igual + 1
        elif num_adivinador[i] in cifra:
            num_igual = num_igual + 1
    
    print ('Pensador: respuesta', orden_igual, 'bien,', num_igual, 'regular')
    print('Estan en el lugar correcto:', orden_igual, 'Estan en el lugar incorrecto:' , num_igual)
    num_adivinador = input("Intenta de nuevo: ")

print ("------------------¡JUEGO TERMINADO!------------------")
