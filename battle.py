import time
import random
from pokemon import Pokemon
class Battle:
    def __init__(self, pokemon_player:Pokemon, pokemon_enemy:Pokemon, pokeballs:int, heal:int):
        self.pokemon_enemy = pokemon_enemy
        self.pokemon_player= pokemon_player
        self.pokemon_player_list = {1:pokemon_player}
        self.pokeballs=pokeballs
        self.heal=heal
        self.game_over=False
    
    def start_battle(self):
        #Select pokemon to use for battle
        selected_pokemon= self.choose_pokemon_battle() #Get the selected pokemon to battle in this method
        
        #Select move, Fight - F, Throw Pokeball - T, Run- R
        #Go to Battle Options
        self.battle_options(selected_pokemon)

    def battle_options(self, pokemon_player:Pokemon):
        #Check hp of opponent and pokemon
        while pokemon_player.current_hp > 0 and self.pokemon_enemy.current_hp > 0:

            self.print_pokemon_hp(pokemon_player)
            time.sleep(2)
            print(f"\nChoose an action: 1. Fight 2. Run 3. Throw Pokeball (Pokeballs Remaining:{self.pokeballs}) 4. Heal current pokemon (Heals Remaining:{self.heal})")
            
            choice_battle_options=input("Your choice: ")

            #Choice to Fight
            if choice_battle_options=="1":
                #Fight Logic

                #Players turn to fight
                self.player_turn(pokemon_player)
                #Check if the enemy has fainted so that it won't execute its turn
                if self.pokemon_enemy.current_hp<=0:
                    print(f"\nWild {self.pokemon_enemy.name} has fainted\n")
                    time.sleep(2)
                    print("\nGoing back to the board\n")
                    time.sleep(2)
                    break


                #Enemy's Turn
                self.enemy_turn(pokemon_player)
                #Check if the player's Pokemon has fainted
                if pokemon_player.current_hp <= 0:
                    print(f"\nYour {pokemon_player.name} has fainted!\n")
                    time.sleep(2)
                    #Check if there are available pokemon
                    #Create a list of available pokemons
                    available_pokemon=[pkmn for pkmn in self.pokemon_player_list.values() if pkmn.current_hp>0]
                    
                    #If there are available pokemon, proceed to choosing another pokemon
                    if available_pokemon:
                        print("Please choose another pokemon")
                        pokemon_player= self.choose_pokemon_battle()
                        

                    #If there are no available pokemon, the player can not continue, and therefore game over
                    else:
                        #Game over
                        self.game_over=True
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
                    self.enemy_turn(pokemon_player)
                    continue
            #Choice to heal current pokemon
            elif choice_battle_options=="4":
                #Check if there are available heal points
                if self.heal > 0:
                    pokemon_player.heal()
                    self.heal-=1
                    print(f"\n{pokemon_player.name} has been healed (Current HP:{pokemon_player.current_hp}).  Remaining heals: {self.heal}\n")
                    time.sleep(3)
                    self.enemy_turn(pokemon_player)
                else:
                    print("No heals remaining.")


    def player_turn(self, pokemon_player:Pokemon):
        #Player's turn
        pokemon_player_damage=self.pokemon_player_attack(pokemon_player)
        #Implement a method for taking damage for pokemon object
        self.pokemon_enemy.take_damage(pokemon_player_damage)
        time.sleep(3)
        self.print_pokemon_hp(pokemon_player)
        time.sleep(3) 

    def enemy_turn(self, pokemon_player:Pokemon):
        #Random move from move list
        move_number=random.randint(1,4)
        pokemon_enemy_damage=self.pokemon_enemy.attack_pokemon(move_number)
        pokemon_player.take_damage(pokemon_enemy_damage)
        time.sleep(3)
        pass
    
    def pokemon_player_attack(self, pokemon_player:Pokemon):
        self.print_movelist(pokemon_player)

        #Select move
        while True:
            try: 
                selected_attack_num=int(input("Please choose a move: "))
                if 1<=selected_attack_num<= len(pokemon_player.moves):
                    pokemon_damage=pokemon_player.attack_pokemon(selected_attack_num)
                    break
                else: 
                    print("Invalid selection. Please select a valid Pokemon number.")
            except:
                print("Invalid input. Please enter a number.")
        
        #Return the damage of the attack
        return pokemon_damage
    
    #Helper Function
    def print_movelist(self, pokemon_player:Pokemon):
        print(f"\n{pokemon_player.name} Movelist:\n")
        for i, move in enumerate(pokemon_player.moves, start=1):
            print(f"{i}. {move['name']} (Damage: {move['damage']})")
            time.sleep(1)

    #Helper Function
    def print_pokemon_hp(self, pokemon_player:Pokemon):
        pokemon_player_hp_percentage=(pokemon_player.current_hp/pokemon_player.hp)*100
        pokemon_enemy_hp_percentage=(self.pokemon_enemy.current_hp/self.pokemon_enemy.hp)*100
        print(f"\nYour {pokemon_player.name}'s | HP: {pokemon_player.current_hp} | HP%:{pokemon_player_hp_percentage:.2f} | Status:{pokemon_player.status}")
        print(f"Wild {self.pokemon_enemy.name}'s | HP: {self.pokemon_enemy.current_hp} | HP%:{pokemon_enemy_hp_percentage:.2f} | Status:{self.pokemon_enemy.status}\n")

    #Helper Function
    def add_pokemon_to_list(self, wild_pokemon:Pokemon):
        new_key=max(self.pokemon_player_list.keys())+1
        self.pokemon_player_list[new_key]=wild_pokemon
        pass

    def throw_pokeball(self, pokeballs:int, wild_pokemon:Pokemon):
        print(f"\nYou have thrown a pokeball to {wild_pokemon.name}\n")
        pokeballs-=1

        return pokeballs

    #Helper Function
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
            capture_chance = 0.1 #change this for testing purposes, 0.1 original value
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
                    selected_pokemon=self.pokemon_player_list[selected_pokemon_num]
                    #Check if the pokemon you selected is fainted
                    if selected_pokemon.current_hp >0:
                        print(f"\nYou have selected {self.pokemon_player_list[selected_pokemon_num].name}")
                        break
                    else:
                        print("You cannot select a fainted Pokemon. Please Choose another")
                else: 
                    print("Invalid selection. Please select a valid Pokemon number.")
            except:
                print("Invalid input. Please enter a number.")
        
        #Return this pokemon to be used in battle
        return selected_pokemon
    
    #Helper Function
    def print_pokemon_list(self):
        #Print a list of all the pokemons you have
        print("Your Current Pokemons:\n")
        for key,pokemon in self.pokemon_player_list.items():
            pokemon_hp_percentage=(pokemon.current_hp/pokemon.hp)*100
            print(f"{key}. {pokemon.name} | MaxHP:{pokemon.hp} | CurrentHP:{pokemon.current_hp} | HP%:{pokemon_hp_percentage:.2f} | Status:{pokemon.status}\n")
            time.sleep(1)
        time.sleep(0.5)
        print(f"Pokeballs remaining: {self.pokeballs}")
        print(f"Heals remaining:{self.heal}\n")
