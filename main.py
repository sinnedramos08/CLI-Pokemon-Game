from gameflow import GameFlow

board_width=input("Input Board Width: ")
board_height=input("Input Board Height: ")
grass_count=input("Input Grass Count: ")


new_game=GameFlow(board_width=20, board_height=10, grass_count=150, steps=50, pokeballs=10, heal=10)
new_game.print_intro()
new_game.choose_new_pokemon()
new_game.start_game()
new_game.end_game()
