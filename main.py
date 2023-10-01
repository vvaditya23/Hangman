import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
#print(chosen_word)
display = []
won = False
guess = ""
lives = 0
player_won = False

chosen_count = len(chosen_word)
for _ in range(chosen_count):
  display.append("_")

print(hangman_art.logo)
  #Join all the elements in the list and turn it into a String.
print(f"{' '.join(display)}")

while not player_won:

  guess = input("\nGuess the letter: ").lower()

  if guess in display:
        print(f"You have already entered {guess}.")
    
  for index, alphabet in enumerate(chosen_word):
    if alphabet == guess:
      display[index] = guess
  
  if guess not in chosen_word:
    print(f"You guessed {guess}, it wrong. You lost a life!")
    lives += 1
    print(hangman_art.stages[lives - 1])
    if lives == 7:
      print("You loose!")
      print(f"The word was: {chosen_word}")
      break
  print(f"{' '.join(display)}")

  if not "_" in display:
    player_won = True
    print("You won!")
