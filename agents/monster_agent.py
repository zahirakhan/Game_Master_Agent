from tools.game_tools import roll_dice

def monster_agent(location: str) -> str:
    print(f"A monster attacks in the {location}!")
    player_roll = roll_dice()
    monster_roll = roll_dice()
    print(f"You rolled a {player_roll}, monster rolled a {monster_roll}.")
    if player_roll >= monster_roll:
        print("You defeated the monster!")
        return "victory"
    else:
        print("You were defeated... but survived!")
        return "defeat"