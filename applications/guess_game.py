#Give 3 chances to the user to guess a number 
lucky_number = 9
guess_limit = 3
guess_number = 1

while guess_number <= guess_limit:
    guess = int(input('Guess a number: '))
    if guess == lucky_number:
        print('You won!')
        break
    else:
        if guess_number == guess_limit:
            print('Better luck next time!')
            break
        print('Try again!')
    guess_number += 1

print('\nThanks for playing!')