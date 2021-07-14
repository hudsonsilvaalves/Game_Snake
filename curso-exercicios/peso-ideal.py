altura = float(input('Entre com sua altura:'))
peso = float(input('Entre com seu peso:'))
imc = peso/(altura * altura)
print('Seu índice de massa corporal é {:.2f}'.format(imc))
if imc < 18:
      print('Você está muito magro')
elif imc >= 18 and imc <=24:
     print('Você está com peso ideal')
elif imc > 24:
    print('Você está precisando se exercitar')