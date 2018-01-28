import  random
choises = ["rock", "paper", "scissors"]
print("instuctions: rock beats scissors, scissors beats paper, and paper beats rock.")
player = raw_input("wanna be rock, paper, or scissors? or press q to quit\n")
while player != "q":
    player = player.lower()
    computer = random.choice(choises)
    print("you choose " + player + " and computer choose " + computer + ".")
    if player == computer:
        print("its a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("you win!")
        else:
            print("computer wins!")
    elif player == "scissors":
        if computer == "paper":
            print("you win!")
        else:
            print("computer wins!")
    elif player == "paper":
        if computer == "rock":
            print("you win!")
        else:
            print("computer wins!")

    elif player != (choises):
        print("I think there is an error...")
        print()
    player = raw_input("wanna be rock, paper, or scissors?\n")


