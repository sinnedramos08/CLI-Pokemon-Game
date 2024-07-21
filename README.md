# CLI Pokemon Battle Game
## Introduction
CLI Pokemon Battle Game is a text-based game implemented in Python that simulates Pokemon battles. This game utilizes object-oriented programming (OOP) principles to manage game logic, Pokemon attributes, and battle mechanics.

## Features
1. Choose from multiple Pokemon with unique attributes and moves.
2. Engage in turn-based battles with wild Pokemon.
3. Capture wild Pokemon and add them to your team.
4. Heal and manage your Pokemon team.
5. Navigate a board where each step can lead to a Pokemon encounter.
6. Increase your Pokemon's health as you explore.

## Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/cli-pokemon-game.git
cd cli-pokemon-game
```
2. Ensure you have Python 3.6+ installed on your machine.

## Usage
1. Navigate to the project directory.
2. Run the game script:
```bash
python main.py
```
3. Follow the on-screen instructions to play the game.

## Game Mechanics
### Board Navigation
- At the start of the game, input your desired board dimensions:
  - Width: Specify the width of the game board.
  - Height: Specify the height of the game board.
  - Number of Grass Tiles: Determine how many grass tiles (where Pokémon encounters occur) will be on the board. 
- Move around the board using w, a, s, d keys.
- Each move consumes a step and heals your Pokemon team by 30 HP (up to their maximum HP).

## Pokemon Battles
Engage in battles with wild Pokemon encountered on the board. In each battle, you have several strategic options:
1. **Fight** - Choose from your Pokemon's unique moves to attack the wild Pokemon. Each move has different damage values and effects
  - **Player's Turn** - Select a move from your Pokemon's move list. The move deals a specified amount of damage to the wild Pokemon.
  - **Wild Pokemon's Turn** - The wild Pokemon will randomly select one of its moves to attack your Pokemon.
2. **Run** - Avaoid fighting the wild Pokemon.
3. **Throw Pokeball** - Try to capture the wild Pokemon. The success rate depends on the wild Pokemon's remaining HP.
  - A capturing timer and chance system determine if the capture is successful.
4. **Heal** - Use a heal to restore 100 HP to your active Pokemon (up to their maximum HP).

The battle continues in a turn-based manner until one of the Pokemon faints, you capture the wild Pokemon, or you decide to run away.

## Future Improvements
1. **Type-Based Damage System**: Improve the battle mechanics by incorporating a type-based damage system. Certain types are strong or weak against others. For example:
  - Super Effective: Attacks deal double damage when the attacker's type has an advantage over the defender's type (e.g., Water-type moves against Fire-type Pokemon).
  - Not Very Effective: Attacks deal half damage when the attacker's type is at a disadvantage (e.g., Fire-type moves against Water-type Pokemon).
  - No Effect: Some moves may have no effect depending on the type match-up (e.g., Electric-type moves against Ground-type Pokemon).
2. **Implement More Pokemon Types and Moves**: Expand the variety of Pokemon and moves.
3. **Enhance Battle Mechanics with Status Effects and Items**: Introduce status effects (e.g., paralysis, poison) and items (e.g., potions, berries).
4. **Leveling Up**: Introduce a leveling system where Pokemon gain experience points (XP) from battles.
5. **Evolving Pokemon**: Implement a feature where Pokemon can evolve into more powerful forms when they reach certain levels or meet specific conditions. Evolution will enhance a Pokemon's stats and may grant new moves
