# very super simple blackjack that isn't really... great
# made following https://www.youtube.com/watch?v=yJz2at4Hco4

import random

player = []
dealer = []

while len(dealer) != 2:
    dealer.append(random.randint(1, 11))
    if len(dealer) == 2:
        print("Dealer has: X and", dealer[1])

while len(player) != 2:
    player.append(random.randint(1, 11))
    if len(player) == 2:
        print("You have ", player)

if sum(dealer) == 21:
    print("Dealer blackjack!")
elif sum(dealer) > 21:
    print("Dealer busted!")

while sum(player) < 21:
    action = str(input("Do you want to stay or hit? "))
    if action == "hit":
        player.append(random.randint(1,11))
        print("You have a total of " + str(sum(player)) + " from these cards ", player)
    else:
        print("The dealer has a total of " + str(sum(dealer)) + " with ", dealer)
        print("You have a total of " + str(sum(player)) + " from these cards ", player)
    if sum(dealer) > sum(player):
        print("Dealer wins!")
    else:
        print("You win!")
        break

if sum(player) > 21:
    print("You busted! Lose!")
elif sum(player) == 21:
    print("Blackjack! You win!")
