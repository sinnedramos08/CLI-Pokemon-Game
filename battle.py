import time
import random
from pokemon import Pokemon
class Battle:
    def __init__(self, pokemon_player:Pokemon, pokemon_enemy:Pokemon, pokeballs:int):
        self.pokemon_enemy = pokemon_enemy
        self.pokemon_player= pokemon_player
        self.pokemon_player_list = {1:pokemon_player}
        self.pokeballs=pokeballs
    
    def start_battle(self):
        #Select pokemon to use for battle
        selected_pokemon= self.choose_pokemon_battle() #Get the selected pokemon to battle in this method
        
        #Select move, Fight - F, Throw Pokeball - T, Run- R
        #Go to Battle Options
        self.battle_options(selected_pokemon)

    def battle_options(self, pokemon_player:Pokemon):
        #Check hp of opponent and pokemon
        while pokemon_player.current_hp > 0 and self.pokemon_enemy.current_hp > 0:
            
            print(f"\nChoose an action: 1. Fight 2. Run 3. Throw Pokeball (Pokeballs Remaining:{self.pokeballs})")
            choice_battle_options=input("Your choice: ")

            #Choice to Fight
            if choice_battle_options=="1":
                #Fight Logic
                #We need a method that will pass us what attack we used
                
                pass
            
            #Choice to Run
            elif choice_battle_options=="2":
                print(f"\nYou run away safely from {self.pokemon_enemy.name}\n")
                time.sleep(2)
                print("Going back to the board\n")
                time.sleep(2)

                #Exit from battle options
                break

            #Choice to throw Pokeball
            elif choice_battle_options=="3":
                #Logic for throwing pokeball
                self.pokeballs=self.throw_pokeball(self.pokeballs, self.pokemon_enemy)
 
                #Capturing timer after throwing the pokeball
                self.capturing_timer(self.pokemon_enemy)

                #Logic for capturing pokemons
                #Check if captured
                #Use health percentage to calculate capturing rate
                captured=self.capturing_pokemon(self.pokemon_enemy)

                #Check if the pokemon is captured, then add to list
                if captured:
                    print(f"Congratulations! You have captured {self.pokemon_enemy.name}\n")
                    #Add to list with new key
                    self.add_pokemon_to_list(self.pokemon_enemy)
                    #Timer
                    time.sleep(3)
                    self.print_pokemon_list()
                    print("Going back to the board")
                    time.sleep(2)
                    break
                #If not captured, still fight with the pokemon
                else:
                    print(f"Wild {self.pokemon_enemy.name} broke free!\n")
                    continue

    def add_pokemon_to_list(self, wild_pokemon:Pokemon):
        new_key=max(self.pokemon_player_list.keys())+1
        self.pokemon_player_list[new_key]=wild_pokemon
        pass

    def throw_pokeball(self, pokeballs:int, wild_pokemon:Pokemon):
        print(f"\nYou have thrown a pokeball to {wild_pokemon.name}\n")
        pokeballs-=1

        return pokeballs

    def capturing_timer(self, wild_pokemon:Pokemon):
        print(f"Trying to capture wild {wild_pokemon.name}")
        seconds=3
        while seconds>0:
            print("...")
            time.sleep(1)
            seconds-=1
        
        time.sleep(3)

    def capturing_pokemon(self,wild_pokemon:Pokemon):
        #Check health percentage
        health_percentage=(wild_pokemon.current_hp/wild_pokemon.hp)*100
        
        #Lower health percentage means higher chance of capturing Pokemon
        if health_percentage > 75:
            capture_chance = 0.9 #change this for testing purposes, 0.1 original value
        elif health_percentage > 50:
            capture_chance = 0.25
        elif health_percentage > 25:
            capture_chance = 0.5
        else:
            capture_chance = 0.8
        
        #Check if captured based on capture chance
        return random.random()<capture_chance

    def choose_pokemon_battle(self):
        print(f"\nChoose the pokemon to battle against {self.pokemon_enemy.name}\n")

        #Print a list of all the pokemons you have
        self.print_pokemon_list()

        #Select which pokemon to use
        while True:
            try: 
                selected_pokemon_num=int(input("Please select a Pokemon from your current list: "))
                if selected_pokemon_num in self.pokemon_player_list:
                    print(f"\nYou have selected {self.pokemon_player_list[selected_pokemon_num].name}")
                    break
                else: 
                    print("Invalid selection. Please select a valid Pokemon number.")
            except:
                print("Invalid input. Please enter a number.")
        
        #Return this pokemon to be used in battle
        return self.pokemon_player_list[selected_pokemon_num]

    def print_pokemon_list(self):
        #Print a list of all the pokemons you have
        print("Your Current Pokemons:\n")
        for key,pokemon in self.pokemon_player_list.items():
            print(f"{key}. {pokemon.name} HP:{pokemon.hp}\n")
            time.sleep(1)
        time.sleep(0.5)
        print(f"Pokeballs remaining: {self.pokeballs}\n")