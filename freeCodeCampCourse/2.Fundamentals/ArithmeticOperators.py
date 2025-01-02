# operatori aritmetici
somma = 3 + 2 ; print("Somma 3 + 2 =",somma) # 5
sommaNumNegativo = 3 + -3 ; print("Somma con numero negativo 3 + -3 =",sommaNumNegativo) # 0
sottrazione = 3 - 2 ; print("Sottrazione 3 - 2 =",sottrazione) # 1
moltiplicazione = 2 * 3 ; print("Moltiplicazione 3 * 2 =",moltiplicazione) # 6
divisione = 11 / 5 ; print("Divisione 11 / 5 =",divisione) # 2.2
resto = 5 % 3 ; print("Resto 5 % 3 =",resto) # 2
potenza = 5 ** 2 ; print("Potenza 5 ** 2 =",potenza) # 25
divisioneInteroPrecedente = 11 // 5 ; print("Intero precedente della divisione 11 // 5 =", divisioneInteroPrecedente) # 2

# gli operatori aritmetici possono essere combinati con l'operatore di assegnazione, esempio:
peso = 65
peso += 7 # peso = peso + 7
print("Peso += 7kg =",peso)
peso -= 22 # 50
print("Peso -= 22kg =",peso)
peso *= 1.5 # 75.0
print("Peso *= 1.5",int(peso)) # peso uguale a 75 anzichè 75.0 forzando la variabile stampata come "int" anzichè "float"