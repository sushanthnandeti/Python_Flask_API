magic_number = 12 

while True: 

    user_input = input('Do you want to play the game?').lower()

    if user_input == 'n':
        break

    number = int(input('Enter the number to crack the game!'))

    if number == magic_number:
        print('You got it! Congrats')
    
    elif abs(magic_number - number) == 1:
        print('You were off by one. Try again, you are very close')

    else: 
        print('OOPS! Not good')


