import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
========''', '''


  +---+
  |   |
  O   |
      |
      |
      |
========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========''','''
  +---+
  |   |
 [O   |
 /|\  |
 / \  |
      |
========''','''
  +---+
  |   |
 [O]  |
 /|\  |
 / \  |
      |
========''']
words = {'Animals':'ant babboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog'
         'goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven'
         'rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),
         'Shapes':'square triangle rectangle circle ellipse rhombus trapazoid pentagon hexagon octogon'.split(),
         'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalope mango strawberry kiwi'.split(),
         'Colours':'red orange yellow green blue indigo violet white black brown purple pink'.split(),
         'Programming languages': 'python c objectivec php java javascript basic pascal delphi erlang fortran haskell machinecode ruby visualbasic'.split()}

def getRandomWord(wordDict):
    #This function returns a random string from the passed dictionary of lists of strings along with the dictionary key
    #randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))
    #Then randomly select a word from the key's list in the dictionary
    wordIndex = random.randint(0, len(wordDict[wordKey]) -1)
    return [wordDict[wordKey] [wordIndex], wordKey]
    

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks [i+1:]

    for letter in blanks: #show the secret word with spaces in between each letter
        print(letter, end=' ')
        print()

    print('Your clue: Think of ' +secretKey)

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) !=1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that leter. Please choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter.')
        else:
            return guess

def playAgain():
    #this function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord, secretKey = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

   
    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord +'"! You have won!')
            gameIsDone = True
    else:
            missedLetters = missedLetters + guess
            #Check if player has guessed too many times and lost
           
                  
            if len(missedLetters) == len(HANGMANPICS) - 1:
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print ('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord, secretKey = getRandomWord(words)
            else:
                break
                
              
    
                
        
