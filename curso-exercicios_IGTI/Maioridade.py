
idade =int( input("Digite a sua idade:  "))
print(idade)
if idade > 18 and idade < 69:
    print("voce está liberado, pode dirigir")
elif idade < 18:
    print("voce é de menor, espere completar 18")
elif idade >= 70:
    print("voce deve procurar o Detran")