def item_agent(battle_result: str):
    if battle_result == "victory":
        print("🏆 You found a magical sword! Added to inventory.")
    else:
        print("💨 You escaped with your life. No loot this time.")