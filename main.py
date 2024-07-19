from gameflow import GameFlow

new_game=GameFlow(board_width=20, board_height=10, grass_count=100, steps=50, pokeballs=10)
new_game.print_intro()
new_game.choose_new_pokemon()
new_game.start_game()