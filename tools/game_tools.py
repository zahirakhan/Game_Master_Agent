import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def generate_event(location: str) -> str:
    events = {
        "forest": "A wild goblin appears!",
        "cave": "A giant spider descends from the ceiling!",
        "castle": "An undead knight blocks your path!"
    }
    return events.get(location, "A mysterious fog surrounds you...")