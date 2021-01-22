# Spaces
minsp = 0
maxsp = 500

# Admin's configuration
print("Hey Admin!")
sw = str(input("Make up a word : "))
guesses = float(input("How many guesses should the user have : "))
h = str(input("Do you want to give the user a hint? y/n : "))

guess = ''
gc = 0

# Admin's hint
if h == 'y':
    hint = str(input("What hint do you wanna give to the user, when the user type down \'Hint\' : "))
elif h == 'n':
    hint = str("I didn\'t give you a hint.")

# Spaces - So user can't see what the admin did.
while minsp != maxsp:
    print("")
    minsp = minsp + 1

print("Hey User!")

# The game starts here.
while guess != sw or gc != guesses:
    guess = str(input("Enter a guess : "))
    
    gc = gc + 1
    
    # Events during/end the game.
    if guess == sw:
        print("You win!")
        exit()
    elif guess == 'Np =>':
        print("You know something that nobody else knows!")
        gc = gc - 1
    elif guess == 'Amazing Grace':
        print("Alan Jackson!")
        gc = gc - 1
    elif guess == 'Hint' or guess == 'hint':
        print("Admin > " + str(hint))
    elif guess == 'GCount' or guess == 'gcount':
        print(str(gc) + "/" + str(guesses))
        gc = gc - 1
    elif gc == guesses:
        print("You lose!")
        exit()

