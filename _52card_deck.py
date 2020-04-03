import random
import collections
SUITS = ['spades', 'hearts', 'diamonds','clubs' ]
ROYAL_FLUSH =['ace', 'king', 'queen', 'jack', '10' ]
VALUES = ['ace', '2', '3', '4', '5', '6', '7','8' ,'9' ,'10' ,'jack' ,'queen' ,'king' ]

def create_deck():
    cards = []
    for suit in SUITS:
        for value in VALUES:
            cards.append((value, suit))
    return cards

def get_a_hand(cards, size_of_hand):
    try:
        hand = random.sample(cards, size_of_hand)        
    except:
        print('exceeds maximum of cards')
        hand = random.sample(cards,52)
    return hand

def main(size_of_hand, number_of_hands):
    cards = create_deck()
    hands = []

    for _ in range(number_of_hands):
        hand = get_a_hand(cards, size_of_hand)
        hands.append(hand)
    pairs = 0
    for hand in hands:
        values = []
        for card in hand:
            values.append(card[0])
        counter = dict(collections.Counter(values))
        for card_key in counter.values():
            #if card_key == 2:
            if card_key == 3:
                pairs += 1
                break
    probability = pairs / number_of_hands
    print(f'The probability of get pair with a hand of {size_of_hand} cards is: {probability}')

if __name__ == '__main__':
    size_of_hand = int(input('How many cards per hand: '))
    number_of_hands = int(input('How many simulations: '))
    main(size_of_hand, number_of_hands)
    #print(deck_of_cards)