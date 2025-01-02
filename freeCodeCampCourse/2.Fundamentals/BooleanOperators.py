# operatori logici o booleani

condizione1 = True
condizione2 = False

print("condizione1 senza operatori logici =",condizione1)
# operatore NOT, nega il valore ricevuto, esempio:
condizione1 = not condizione1 # assegno a condizione1 il nuovo valore booleano "negato" tramite l'operatore logico NOT
print("condizione1 con operatore logico NOT =",condizione1)

condizione1 = True # ripristino "condizione1" al suo status originario "True", essendo stato negato dall'operatore NOT

# quando si ha l'operatore logico AND, tutte le variabili devono avere condizione Vera per generare come risultato Vero o 1
operatoreAND = condizione1 and condizione2 # effettuo l'operazione dell'algebra di Boole con l'operatore AND
print("Operazione logica AND su True e False =",operatoreAND)
# quando si ha l'operatore logico OR, basta che una sola delle variabili abbia valore 1 o condizione Vera per dare come risultato il valore Vero
operatoreOR = condizione1 or condizione2 # effettuo l'operazione dell'algebra di Boole con l'operatore OR
print("Operazione logica OR su True e False =",operatoreOR)

# una caratteristica dell'operatore OR (utilizzato con or o |) è che utilizzerà SEMPRE il primo valore "Vero" se presente, 
# altrimenti utilizzerà il secondo valore sia che sia "Vero" o "Falso"
# ecco alcuni esempi:

print("OPERATORE LOGICO OR")
print(True or False) # stamperà il valore True essendo come primo valore Vero
print(False or True) # stamperà il valore True essendo il primo valore False appunto Falso
print(0 or 1) # stamperà il valore 1 essendo il primo valore 0
print(False or "Ciao") # stamperà Ciao essendo il primo valore Falso
print("Buongiorno" or "Ciao") # stamperà Buongiorno essendo, come primo valore, positivo
print([] or False) # stamperà False essendo "[]" considerato vuoto e quindi falso
print(False or []) # stamperà [] essendo il primo valore Falso

# l'operatore logico AND (utilizzato con and o &) considererà il secondo valore SOLO SE il primo verrà identificato come Vero
# dunque se il primo valore sarà Falso restituirà questo come output; se il primo valore sarà Vero, resituirà il secondo come risultato che sia Vero o no

print("OPERATORE LOGICO AND")
print(True and False) # stamperà il valore False essendo il primo valore Vero
print(False and True) # stamperà il valore False essendo il primo valore False
print(0 and 1) # stamperà il valore 0 essendo il primo valore Falso
print(False and "Ciao") # stamperà il valore False essendo il primo valore False
print("Buongiorno" and "Ciao") # stamperà Ciao essendo il primo valore Vero
print([] and False) # stamperà [] essendo come primo valore vuoto e dunque Falso
print(False and []) # stamperà False essendo come primo valore Falso