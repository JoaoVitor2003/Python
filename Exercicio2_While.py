#Exercício 2
nota1 = float(input("Insira a nota 1: "))
nota2 = float(input("Insira a nota 2: "))


while nota1 <= 0 or nota1 >= 10:
    
    nota1 = float(input("Insira uma nota válida entre 0 e 10: "))

while nota2 <= 0 or nota2 >= 10:

    nota2 = float(input("Insira uma nota válida entre 0 e 10: "))

nota_final = (nota1 + nota2) / 2
print(f"A média é: {nota_final:.1f}")
    
