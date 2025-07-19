from agents.narrator_agent import narrator_agent
from agents.monster_agent import monster_agent
from agents.item_agent import item_agent

def main():
    print("🎮 Welcome to Fantasy Adventure Game 🎮")
    name = input("Enter your hero's name: ")
    location = narrator_agent(name)
    monster_result = monster_agent(location)
    item_agent(monster_result)

if __name__ == "__main__":
    main()