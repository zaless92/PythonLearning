attivitàCompletata = True # quando si utilizzano gli operatori Booleani è importante indicarli con la prima lettera MAIUSCOLA

# un esempio per le condizioni nelle istruzioni "if"

if attivitàCompletata: # in questo caso la variabile è indicata come "True" dunque sarà verificata la prima condizione e stampata la risposta "Si"
    print("si".title())
else:
    print("no".title())

# una cosa da considerare è che:
# se anzichè "False" scrivessi "0", questo verrebbe interpretato come Falso
# se dovessi scrivere qualsiasi altro valore, anche "-1" o "10", questi sarebbero sempre interpretati come Vero
# le stringhe sono "False" solo quando sono vuote, altrimenti saranno sempre "True"

libro_1_letto = True
libro_2_letto = False

# in questo caso la funzione "any" verificherà la lista, nello specifico se almeno un valore sia Vero, e restituirà "True"
libri_letti = any([libro_1_letto, libro_2_letto])
print(libri_letti)

ingredienti_acquistati = True
cibo_cucinato = False

# in questo caso, invece, la funzione "all" verificherà che tutti i valori siano "True" e restituirà il valore corrispondente, "True" o "False"
pronto_per_servire = all([ingredienti_acquistati, cibo_cucinato])
print(pronto_per_servire)