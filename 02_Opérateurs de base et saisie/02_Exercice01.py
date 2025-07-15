
# Demander deux nombres
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

# Calculs
somme = a + b
différence = a - b
produit = a * b
quotient = a / b if b != 0 else "Division par zéro"
division_entiere = a // b if b != 0 else "Division par zéro"
reste = a % b if b != 0 else "Division par zéro"

# Affichage des résultats
print(f"Somme : {somme}")
print(f"Différence : {différence}")  
print(f"Produit : {produit}")
print(f"Quotient : {quotient}")
print(f"Division entière : {division_entiere}")
print(f"Reste : {reste}")