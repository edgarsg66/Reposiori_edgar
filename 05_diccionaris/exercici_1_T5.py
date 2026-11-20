# Exercici 1: Crear un diccionari
estudiant = {
  "nom": "Edgar",
  "edat": 19,
  "fruita_fav": ["poma", "platan", "kiwi"]
}
print(estudiant)

# Exercici 2: Accedir i modificar
print(estudiant["fruita_fav"][1])  
estudiant["edat"] = 25
print(estudiant["edat"])

# Exercici 3: Afegir i eliminar
estudiant["grau"] = "Enginyeria de Sistemes de Telecomunicació"
del estudiant["edat"]
print(estudiant)

# Exercici 4: Comprovar claus
print("nom" in estudiant)    
print("email" in estudiant)  #

# Exercici 5: Recórrer un diccionari
for clau, valor in estudiant.items():
  print(f"{clau}: {valor}")

# Exercici 6: Comptar paraules
paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
recompte = {}
for paraula in paraules:
  if paraula in recompte:
    recompte[paraula] += 1
  else:
    recompte[paraula] = 1
print(recompte)  