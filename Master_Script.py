# This program aggregates the other modules and arranges them in the order of execution.

# Import of modules.
import Module_CardDeck
import Module_Hands

# Picking up random cards from the card deck.
player_1st_card = Module_CardDeck.card_picking_function()
player_2nd_card = Module_CardDeck.card_picking_function()
dealer_1st_card = Module_CardDeck.card_picking_function()
dealer_2nd_card = Module_CardDeck.card_picking_function()

# Instantiating the 'Hands' class.
hands_class = Module_Hands.GameHand(player_1st_card, player_2nd_card, dealer_1st_card, dealer_2nd_card)

# Displaying the cards assigned to the player's and the dealer's hands.
hands_class.display_cards()

# Execute the first turn of the game.
hands_class.of_player()

# Run successive trials of the game, if asked for by the player.
hands_class.continue_game()
