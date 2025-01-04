# dichiarazione di un "if" standard
def è_maggiorenne(age):
    if age >= 18:
        return True
    else:
        return False
    
# esempio di operatore ternario
def è_maggiorenne2(age):
    return True if age >= 18 else False

# l'operatore ternario dunque comprime la medesima situazione precedente in un'unica riga