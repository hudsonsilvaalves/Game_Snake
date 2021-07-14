trabalho = input('Voce deve trabalhar hoje? ')
dia = input('O dia esta bonito? ')
preguica = input('voce esta com preguiça? ')

if trabalho == 'sim':
    print('E uma pena')
elif trabalho == 'não':
    print('Aproveite o dia')

if dia == 'sim' and trabalho == 'não':
     print('Aproveite para caminhar')
elif dia == 'não' and trabalho == 'não':
    print('Aproveite e assista um filme')

if preguica == 'sim' and trabalho == 'não':
     print('Aproveite para dormir mais')
elif preguica == 'não' and trabalho == 'não':
    print('vamos estudar python!')