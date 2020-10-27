import random
import time



name=input("What is your name? ")
print("Good luck! ", name)
gameWords=['apple', 'pie','banana','coffee', 'donut', 'bagel', 'candy','tortilla', 'pizza', 'burger','hot dog' ]

answer=input('do you want to guess a type of food ')



while answer == 'yes':
    word= random.choice(gameWords)
    guesses =''
    turns=10
    while turns>0:
        for char in word:
            if char in guesses:
                print(char)
            else:
                print('_',end='')
        guess= input("give me a letter: ")
        guesses += guess
        turns-=1
    


    answer=input('do you want to play again ')
time.sleep(5)

    
    
