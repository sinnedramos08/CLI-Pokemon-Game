from gameflow import GameFlow

new_game=GameFlow(board_width=5, board_height=5, grass_count=5, steps=50)
new_game.start_game()



'''
def play(width=15, height=10, grass=15,steps=5000):

    #Create a new board
    new_board=Board(width=width, height=height,grass=grass,steps=steps)
    new_board.print_board()
    
    #Play the game with movements
    while True:
        movement=input("Movement w/a/s/d: ")
        if movement=="w":
            new_board.move_up()
        elif movement=="s":
            new_board.move_down()
        elif movement=="d":
            new_board.move_right()
        elif movement=="a":
            new_board.move_left()
        if new_board.steps==0:
            break
    
    #List all the pokemons you caught

    
play()
'''

