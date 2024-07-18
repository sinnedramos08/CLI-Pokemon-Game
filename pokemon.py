import random
pokemon_primary_types = {
    "Bulbasaur": "Grass", "Ivysaur": "Grass", "Venusaur": "Grass",
    "Charmander": "Fire", "Charmeleon": "Fire", "Charizard": "Fire",
    "Squirtle": "Water", "Wartortle": "Water", "Blastoise": "Water",
    "Caterpie": "Bug", "Metapod": "Bug", "Butterfree": "Bug",
    "Weedle": "Bug", "Kakuna": "Bug", "Beedrill": "Bug",
    "Pidgey": "Normal", "Pidgeotto": "Normal", "Pidgeot": "Normal",
    "Rattata": "Normal", "Raticate": "Normal", "Spearow": "Normal",
    "Fearow": "Normal", "Ekans": "Poison", "Arbok": "Poison",
    "Pikachu": "Electric", "Raichu": "Electric", "Sandshrew": "Ground",
    "Sandslash": "Ground", "Nidoran♀": "Poison", "Nidorina": "Poison",
    "Nidoqueen": "Poison", "Nidoran♂": "Poison", "Nidorino": "Poison",
    "Nidoking": "Poison", "Clefairy": "Fairy", "Clefable": "Fairy",
    "Vulpix": "Fire", "Ninetales": "Fire", "Jigglypuff": "Normal",
    "Wigglytuff": "Normal", "Zubat": "Poison", "Golbat": "Poison",
    "Oddish": "Grass", "Gloom": "Grass", "Vileplume": "Grass",
    "Paras": "Bug", "Parasect": "Bug", "Venonat": "Bug",
    "Venomoth": "Bug", "Diglett": "Ground"
}

type_moves = {

    "Bug": [
        {"name": "Bug Bite", "damage": 60},
        {"name": "X-Scissor", "damage": 80},
        {"name": "Signal Beam", "damage": 75},
        {"name": "Leech Life", "damage": 80}
    ],
    "Electric": [
        {"name": "Thunderbolt", "damage": 90},
        {"name": "Thunder", "damage": 110},
        {"name": "Spark", "damage": 65},
        {"name": "Thunder Shock", "damage": 40}
    ],
    "Fairy": [
        {"name": "Moonblast", "damage": 95},
        {"name": "Dazzling Gleam", "damage": 80},
        {"name": "Play Rough", "damage": 90},
        {"name": "Draining Kiss", "damage": 50}
    ],
    "Fire": [
        {"name": "Flamethrower", "damage": 90},
        {"name": "Fire Blast", "damage": 110},
        {"name": "Heat Wave", "damage": 95},
        {"name": "Flame Wheel", "damage": 60}
    ],
    "Grass": [
        {"name": "Leaf Blade", "damage": 90},
        {"name": "Solar Beam", "damage": 120},
        {"name": "Razor Leaf", "damage": 55},
        {"name": "Energy Ball", "damage": 90}
    ],
    "Ground": [
        {"name": "Earthquake", "damage": 100},
        {"name": "Bulldoze", "damage": 60},
        {"name": "Earth Power", "damage": 90},
        {"name": "Dig", "damage": 80}
    ],
    "Normal": [
        {"name": "Body Slam", "damage": 85},
        {"name": "Hyper Beam", "damage": 150},
        {"name": "Return", "damage": 102},
        {"name": "Double-Edge", "damage": 120}
    ],
    "Poison": [
        {"name": "Sludge Bomb", "damage": 90},
        {"name": "Poison Jab", "damage": 80},
        {"name": "Acid", "damage": 40},
        {"name": "Cross Poison", "damage": 70}
    ],
    "Water": [
        {"name": "Surf", "damage": 90},
        {"name": "Hydro Pump", "damage": 110},
        {"name": "Waterfall", "damage": 80},
        {"name": "Bubble Beam", "damage": 65}
    ]
}


class Pokemon:
    def __init__(self, name:str, hp:int):
        self.name = name
        self.hp = hp #For max HP tracking
        self.current_hp = hp #For current HP tracking
        self.primary_type=pokemon_primary_types[name]
        self.moves = type_moves.get(self.primary_type, []) #Returns a list with dictionary entries example: 
        #[{'name': 'Bug Bite', 'damage': 60}, {'name': 'X-Scissor', 'damage': 80}, {'name': 'Signal Beam', 'damage': 75}, {'name': 'Leech Life', 'damage': 80}]

    def attack(self):
        #Randomly choose attack based on move list
        attack_number=random.randint(1,4)
        if attack_number == 0:
            pass
        elif attack_number == 1:
            pass
        elif attack_number == 2:
            pass
        elif attack_number == 3:
            pass

        #Return the damage of the attack
        #return damage
        pass

    def take_damage(self):
        pass
    def heal(self):
        pass

    def __repr__(self):
        return f"{self.name} (HP: {self.hp}, Type: {self.primary_type}, Movelist: {self.moves})"
