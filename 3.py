'''3. A série de Fibonacci é formada pela seguinte sequência: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, etc.
 Escreva um algoritmo que gere a série de Fibonacci até o vigésimo termo. '''

numero1 = 1
numero2 = 1

for i in range (3, 21):
    prox_numero = numero1 + numero2
    print(prox_numero)
    numero1 = numero2
    numero2 = prox_numero


 