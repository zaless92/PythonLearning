
# importo la libreria "random" per gestire un output casuale
import random

def game():
  # definisco la funzione delle scelte per il giocatore ed il computer
  def get_choices():
    # definisco la funzione input con un messaggio per il giocatore
    player_choice = input("Digita la tua scelta (Roccia, Carta, Forbici): ")
    # definisco una lista di stringhe per la scelta casuale del computer
    randomChoices = ["Roccia", "Carta", "Forbici"]
    # assegno la variabile di scelta del computer chiamando la funzione random.choice della lista randomChoices
    computer_choice = random.choice(randomChoices)
    # definisco un dizionario con le scelte del giocatore e del computer
    choices = {"player": player_choice, "computer": computer_choice}
    # restituisco il dizionario con le variabili generate durante l'esecuzione della funzione
    return choices

  # definisco la funzione per verificare l'esito delle scelte del giocatore e del computer
  def check_win(player, computer):
    # concateno più stringhe da stampare con il segno +
    # oppure aggiungo una f prima delle virgolette e le variabili tra parentesi graffe chiudendo le virgolette alla fine
    # così facendo posso evitare di utilizzare il segno + molteplici volte
    print(f"Tu hai scelto  {player}, il computer ha scelto {computer}")
    if player == computer:
      return "Pareggio!"
    # anzichè utilizzare una serie di "elif" verificando le scelte del giocatore e del computer tramite "and"
    # è possibile verificare la scelta del giocatore ed utilizzare degli "if" annidati ed "else"
    # se l'"if" iniziale restituirà "pareggio", il codice successivo non verrà eseguito
    elif player == "Roccia":
      if computer == "Forbici":
        return "La Roccia rompe le Forbici! Hai Vinto!"
      else:
        return "La Carta copre la Roccia! Hai Perso!"
    elif player == "Carta":
      if computer == "Roccia":
        return "La Carta copre la Roccia! Hai Vinto!"
      else:
        return "Le Forbici tagliano la Carta! Hai Perso!"
    elif player == "Forbici":
      if computer == "Carta":
        return "Le Forbici tagliano la Carta! Hai Vinto!"
      else:
        return "La Roccia rompe le Forbici! Hai Perso!"
  
  # chiamo la funzione get_choices per generare l'output choices da stampare successivamente
  choices = get_choices()
  result = check_win(choices["player"], choices["computer"])
  print(result)

# chiamo la funzione game in loop per lasciare il gioco in esecuzione
while True:
  game()