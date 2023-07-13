import math

#Calculo de IMC

peso = float(input('Ingrese su peso en kg'))
altura = float(input('Ingrese su estatura en metros'))

print(peso)
print(altura)

IMC = round(peso/math.pow(altura, 2), 2)

print('Su Indice de Masa Corporal es de ' + str(IMC))