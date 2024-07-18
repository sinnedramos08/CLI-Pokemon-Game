import random
from pokemon import pokemon_primary_types, type_moves
from pokemon import Pokemon
import time

class Board:
    def __init__(self, width:int, height:int, grass:int, steps:int):
        #Create a new board class with parameters:
        #width, height, number of grass
        self.width=width
        self.height=height
        self.grass=grass
        self.steps=steps

        #Create the board itself on the command line
        #Use helper function to create the board
        #We need another copy of the original board so we can know
        #the index of grass on the board
        self.board,self.grass_location=self.make_new_board()
    
    #Create a new baord with grass
    def make_new_board(self):
        '''
        We will use 2D List with list within the list
        The output will look like this:

        [[' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ']]
        '''
        board=[[" " for _ in range(self.width)] for _ in range(self.height)]
        board[0][0]="A"

        #Add grass tiles
        #We use random library to put grass on random tiles
        grass_board=0
        area=self.width*self.height

        #Create a list of grass location for memory
        grass_location=[]

        while grass_board<self.grass:
            loc=random.randint(0, area-1) #This chooses a random location from 0 to the last index of the 2D array
            #Find the row number 
            #Example we have a width=4 and height=5
            #We locate the random row number by
            #Using the floor function // on random loc to the width of the board
            #Example: loc is 14, width is 4, 14//4=3, therefore the row location is index 3
            #Example: loc is 4, width is 4, 14//4=1, therefore the row location is index 1
            row = loc//self.width

            #Find the column number
            #We use the remainder to get the column location
            #Example: loc is 14, width is 4, 14%4=2, therefore column location is index 2
            #Example: loc is 4, width is 4, 14%4=0, therefore column location is index 0
            col=loc%self.width

            #Create a grass location list for the memory of grass location
            
            #Check if there's a grass on that location
            if board[row][col]=="*" or board[row][col]=="A":
                #Go to the next iteration
                continue

            #Plant the grass on the location
            board[row][col]="*"

            #Create a memory of (row,col) pairs of the location of the grass
            grass_location.append([row,col])


            grass_board+=1

        return board, grass_location

    def move_right(self):
        #We need to move Ash to the right from his original location
        #We add 1 to its outer index
        #We need to find ash location first
        r,c=self.ash_finder()

        #Check if out of bounds
        if c+1<self.width:
            self.update_board(r,c,r,c+1)
            self.steps-=1
        self.print_board()

    def move_left(self):
        
        r,c=self.ash_finder()
        if c - 1 >= 0:
            self.update_board(r, c, r, c - 1)
            self.steps-=1
        self.print_board()

    def move_up(self):  
        r,c=self.ash_finder()
        #Check if out of bounds
        if r - 1 >= 0:
            self.update_board(r, c, r - 1, c)
            self.steps-=1
        self.print_board()

    def move_down(self):
        #We need to move Ash to the left from his original location
        #We need to find ash location first
        r,c=self.ash_finder()

        #Check if out of bounds
        if r + 1 < self.height:
            self.update_board(r, c, r + 1, c)
            self.steps-=1
        self.print_board()

    #Find ash on the board
    def ash_finder(self):
        #Scan for ash location on board
        for row in range(self.height):
            for col in range (self.width):
                if self.board[row][col] !="A":
                        continue
                return row,col

    #Countdown before battle
    def countdown_battle(self, pokemon:str):
        #Count down for entering battle
        seconds=3
        while seconds>0:
            print(f"Entering battle in {seconds}")
            time.sleep(1)
            seconds-=1
        
        print(f"Battle against {pokemon} starts now!")

    #Updating the board, where Ash lands on new tile    
    def update_board(self,old_r:int,old_c:int, new_r:int, new_c:int):
        #Check if the tile previously is a grass
        #When moving to another tile, return back the grass
        #Use the list of grass locations as the memory
        if [old_r,old_c] in self.grass_location:
            self.board[old_r][old_c] = "*"
        else:
            self.board[old_r][old_c] =" "
        self.board[new_r][new_c]="A"
    
    #Check if ash is on the grass
    def is_ash_on_grass(self):
        new_r, new_c = self.ash_finder()
        #Check if Ash is on a grass tile
        if [new_r, new_c] in self.grass_location:
            return True
        else: return False

    #For Printing the board
    def print_board(self):
        print(f"Remaining Steps: {self.steps}")
        #Print Upper Boarder
        print("-" * (self.width + 2))

        #Print each row in board 2D array
        #row variable represent each list within the list
        for row in self.board:
            #"".join(row) joins each element in the list with "" as separator
            print("|" + "".join(row) + "|")

        #Print Lower Boarder
        print("-" * (self.width + 2))

    #Place Pokemon on Grass Tiles
    def place_pokemon(self):
        #We place pokemons on the grass tiles
        pokemon_enemy=Pokemon(name=random.choice(list(pokemon_primary_types.keys())), hp=random.randint(200,800))
        return pokemon_enemy


            







