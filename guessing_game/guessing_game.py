import random
level = raw_input("enter in a level, easy, medium, hard, or extreme\n")
if level == "easy":
    the_number = random.randint(1,10)
    guess = int(raw_input("guess a number between 1 and 10\n"))
    counter = 0
    while guess != the_number and counter < 2:
        counter = counter + 1
        if guess > the_number:
            print guess, "was too high, guess again!"
        elif guess < the_number:
            print guess, "was too low, guess again!"
        guess = int(raw_input("guess again:\n"))
    if guess == the_number:
        print guess, "is the right number! Conrats!"
    else:
        print "You lose game over! The number is:", the_number


elif level == "medium":
    the_number = random.randint(1,50)
    guess = int(raw_input("guess a number between 1 and 50\n"))
    counter = 0
    while guess != the_number and counter < 4:
        counter = counter + 1
        if guess > the_number:
            print guess, "was too high, guess again!"
        elif guess < the_number:
            print guess, "was too low, guess again!"
        guess = int(raw_input("guess again:\n"))
    if guess == the_number:
        print guess, "is the right number! Conrats!"
    else:
        print "You lose game over! The number is:", the_number


elif level == "hard":
    the_number = random.randint(1,100)
    guess = int(raw_input("guess a number between 1 and 100\n"))
    counter = 0
    while guess != the_number and counter < 5:
        counter = counter + 1
        if guess > the_number:
            print guess, "was too high, guess again!"
        elif guess < the_number:
            print guess, "was too low, guess again!"
        guess = int(raw_input("guess again:\n"))
    if guess == the_number:
        print guess, "is the right number! Conrats!"
    else:
        print "You lose game over! The number is:", the_number



elif level == "extreme":
    the_number = random.randint(1,1000)
    guess = int(raw_input("guess a number between 1 and 1000\n"))
    counter = 0
    while guess != the_number and counter < 7:
        counter = counter + 1
        if guess > the_number:
            print guess, "was too high, guess again!"
        elif guess < the_number:
            print guess, "was too low, guess again!"
        guess = int(raw_input("guess again:\n"))
    if guess == the_number:
        print guess, "is the right number! Conrats!"
    else:
      print "You lose game over! The number is:", the_number
