###
# EXERCICIS
###

#Edgar Sánchez Gonzalez, 1794560, edgarsg66

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
nivell_senyal = float(input("escriu el nivell de senyal rebut (RSSI) en dbm: "))
if nivell_senyal >= -50:
    print("la cobertura es excelent")
elif nivell_senyal >= -67:
    print("la cobertura es bona")
elif nivell_senyal >= -75:
    print("la cobertura es feble")
else:
    print("la cobertura es molt feble")


# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

nivell_recepcio = float(input("escriu el nivell de recepcio en dBm: "))
if nivell_recepcio > -8:
    print("el nivell es massa alt")
elif nivell_recepcio < -27:
    print("nivell massa baix")
else:
    print("el nivell es acceptable")


# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

consum_dades = float(input("escriu el consum de dades en GB: "))
if consum_dades > 20:
    print(f"has superat el limit de dades per un total de { consum_dades - 20 }")
else:
    print("el teu consum esta dintre del limit")


# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

indicador_LOS = input("l'indicador LOS està encès? si o no?: ").strip().lower()
indicador_Internet = input("l'indicador d'Internet està encès? si o no?: ").strip().lower()
if indicador_LOS == "si":
    print("cal revisar el cable de fibra")
elif indicador_Internet == "no":
    print("comprovar el serrvei del proveidor")
else: 
    print("tot funciona correctament")


# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

percentatge_bateria = int(input("escriu el percentatge de la barteria disponible del SAI: "))

if percentatge_bateria > 100 or percentatge_bateria < 0:
    print("el percentatge de bateria esta fora del rang")
elif percentatge_bateria < 20:
    print("nivell de bateria crític")
elif percentatge_bateria < 50:
    print("nivell de bateria baix")
else:
    print("bateria suficient")


# Exercici 6: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

latencia = int(input("escriu la latencia en milisegons: "))
paq_perduts = float(input("escriu el percentatge de paquets perduts: "))

if latencia < 0:
    print("rebutjem una latencia negativa")
elif paq_perduts > 100 or paq_perduts < 0:
    print("rebutjem un percentatge fora del rang")
elif latencia <= 30 and paq_perduts <= 1:
    print("la connexio es excel·lent")
elif latencia <= 80 and paq_perduts <= 3:
    print("la connexio es bona")
elif latencia <= 150 and paq_perduts <= 5:
    print("la connexio es acceptable")
else:
    print("la connexio es deficient")


# Exercici 7: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

tipus_pla = input("Escriu el tipus de pla (bàsic o plus): ").strip().lower()
consum_mensual = float(input("Escriu el consum mensual en GB: "))

if consum_mensual < 0:
    print("Rebutjat: el consum mensual no pot ser negatiu.")
elif tipus_pla not in ("bàsic", "basic", "plus"):
    print("Rebutjat: el tipus de pla és desconegut.")
else:
    if tipus_pla in ("bàsic", "basic"):
        quota_base = 10
        limit_gb = 10
        preu_extra = 1.50
    else:
        quota_base = 20
        limit_gb = 30
        preu_extra = 0.75

    if consum_mensual > limit_gb:
        gb_extra = consum_mensual - limit_gb
        total = quota_base + (gb_extra * preu_extra)
    else:
        total = quota_base

    print(f"El preu del pla {tipus_pla} és de {total:.2f} euros.")

# Exercici 8: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

compte = input("el compte esta actiu? (si/no): ").strip().lower()
contrasenya = input("la contrassenya es correcta? (si/no): ").strip().lower()

if compte != "si":
    print("l'acces es denegat perque el compte no esta actiu")
elif contrasenya != "si":
    print("l'acces es denegat perque la contrasenya es incorrecta")
else:
    codi = input("el codi de doble verificacio es correcte? (si/no): ").strip().lower()
    if codi == "si":
        print("es permet l'acces de forma total")
    else:
        pint("l'acces es denegat perque falla el codi")


# Exercici 9: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

router = input("el router esta ences? (si/no): ").strip().lower()

if router != "si":
    print("cal encendre el router")
else:
    ind_LOS = input("l'indicador LOS esta ences? (si/no): ").strip().lower()
    ind_int_rout = input("l'ibndicador de l'internet del router esta ences? (si/no): ").strip().lower()

    if ind_LOS == "si":
        print("cal revisar el cable de fibra")
    elif ind_int_rout != "si":
        print("cal contactar amb el proveïdor")
    else:
        print("la connexió funciona correctament")


# Exercici 10: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.

incidencia = input("afecta un servei crític? (si/no): ").strip().lower()
usuaris_afectats = int(input("escriu el nombre d'usuaris afectats: "))

if usuaris_afectats < 0:
    print("es rebutja el nombre d'usuaris")
else:
    alternativa = input("Hi ha una alternativa de connexió disponible? (si/no): ").strip().lower()

    if (incidencia == "si" and alternativa != "si") or (usuaris_afectats >= 50 and alternativa != "si"):
        print("asignar prioritat crítica")
    elif usuaris_afectats >= 10 or incidencia == "si":
        print("asignar prioritat alta")
    else:
        print("asignar prioritat baixa")
