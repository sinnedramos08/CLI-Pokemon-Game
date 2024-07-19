import random
from board import Board
from pokemon import Pokemon
from battle import Battle
import time

class GameFlow:
    def __init__(self, board_width:int, board_height:int, grass_count:int, steps:int,pokeballs:int, heal:int):
        self.board=Board(board_width, board_height, grass_count, steps)
        self.pokemon_player=None #Initialized as None untile we choose our first pokemon
        self.pokeballs=pokeballs
        self.battle=None #Initialize this as None for the first time
        self.pokemon_player_list= None
        self.heal: int=heal

    def print_intro(self):
        print("Welcome to CLI Pokemon Game")
        time.sleep(1)
        name_player=input("Please enter your name: ")
        time.sleep(1)
        print(f"Hello, {name_player}, please choose your first pokemon from the list below")
        time.sleep(1)
        print('''
        Pokemon 1: Pikachu
        Type: Electric
        HP: 500
        Movelist:
        1. Thunderbolt (damage: 90)
        2. Thunder (damage: 110) 
        3. Spark (damage: 65)
        4. Thundershock (damage: 40)''')
        time.sleep(1)
        print('''
        Pokemon 2: Charmander
        Type: Fire
        HP: 500
        Movelist:
        1. Flamethrower (damage: 90)
        2. Fire Blast (damage: 110) 
        3. Heat Wave (damage: 95)
        4. Flame Wheel (damage: 60)''')
        time.sleep(1)
        print('''
        Pokemon 3: Bulbasaur
        Type: Grass
        HP: 500
        Movelist:
        1. Leaf Blade (damage: 90)
        2. Solar Beam (damage: 120) 
        3. Razor Leaf (damage: 55)
        4. Energy Ball (damage: 90)''')
        time.sleep(1)
        print('''
        Pokemon 4: Squirtle
        Type: Water
        HP: 500
        Movelist:
        1. Surf (damage: 90)
        2. Hydro Pump (damage: 110) 
        3. Waterfall (damage: 80)
        4. Bubble Beam (damage: 65)''')
        time.sleep(1)

    #Choose new pokemon: Pikachu, Charmander, Bulbasaur, Squirtle
    def choose_new_pokemon(self):

        pokemon_dict={
            "1": "Pikachu",
            "2": "Charmander",
            "3": "Bulbasaur",
            "4": "Squirtle"
        }

        #Choose Pokemon
        while True:
            pokemon_num=input("Please enter the number of your desired pokemon (1,2,3,4): ")
            if pokemon_num in pokemon_dict:
                break
            else:
                print("Please select from the 4 pokemons only")
        
        selected_pokemon = pokemon_dict[pokemon_num]

        #Create a new pokemon for the player
        self.pokemon_player= self.create_pokemon_player(selected_pokemon)

        self.pokemon_player_list={1:self.pokemon_player}

        #This will return a Pokemon object from the Pokemon class
        print(f"Congrats! you received {self.pokemon_player.name}\n")
        #Timer for entering the game
        time.sleep(1)
        seconds=3
        while seconds>0:
            print(f"Entering Pokemon Game in {seconds}")
            time.sleep(1)
            seconds-=1
        print("\n")
    
    #Create pokemon for player
    def create_pokemon_player(self, pokemon_name:str):
        return Pokemon(name=pokemon_name, hp=500)
    
    #Start the game, create new baord and initialize movements
    def start_game(self):

        while True:
            self.board.print_board()
            movement = input("Enter movement (w/a/s/d): ").strip().lower()

            #Heal all pokemon for 30 HP when moving
            self.heal_all_pokemon_step(30)

            #Movements
            if movement == "w":
                self.board.move_up()
            elif movement == "s":
                self.board.move_down()
            elif movement == "d":
                self.board.move_right()
            elif movement == "a":
                self.board.move_left()

            #End game if no more steps
            if self.board.steps==0:
                print("Congratulations! You have successfully completed CLI ")
                break

            if self.board.is_ash_on_grass():
                self.pokemon_encounter()
            
            #Initiate game over sequence if there are no more Pokemons available to battle
            #self.battle is initially None, this means that if there is a battle object, and it has game over attribute = true
            #Game over sequence is initiated
            if self.battle and self.battle.game_over:
                print("Game Over! All your Pokemon have fainted.")
                break
                
    def heal_all_pokemon_step(self, amount:int):
        if self.pokemon_player_list:
            for pokemon in self.pokemon_player_list.values():
                pokemon.current_hp = min(pokemon.hp, pokemon.current_hp + amount)
                pokemon.check_status()

    #Encountering Pokemon
    def pokemon_encounter(self):

        #Check if there will be a pokemon encounter on that grass
        #50% chance of encounter when on a grass
        rand_num=random.randint(0,1)
        if rand_num==0:
            #This means that there will be a pokemon encounter on that grass tile
            #We then place a random pokemon 
            pokemon_enemy=self.board.place_pokemon()
            print("...")
            time.sleep(3)
            print(f"You encountered a wild {pokemon_enemy.name}, Type: {pokemon_enemy.primary_type}, HP: {pokemon_enemy.hp}")
            self.board.countdown_battle(pokemon_enemy.name)
            time.sleep(1)


            # Battle Logic Here

            #Ensure that pokemon_player is not None, helps for code warnings when instantiating using this object
            assert self.pokemon_player is not None
        
            #If we encounter pokemon for the first time, we create a battle class for the first time
            if not self.battle: #This will check if the self.battle has no value or None
                self.battle = Battle(self.pokemon_player, pokemon_enemy, self.pokeballs,self.heal)
            
            #This means that we have already a Battle object and we don't need to instantiate it again
            #We will just update the parameters for the battle object before starting battle
            else:
                self.battle.pokemon_enemy = pokemon_enemy
                self.battle.pokemon_player = self.pokemon_player
                self.battle.pokeballs = self.pokeballs
                self.battle.heal= self.heal

            #Start battle
            self.battle.start_battle()

            #Update pokeballs and pokemonlist based on the result of battle
            self.pokeballs = self.battle.pokeballs
            self.pokemon_player_list = self.battle.pokemon_player_list
            self.heal=self.battle.heal

    def end_game(self):
        time.sleep(3)
        print("\nHere are all the pokemons you captured:\n")
        time.sleep(2)
        self.print_pokemon_list()
        print("\nThank you for playing CLI Pokemon Game")
        time.sleep(2)
        print("This Game is created by: Dennis Andrew R. Ramos")
        time.sleep(3)
        print("Goodbye!")

    def print_pokemon_list(self):

        assert self.pokemon_player_list is not None
        for key,pokemon in self.pokemon_player_list.items():
            print(f"{key}. {pokemon.name} | CurrentHP:{pokemon.current_hp} | MaxHP:{pokemon.hp} | Status:{pokemon.status}\n")
            time.sleep(1)
        pass