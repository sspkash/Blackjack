# This program helps manage the player's bankroll, during the course of the game.

import time


class BankrollOfPlayer:
    def __init__(self, amount):
        self.amount = amount

    def bet_input(self):
        global bet_amount
        bet_amount = int(input('\nPlace your bet!\n'))

    def bet_verification(self):
        global bet_amount
        while bet_amount > self.amount:
            print(f'The bet amount exceeds the available amount which is {self.amount}.')
            self.bet_input()

    def bet_implementation(self, result):
        global bet_amount
        self.amount -= bet_amount
        if result:
            self.bankroll_addition(bet_amount)
        else:
            self.bankroll_subtraction(bet_amount)

    def bankroll_addition(self, value):
        self.amount += (1.5 * value)
        time.sleep(2)
        print(f'\nYou won {1.5 * value}$!\nYou currently have {self.amount}$ in your account.\n')

    def bankroll_subtraction(self, value):
        time.sleep(2)
        print(f'\nYou lost {value}$!\nYou currently have {self.amount}$ in your account.\n')
