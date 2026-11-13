###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
index= 10

while index >= 1:
    print(index)
    index -= 1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while. 
index = 1
suma_parells = 0

while index <= 20:
    if index % 2 == 0:
        suma_parells += index
    index += 1

print(f"la suma de tots els mombres parells entre el 1 i el 20 es: {suma_parells}")


# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
numero= int(input("escriu un numero enter positiu: "))
calcul_fact = 1
index = 1
while index <= numero:
    calcul_fact *= numero
    index += 1
print(f"el factorial de {numero} es: {calcul_fact}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
contra=input("escriu una contrasenya de almenys 8 caracters: ")

while len(contra) < 8:
    contra= input("la contrasenya no es valida, tora a escriurela: ")

print("Contrasenya vàlida")


# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
numero=int(input("escriu un numero: "))
index = 1
result_multip = 1

while index <= 10:
    result_multip = index * numero
    print (f" {numero} * {index} = {result_multip}")
    index += 1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
n = int(input("Introdueix un número enter positiu N: "))

numero = 2
while numero <= n:
  es_primer = True  
  divisor = 2
  while divisor * divisor <= numero:  
    if numero % divisor == 0:
      es_primer = False  
      break  
    divisor += 1
  if es_primer:
    print(numero)

  numero += 1