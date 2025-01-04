# alcuni esempi di stringhe

"Marco" # è possibile dichiarare una stringa con le virgolette "stringa"
'Marco' # oppure è anche possibile dichiarare una stringa con gli apici singoli 'stringa'

nome = "Marco" # è possibile assegnare una stringa ad una variabile
frase = "Marco" + " è il mio nome" # le stringhe possono essere concatenate con l'operatore + ed assegnate ad una variabile
frase2 = nome + " è il mio nome" # è inoltre possibile concatenare un'altra variabile con una stringa
nome += " è il mio nome" # con questa tipologia di formulazione è possibile aggiungere una stringa alla fine del testo già esistente in una variabile, aggiornandone il contenuto

# è possibile stampare delle stringhe su più righe, adottando il seguente metodo:
print("""Marco ha

32 anni
      
si sta laureando in ignegneria informatica

e sta imparando il linguaggio Python

""")

# le stringhe hanno anche dei "metodi" che ci permettono di modificare il testo, esempio:

print("mArCo".upper()) # con questo metodo è possibile stampare tutto il testo in maiuscolo
print("MarCO".lower()) # con questo metodo è possibile stampare tutto il testo in minuscolo
print("mArco andrIOla".title()) # questo metodo renderà la prima lettera di ogni parola maiuscola ed il resto del testo minuscolo

# ci sono anche metodi che permettono di effettuare delle verifiche sul testo
print("MarCO".islower()) # questo metodo permette di verificare se il testo sia tutto minuscolo, e restituirà un output booleano (True o False)

# NOTA: il metodo è applicato alla relativa funzione che lo chiama, e non sovrascrive il contenuto della variabile chiamata, esempio:

print(nome.lower()) # eseguendo il codice si può notare che la prima lettera del nome è minuscola
print(nome) # eseguendo successivamente questa istruzione si nota che il nome ha nuovamente la prima lettera maiuscola

# nella documentazione ufficiale è possibile trovare tutti i metodi disponibili

età = 32
print(str(età)) # è utile ricordare che un valore, ad esempio intero, può essere convertito in stringa

# un altro controllo che può essere effettuato su una stringa è il controllo del numero di caratteri presenti, esempio:

print(len(nome)) # con questo comando verrà stampato il numero di caratteri presenti, spazi inclusi

# sarà altresì possibile verificare il contenuto di testo nel testo, ovvero la presenza di una "sottostringa" nella "stringa", esempio:

print("rc" in nome) # questa istruzione restituirà un output booleano verificando la presenza della stringa antecedente "in" nella stringa/variabile successiva

nome = "Ma\"rco" # è utile notare che utilizzando il "backslash" è possibile aggiungere le virgolette in una stringa, senza incorrere in errore di compilazione
print(nome)

nome = "marco\nsi sta laureando\nin ingegneria informatica\na febbraio" # mentre in questo caso è possibile utilizzare "backslash" seguito da "n" per mandare il testo a capo
print(nome.title())

nome = "Marco"
print(nome[1]) # attraverso l'utilizzo di questo indice si potrà stampare il carattere n°1 presente in lista. La numerazione parte da 0
# dunque nell'esempio corrente, M = 0, a = 1, ecc. 
print(nome[-1]) # sarà inoltre possibile partire da "-1", quindi M = 0, o = -1, c = -2, ecc.
print(nome[1:3]) # infine sarà possibile operare su un range di caratteri, separato dai due punti tra parentesi quadre
# NOTA: quando si utilizza il "range" l'ultimo carattere presente nell'indice non sarà compreso.
# nell'esempio utilizzato verranno stampati gli indici 1 e 2, ovvero le lettere "ar" escludendo la "c"
# è inoltre possibile lasciare vuoto lo spazio antecedente i due punti o lo spazio successivo, indicando così un punto di fine o un punto di partenza