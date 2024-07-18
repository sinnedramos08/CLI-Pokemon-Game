from gameflow import GameFlow

new_game=GameFlow(board_width=5, board_height=5, grass_count=5, steps=50, pokeballs=10)
new_game.print_intro()
new_game.choose_new_pokemon()
new_game.start_game()