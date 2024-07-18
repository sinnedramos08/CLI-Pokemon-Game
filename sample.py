        #Add to pokemon list if captured
        if captured:
            print(f"Congratulations! You have captured {wild_pokemon.name}")
            #Add to list with new key
            new_key=max(self.pokemon_player_list.keys())+1
            self.pokemon_player_list[new_key]=wild_pokemon

            print("Your Current Pokemons: \n")
            for key,pokemon in self.pokemon_player_list.items():
                print(f"{key}. {pokemon.name}\n")
        else:
            print(f"Wild {wild_pokemon.name} broke free!")