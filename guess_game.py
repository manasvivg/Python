print 'this program can guess a number you think'
top = input('What is the maximum number possible in the game: ')
bottom = input('What is the minimum number possible in the game: ')

print 'Please think of a Number between ' + str(bottom) + ' and ' + str(top)
guess = bottom + (top-bottom)/2
ans = ''
direction = ''
while ans != 'y':
    print 'Is your number ' + str(guess) + ' (y/n)'
    ans = raw_input()

    if ans == 'y':
        print 'I am the guessing god!!!! bow down to me!!'
    else:
        direction = raw_input('Is your number lower or higher (l/h)')

    if direction == 'l':
        top = guess
        guess = bottom + ((guess-bottom)/2)


    if direction == 'h':
        bottom = guess
        guess = guess + (top-guess)/2
