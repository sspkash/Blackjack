# This program helps emulate a deck of 52 playing cards, a choosing a card from it at random.

from random import randint
import time

card_face_values = {'ace': (1, 11), 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                    'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10}

card_deck = {'diamonds': card_face_values, 'hearts': card_face_values,
             'clubs': card_face_values, 'spades': card_face_values}


def card_picking_function():
    card_suite_var = randint(0, 3)
    card_number_var = randint(0, 12)

    chosen_card_suite = tuple(card_deck.keys())[card_suite_var]
    chosen_card_value = tuple((tuple(card_deck.items())[card_suite_var][1]).items())[card_number_var][0]

    return chosen_card_value, chosen_card_suite

while __name__ == '__main__':
    print(card_picking_function())
    time.sleep(1)