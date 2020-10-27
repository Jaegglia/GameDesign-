#self made game number 1

gamewords={'lemonade','milk','soda','water','juice','koolaid','wine','kombucha','tea'}

def intro():
    print('Welcome to the scramble game\n')
    print('I will show you a scrambled word, and you will have to guess the word\n')

#this is to shuffle the word
def shuffle_word():
    wordKey = random.choice(list(gamewords.keys()))
    return wordKey

def getAnswer():
    answer = input('\nEnter your first guess: ')
    while True:
            if answer.isalpha():
                return answer
            else:
                answer = input('\nEnter a letter: ')

def keepPlaying():
    iContinue = input("\nWould you like to keep playing? ")
    return iContinue

def scramble():
    theList = list(shuffle_word())
    random.shuffle(theList)
    return(''.join(theList))

if keepPlaying() == 'y':
    intro()
    shuffle_word()
    randomW = shuffle_word()
    #scramKey = list(randomW)
    thisWord = scramble()
    print ("\nThe scrambled word is " +thisWord)
    solution = getAnswer()
    if solution == thisWord:
        print("\nCongratulations")
else:
    print("\nThanks for playing")
