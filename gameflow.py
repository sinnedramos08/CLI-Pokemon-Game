import random
from board import Board

class GameFlow:
    def __init__(self, board_width:int, board_height:int, grass_count:int, steps:int):
        self.board=Board(board_width, board_height, grass_count, steps)
    
    #Choose new pokemon
    def choose_new_pokemon(self):
        pass
    
    #
    def start_game(self):

        while True:
            self.board.print_board()
            movement = input("Enter movement (w/a/s/d): ").strip().lower()
            if movement == "w":
                self.board.move_up()
            elif movement == "s":
                self.board.move_down()
            elif movement == "d":
                self.board.move_right()
            elif movement == "a":
                self.board.move_left()
            if self.board.steps==0:
                break

            if self.board.is_ash_on_grass():
                self.pokemon_encounter()
    
    def pokemon_encounter(self):
        #Check if there will be a pokemon encounter on that grass
        #50% chance of encounter when on a grass
        rand_num=random.randint(0,1)
        if rand_num==0:
            #This means that there will be a pokemon encounter on that grass tile
            #We then place a random pokemon 
            pokemon_enemy=self.board.place_pokemon()
            print(f"You encountered a wild {pokemon_enemy}")
            self.board.countdown_battle(pokemon_enemy.name)
            # Battle Logic Here

        

    
