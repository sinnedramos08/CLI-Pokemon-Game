from gameflow import GameFlow

new_game=GameFlow(board_width=20, board_height=10, grass_count=150, steps=1, pokeballs=10, heal=10)
new_game.print_intro()
new_game.choose_new_pokemon()
new_game.start_game()
new_game.end_game()
