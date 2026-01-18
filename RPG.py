import random

insults = [
    "That was embarrassing 💀",
    "Are you even trying? LMAO 😐",
    "That character would not survive 5 minutes.",
    "I’ve seen NPCs do better.",
    "Bold choices. Wrong ones, but bold.",
    "Interesting… in a bad way.",
    "The dice are judging you."
]

full_dot = '●'
empty_dot = '○'

# Three special archetypes
archetypes = {
    "Specialist": (50, 13, 10),
    "Balanced": (25, 24, 24),
    "Wildcard": (11, 31, 31) 
}

def create_character(name, strength, intelligence, charisma):
    # --- Name validation ---
    if not isinstance(name, str):
        return "The character name should be a string 😭"
    if name == '':
        return "The character should have a name 🥹"
    if len(name) > 10:
        return "The character name is too long 😵‍💫"
    if ' ' in name:
        return "The character name should not contain spaces 🙄"

    # --- Stat validation ---
    for stat in (strength, intelligence, charisma):
        if not isinstance(stat, int):
            return "All stats should be integers 😤"
        if stat < 1 or stat > 100:
            return "Stats must be between 1 and 100 😡"

    total = strength + intelligence + charisma
    if total != 73:
        return "Something feels… off."

    # --- Check archetypes ---
    exact_match = None
    partial_match = False
    for name_, stats in archetypes.items():
        if (strength, intelligence, charisma) == stats:
            exact_match = name_
        elif sorted((strength, intelligence, charisma)) == sorted(stats):
            partial_match = True

    if partial_match and not exact_match:
        return "You were smart to figure out the numbers, but not enough to unlock the 3 legendary characters.\nTo unlock them, find the correct order of the numbers! 😉"

    archetype_name = exact_match if exact_match else "Custom Build"

    # --- Display ---
    max_dots = 10
    scaled_strength = int(strength / 100 * max_dots)
    scaled_intelligence = int(intelligence / 100 * max_dots)
    scaled_charisma = int(charisma / 100 * max_dots)

    result = f"{name} ({archetype_name})\n"
    result += 'STR ' + full_dot*scaled_strength + empty_dot*(max_dots - scaled_strength) + '\n'
    result += 'INT ' + full_dot*scaled_intelligence + empty_dot*(max_dots - scaled_intelligence) + '\n'
    result += 'CHA ' + full_dot*scaled_charisma + empty_dot*(max_dots - scaled_charisma)

    return result

# -------- LOOP --------
while True:
    name = input("Name? Better than yours: ")
    strength = int(input("Strength? Be honest (number): "))
    intelligence = int(input("Intelligence? No lying (number): "))
    charisma = int(input("Charisma? We can tell (number): "))

    result = create_character(name, strength, intelligence, charisma)

    if full_dot in result:
        print("\nCharacter created successfully 🎀\n")
        print(result)
        break
    else:
        print("\n" + result)
        print(random.choice(insults)+"\n")
        print("HINT: Sum the number of books in The Iliad, the number of pilgrims in The Canterbury Tales, and the number of years a man must stay away from home in The Odyssey\n")
        print("Try again 😝\n")
