'''Programa que calcule el indice de masa corporal (IMC)de una persona
 peso / estatura
IMC             CLASIFICACION
-----------------------------------
< 18.5          bajo peso
18.5 - 24.9     normal
25.0 - 29.9     sobrepeso
30.0 - 34.9     obesidad 1
35.0 - 39.9     obesidad 2
40.0 - 49.9     obesidad 3 
> 50.0          obesidad 4
----------------------------------
IMC = peso / (estatura* estatura)
'''

def calculadoraIMC(p, e):  # siendo p = peso / e = estatura
    return p/ (e**2)

def clasificacion(IMC):
    if IMC < 18.5 :
        return "Bajo peso"
    elif 18.5 <=IMC <=  24.9:
        return "Normal"
    elif 25.0 <= IMC <= 29.9:
        return "Sobrepeso" 
    elif 30.0 <= IMC <=  34.9:
        return "Obesidad 1"
    elif 35.0 <= IMC <= 39.9: 
        return "Obesidad 2"
    elif 40.0 <= IMC <= 49.9:
        return "Obesidad 3" 
    else:
        return "obesidad 4"


    

peso = float ( input("ingrese su peso en Kilos (kg) ejemplo 45: "))
estatura = float( input("ingrese su altura en Metros (m) ejemplo 1.70 : "))

input(print( "el resultado de su indice de masa corporal (IMC) indica que usted se encuentra: ", clasificacion(calculadoraIMC(peso, estatura))))


