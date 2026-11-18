n1 = float(input("donner le premier nombre: "))
op = input("donner une opération (+, -, *, / ,**): ").strip()
n2 = float(input("donner le deuxième nombre: "))

if op == "+":
    print("Réponse:", n1 + n2)
elif op == "-":
    print("Réponse:", n1 - n2)
elif op == "**":
    print("Réponse:", n1 ** n2)
elif op == "*":
    print("Réponse:", n1 * n2)
elif op == "/":
    if n2 != 0:
        print("Réponse:", n1 / n2)
    else:
        print("Division par zéro impossible.")
else :
    print("opération inconnue")
