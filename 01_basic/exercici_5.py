###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
nom_tecnic = input("introdueix el nom del tecnic: ")
nom_xarxa = input(introdueix el nom de la xarxa: ")
print(f"Tenim un tecnic que es diu {nom_tecnic} i una xarxa que es diu {nom_xarxa}")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud_enllaç_km = float(input("introduir longitud del enllaç en km: "))
velocitat_transmissio = float(input("escriu la velocitat de transmissio: "))
print(f"el temps en transetre 1 Gb de dades es de: {(8 / velocitat_transmissio) * 1000} segons")



# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
Hores_feina = float(input("escriu el nombre de hores de feina: "))
preu_hora = float(input("escriu el preu per hora: "))
preu_material = float(input("escriu el preu del material: "))

cost_total = preu_material + (Hores_feina * preu_hora)
print(f"el cost total de la obra es de: {cost_total}")
