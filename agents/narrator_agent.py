from tools.game_tools import generate_event

def narrator_agent(player_name: str) -> str:
    print(f"Welcome, {player_name}, to the land of Eldoria!")
    print("You stand at a crossroads. Do you choose:\\n1. Forest\\n2. Cave\\n3. Castle")
    choice = input("Enter 1, 2, or 3: ")
    location_map = {"1": "forest", "2": "cave", "3": "castle"}
    location = location_map.get(choice, "forest")
    event = generate_event(location)
    print(f"You enter the {location}.\\n{event}")
    return location
