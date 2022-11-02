print("---CALCULADORA IMC---")
peso=float(input("cual es tu peso"))
altura=int(input("cual es tu altura"))
altura= altura/100
imc= peso/(altura*altura)
print("su imc es de "+str(imc))
if imc <20:
    print("estas en estado de delgadez")
if imc>=20 and imc<26:
    print(" estas en estado normal")
if imc>=26 and imc<30:
    print("Estas en un estado de sobrepeso")
if imc>=30:
    print("estas en un estado de obesidad")
