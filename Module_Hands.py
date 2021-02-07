# This program defines a class to emulate the hands of the player and the dealer.

import time
import Module_CardDeck
import Module_PlayerBankroll


class GameHand:

    def __init__(self, card1, card2, card3, card4):
        self.player_card1 = card1
        self.player_card2 = card2
        self.dealer_card1 = card3
        self.dealer_card2 = card4
        bankroll_amount_input = int(input('How much amount would you like to store in your bankroll?\n'))
        self.bankroll_class = Module_PlayerBankroll.BankrollOfPlayer(bankroll_amount_input)
        self.bankroll_class.bet_input()
        self.bankroll_class.bet_verification()

    def display_cards(self):
        print(
            f'\nYou have received {self.player_card1[0]} of {self.player_card1[1]} and {self.player_card2[0]} of '
            f'{self.player_card2[1]}.')
        time.sleep(2)
        print(f'Dealer has received the {self.dealer_card1[0]} of {self.dealer_card1[1]}!\n')
        time.sleep(2)

    def of_player(self):
        global game_output
        if self.player_card1[0] == 'ace':
            player_ace_flag = True
            sum_of_player_hands = (Module_CardDeck.card_deck[self.player_card2[1]])[self.player_card2[0]]
            if 21 - sum_of_player_hands >= 11:
                sum_of_player_hands += (Module_CardDeck.card_deck[self.player_card1[1]])[self.player_card1[0]][1]
            else:
                sum_of_player_hands += (Module_CardDeck.card_deck[self.player_card1[1]])[self.player_card1[0]][0]
        elif self.player_card2[0] == 'ace':
            player_ace_flag = True
            sum_of_player_hands = (Module_CardDeck.card_deck[self.player_card1[1]])[self.player_card1[0]]
            if 21 - sum_of_player_hands >= 11:
                sum_of_player_hands += (Module_CardDeck.card_deck[self.player_card2[1]])[self.player_card2[0]][1]
            else:
                sum_of_player_hands += (Module_CardDeck.card_deck[self.player_card2[1]])[self.player_card2[0]][0]
        else:
            player_ace_flag = False
            sum_of_player_hands = (Module_CardDeck.card_deck[self.player_card1[1]])[self.player_card1[0]] + \
                                  (Module_CardDeck.card_deck[self.player_card2[1]])[self.player_card2[0]]
        print(f'Sum of your cards is {sum_of_player_hands}.')
        time.sleep(2)
        while sum_of_player_hands < 21:
            player_hit_input = input('\nDo you want to hit?\n')
            if 'y' in player_hit_input.lower():
                new_player_card = Module_CardDeck.card_picking_function()
                time.sleep(2)
                print(f'\nYou have received {new_player_card[0]} of {new_player_card[1]}.')
                try:
                    sum_of_player_hands += (Module_CardDeck.card_deck[new_player_card[1]])[new_player_card[0]]
                    if sum_of_player_hands > 21 and player_ace_flag:
                        sum_of_player_hands -= 10
                except:
                    if 21 - sum_of_player_hands >= 11:
                        sum_of_player_hands += (Module_CardDeck.card_deck[new_player_card[1]])[new_player_card[0]][1]
                    else:
                        sum_of_player_hands += (Module_CardDeck.card_deck[new_player_card[1]])[new_player_card[0]][0]
                time.sleep(2)
                print(f'The new sum of your cards is {sum_of_player_hands}.')

            elif 'n' in player_hit_input.lower():
                self.of_dealer(sum_of_player_hands)
                break

            else:
                print('Oops! Invalid input!')

        else:
            if sum_of_player_hands == 21:
                game_output = True
                print('\nYou got a Blackjack!')
                self.bankroll_class.bet_implementation(game_output)
            else:
                game_output = False
                print('\nYou bust!')
                self.bankroll_class.bet_implementation(game_output)

    def of_dealer(self, player_sum):
        global game_output
        time.sleep(2)
        print(f'\nThe other card of the dealer was the {self.dealer_card2[0]} of {self.dealer_card2[1]}.')
        if self.dealer_card1[0] == 'ace':
            dealer_ace_flag = True
            sum_of_dealer_hands = (Module_CardDeck.card_deck[self.dealer_card2[1]])[self.dealer_card2[0]]
            if 21 - sum_of_dealer_hands >= 11:
                sum_of_dealer_hands += (Module_CardDeck.card_deck[self.dealer_card1[1]])[self.dealer_card1[0]][1]
            else:
                sum_of_dealer_hands += (Module_CardDeck.card_deck[self.dealer_card1[1]])[self.dealer_card1[0]][0]
        elif self.dealer_card2[0] == 'ace':
            dealer_ace_flag = True
            sum_of_dealer_hands = (Module_CardDeck.card_deck[self.dealer_card1[1]])[self.dealer_card1[0]]
            if 21 - sum_of_dealer_hands >= 11:
                sum_of_dealer_hands += (Module_CardDeck.card_deck[self.dealer_card2[1]])[self.dealer_card2[0]][1]
            else:
                sum_of_dealer_hands += (Module_CardDeck.card_deck[self.dealer_card2[1]])[self.dealer_card2[0]][0]
        else:
            dealer_ace_flag = False
            sum_of_dealer_hands = (Module_CardDeck.card_deck[self.dealer_card1[1]])[self.dealer_card1[0]] + \
                                  (Module_CardDeck.card_deck[self.dealer_card2[1]])[self.dealer_card2[0]]
        print(f"Sum of dealer's hands is {sum_of_dealer_hands}.\n")
        while sum_of_dealer_hands < 21 and sum_of_dealer_hands <= player_sum:
            time.sleep(2)
            new_dealer_card = Module_CardDeck.card_picking_function()
            print(f"The dealer's new card is a {new_dealer_card[0]} of {new_dealer_card[1]}.")
            try:
                sum_of_dealer_hands += (Module_CardDeck.card_deck[new_dealer_card[1]])[new_dealer_card[0]]
                if sum_of_dealer_hands > 21 and dealer_ace_flag:
                    sum_of_dealer_hands -= 10
            except:
                if 21 - sum_of_dealer_hands >= 11:
                    sum_of_dealer_hands += (Module_CardDeck.card_deck[new_dealer_card[1]])[new_dealer_card[0]][1]
                else:
                    sum_of_dealer_hands += (Module_CardDeck.card_deck[new_dealer_card[1]])[new_dealer_card[0]][0]
            print(f"The sum of dealer's hands is {sum_of_dealer_hands}.\n")
            if sum_of_dealer_hands == 21 or sum_of_dealer_hands > 21:
                if sum_of_dealer_hands == 21:
                    game_output = False
                    time.sleep(2)
                    print('Dealer gets a Blackjack!')
                    self.bankroll_class.bet_implementation(game_output)
                    break
                else:
                    game_output = True
                    time.sleep(2)
                    print('Dealer busted!')
                    self.bankroll_class.bet_implementation(game_output)
                    break
        else:
            game_output = False
            time.sleep(2)
            print('Dealer wins!')
            self.bankroll_class.bet_implementation(game_output)

    def continue_game(self):
        while True:
            if self.bankroll_class.amount == 0:
                print("Sorry bud, you ain't got no more cash on you!\nTime to walk outta the door!")
                break
            else:
                continue_input = input('\nWould you like to continue?\n')
                if 'y' in continue_input.lower():
                    self.bankroll_class.bet_input()
                    self.bankroll_class.bet_verification()
                    self.player_card1 = Module_CardDeck.card_picking_function()
                    self.player_card2 = Module_CardDeck.card_picking_function()
                    self.dealer_card1 = Module_CardDeck.card_picking_function()
                    self.dealer_card2 = Module_CardDeck.card_picking_function()
                    self.display_cards()
                    self.of_player()
                elif 'n' in continue_input.lower():
                    print('Duh! What a chicken!')
                    break
                else:
                    print("Nope! Invalid input! Enter 'Yes' or 'No' to proceed.")
