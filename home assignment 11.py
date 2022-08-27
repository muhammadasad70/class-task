import random
card_rank=['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
card_suit=['Clubs', 'Diamonds', 'Hearts', 'Spades']
card=random.choice(card_rank)
card1=random.choice(card_suit)
print("The card you picked is the",card,"of",card1)