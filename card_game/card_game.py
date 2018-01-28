import random
cards = 40
your_point_tracker = 0
oponents_point_tracker = 0
suits = ["hearts", "spades", "dimonds", "clubs"]
card = ["two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "jack", "queen", "king", "ace"]
print("Classic card game: War: type in draw to draw a card, anyone who has a more powerful card, wins the match.\n"
      " Whoever has the most wins at the end, wins!")
draw = raw_input("enter draw to draw\n")
while draw == "draw" and cards > 0:
    my_type = random.choice(suits)
    my_card_value = random.choice(card)
    oponent_type = random.choice(suits)
    oponent_card_value = random.choice(card)
    print"you drew:", my_type, "of", my_card_value
    print"your oponent drew:",  oponent_type, "of", oponent_card_value
    if card.index(my_card_value) > card.index(oponent_card_value):
        print("you score a point!")
        your_point_tracker + 1
        cards = cards - 2
    if card.index(my_card_value) < card.index(oponent_card_value):
        print("your oponent gained a point!\n")
        oponents_point_tracker + 1
        cards = cards - 2
    if card.index(my_card_value) == card.index(oponent_card_value):
        print("its a tie!")
        cards = cards - 2
    if cards == 0:
        print("game over!\n cauclulating points...")
        if oponents_point_tracker > your_point_tracker:
            print("your oponent wins!")
        elif your_point_tracker > oponents_point_tracker:
            print("you win!")
        elif your_point_tracker == oponents_point_tracker:
            print("its a tie!")
    else:
        draw = raw_input("enter draw to draw again\n")
else:
    print("i think there is an errerÅÅ")