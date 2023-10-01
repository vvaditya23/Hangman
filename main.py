import random

word_list = ["aardvark", "baboon", "aabb"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
won = False
guess = ""

chosen_count = len(chosen_word)
for _ in range(chosen_count):
  display.append("_")
print(display)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while "_" in display:
  guess = input("Guess the letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

  for index, alphabet in enumerate(chosen_word):
    if alphabet == guess:
      display[index] = guess
    else:
      print("Wrong!")
    
  print(display)

print("You won!")
