import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
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
      |
      |
=========
''', '''
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
  |   |
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
      |
      |
      |
      |
=========
''']



display=[]
word_len = len(chosen_word)
for lett in range(word_len):
    display += '_'

endgame=False
livestime = 6

while not endgame:

    guess = input("Guess a letter: ").lower()
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position]= letter
        else:
            display = display


    if guess not in chosen_word:
        hangman = stages[livestime]
        print(hangman)
        livestime -= 1
        if livestime == 0 :
            end_of_game=True
            print('you lose')




    guess_word = ""

    for item in display:
        guess_word += item 

    if '_' not in display:
        endgame=True
        print('you win')

    print(guess_word)