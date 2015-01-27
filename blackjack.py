# Game of Blackjack

# Simplified Rules (10 pts possible):
# - Human player gets the first two cards
# - Human player plays the rest of their hand
# - Then computer gets next two cards
# - Computer must take cards score >= 17
# - Computer must stand when score >= 17
# - Aces always count as 11
# - Human player loses if their score is > 21
# - Computer loses if computer score is > 21
# - Human player wins immediately if their score is exactly 21
# - Computer wins immediately if their score is exactly 21
# - If computer score is betwen 17 and 20, winner is determined by score
# - If it's a tie, nobody wins.

# Grading:
# - 5 points for allowing a human user to play their complete hand
# - 5 points for allowing the computer to play its hand

# (Optional) Extras
# [You don't get extra credit for these, but they're fun.]
# - 1. Aces should count as 1 if counting as 11 would have made the score > 21
# - 2. Initally, human and dealer both get two cards; one dealer card is face up
# - 3. Allow the user to play as many games as they want
# - 4. Dealing cards to the cmputer should have a dramatic, 4-second delay

# Here's the psuedocode we wrote on the board in class:

## Get a deck of cards

## Shuffle the deck

## Deal the first two cards to user

## User can choose to take cards as long as score < 21

## If user goes over 21, game is over.

## If user reaches 21, game is over.

## If user stands with less than 21, then it's the dealer's turn:

## Computer takes two cards
## Computer must take more cards while computer score < 17
## If computer score reached 21, computer wins.
## If computer score goes over 21, computer loses.
## If computer score is 17 to 20, winner is determined by higher score.import random


import random

suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
faces =  ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = []

for i in suits:
	for j in faces:
		deck.append(j+i)

random.shuffle(deck)

def card_scores(cards):
	scores = 0
	for card in cards:
		if card[0] in ["J", "Q", "K"]:
			score = 10
		elif card[0] == "A":
			score = 11
		else:
			score = int(card[:-1])
		scores = scores + score
	return scores

#player got two cards
your_hand = [deck.pop(0), deck.pop(1)]
your_scores = card_scores(your_hand)

print("You have:", "".join(your_hand))
print("Your scores are", your_scores)

#dealer got two cards
dealer_hand = [deck.pop(0), deck.pop(1)]
dealer_scores = card_scores(dealer_hand)

#play game
while your_scores < 21 and input("Take another card? (y/n): ") == 'y':
	your_hand.append(deck.pop(0))
	your_scores = card_scores(your_hand)
	print("You have:","".join(your_hand))
	print("Your scores are", your_scores)
	
if your_scores == 21:
	print("Blackjack! You won!")

elif your_scores > 21:
	print("You were busted. You lost!")

else:
	while dealer_scores < 17:
		dealer_hand.append(deck.pop(0))
		dealer_scores = card_scores(dealer_hand)

	if dealer_scores == 21:
		print("Dealer got Blackjack! You lost!")
		print("Dealer has:", "".join(dealer_hand))
		print("Dealer's scores are", dealer_scores)
	elif dealer_scores > 21:
		print("Dealer was busted. You won!")
	elif your_scores > dealer_scores:
		print("You won!")
		print("Dealer has:", "".join(dealer_hand))
		print("Dealer's scores are", dealer_scores)
	elif your_scores < dealer_scores:
		print("You lost!")
		print("Dealer has:", "".join(dealer_hand))
		print("Dealer's scores are", dealer_scores)
	else:
		print("It's a tie. No one won.")
		print("Dealer has:", "".join(dealer_hand))
		print("Dealer's scores are", dealer_scores)
