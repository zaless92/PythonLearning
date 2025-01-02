# python è un linguaggio dinamico, capirà la tipologia (classe) della variabile automaticamente. Ecco alcuni esempi:
name = "Marco" # questa è una stringa
print(type(name)) # questo comando mostrerà la tipologia della variabile (o classe)
print(type(name) == str) # questo comando mostrerà se è vero o falso che la variabile sia effettivamente una stringa
print(isinstance(name, str)) # questo comando mostrerà se è vero o falso che la variabile sia effettivamente quella posta successivamente alla virgola
age = 32 # questo è un intero
print(isinstance(age, float)) # questo comando resituirà "False" come output, essendo il valore di "age" un intero e non un valore in virgola
age = float(32) # in questo modo è possibile forzare una variabile ad essere riconosciuta come di altro tipo
print(isinstance(age, float)) # questo comando resituirà "True" avendo forzato la variabile "age" come float (o valore in virgola)
bodyTemperature = 36.8 # questo è un valore in virgola mobile "float"
print(isinstance(bodyTemperature, float)) # questo comando restituirà "True", essendo il valore "bodyTemperature" in virgola
daughtersNames = ["Giulia", "Ilaria"] # questo potrebbe essere considerato come un array, contenendo elementi dello stesso tipo (python non ha array a livello nativo, ma liste)
giuliasData = ["Giulia", 5, 1.2] # questa è una lista, contenendo elementi di tipo diverso
giuliasData2 = {"name": "Giulia" , "age": 5 , "height": 1.2} # questo è un dizionario, avendo a sinistra la "chiave" e dopo i due punti il "valore"

# non tutte le parole possono essere utilizzate come "variabili", utilizzare parole come "if", "for", "while", ecc. genererebbe un errore di sintassi

# è possibile scrivere più istruzioni (statements) sulla stessa riga, inserendo un "; (semicolon)" tra le varie istruzioni
# questa tipologia di scrittura permette di utilizzare un solo rigo per dichiarare più variabili, magari dello stesso soggetto, mantenendo ordine e leggibilità
dogName = "Ryuu" ; dogAge = 6 ; dogHeightAtNeckInCm = 71 ; print("Dog Name:",dogName,"Dog Age:",dogAge,"Dog Height at neck (cm):",dogHeightAtNeckInCm)
