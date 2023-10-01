import random

word_list = ["aardvark", "baboon", "aabb"]

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',  '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
won = False
guess = ""
lives = 0
player_won = False

chosen_count = len(chosen_word)
for _ in range(chosen_count):
  display.append("_")
  #Join all the elements in the list and turn it into a String.
print(f"{' '.join(display)}")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#while "_" in display:
while not player_won:
  
  guess = input("Guess the letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

  for index, alphabet in enumerate(chosen_word):
    if alphabet == guess:
      display[index] = guess

  if guess not in chosen_word:
    lives += 1
    print(stages[lives - 1])
    if lives == 7:
      print("You loose!")
      break
  print(f"{' '.join(display)}")

  if not "_" in display:
    player_won = True
    print("You won!")
