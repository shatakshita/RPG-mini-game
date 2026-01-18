import streamlit as st
import random

# ---------- DATA ----------
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

archetypes = {
    "Specialist": (50, 13, 10),
    "Balanced": (25, 24, 24),
    "Wildcard": (11, 31, 31)
}

# ---------- LOGIC ----------
def create_character(name, strength, intelligence, charisma, fail_count):
    # --- Name validation ---
    if not isinstance(name, str) or name.strip() == "":
        return "The character should have a name 🥹", fail_count
    if len(name) > 10:
        return "The character name is too long 😵‍💫", fail_count
    if " " in name:
        return "The character name should not contain spaces 🙄", fail_count

    # --- Stat validation ---
    for stat in (strength, intelligence, charisma):
        if not isinstance(stat, int):
            return "All stats should be integers 😤", fail_count
        if stat < 1 or stat > 100:
            return "Stats must be between 1 and 100 😡", fail_count

    total = strength + intelligence + charisma
    if total != 73:
        fail_count += 1
        insult_index = min(fail_count - 1, len(insults)-1)
        message = (
            f"{insults[insult_index]}\n\n"
            "HINT: Sum the number of books in The Iliad, "
            "the number of pilgrims in The Canterbury Tales, "
            "and the number of years a man must stay away from home in The Odyssey\n"
            "Try again 😝"
        )
        return message, fail_count

    # --- Check archetypes ---
    exact_match = None
    partial_match = False
    for arch, stats in archetypes.items():
        if (strength, intelligence, charisma) == stats:
            exact_match = arch
        elif sorted((strength, intelligence, charisma)) == sorted(stats):
            partial_match = True

    # --- Partial match hint ---
    if partial_match and not exact_match:
        return (
            "You were smart to figure out the numbers, but not enough "
            "to unlock the 3 legendary characters.\n"
            "To unlock them, find the correct order of the numbers! 😉", fail_count
        )

    # --- Final archetype ---
    archetype_name = exact_match if exact_match else "Custom Build"

    max_dots = 10
    def scale(x): return int(x / 100 * max_dots)

    # --- Dot representation ---
    result = f"{name} ({archetype_name})\n"
    result += "STR " + full_dot * scale(strength) + empty_dot * (max_dots - scale(strength)) + "\n"
    result += "INT " + full_dot * scale(intelligence) + empty_dot * (max_dots - scale(intelligence)) + "\n"
    result += "CHA " + full_dot * scale(charisma) + empty_dot * (max_dots - scale(charisma))

    return f"Character created successfully 🎀\n\n{result}", fail_count

# ---------- STREAMLIT APP ----------
st.set_page_config(page_title="RPG Mini Game", page_icon="🎲", layout="centered")

# Track fails
if "fail_count" not in st.session_state:
    st.session_state.fail_count = 0

# ---------- STYLING ----------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #a398c2;
}
[data-testid="stSidebar"] {
    background-color: #a398c2;
}
.main-popup {
    background-color: #f0e6ff;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 5px 5px 20px rgba(0,0,0,0.4);
}
h1 {
    text-align: center;
    color: #4b2e83;
}
.stTextInput>div>input, .stNumberInput>div>input, .stButton>button {
    background: #fff;
    color: #000;
    border-radius: 5px;
    border: 1px solid #aaa;
    padding: 5px 8px;
}
.stButton>button:hover {
    background-color: #ddd;
}
</style>
""", unsafe_allow_html=True)

# ---------- POPUP AREA ----------
st.markdown('<div class="main-popup">', unsafe_allow_html=True)

st.title("🎲 RPG Mini Game")

name = st.text_input("Name? Better than yours:")
strength = st.number_input("Strength? Be honest (number):", min_value=1, max_value=100, step=1)
intelligence = st.number_input("Intelligence? No lying (number):", min_value=1, max_value=100, step=1)
charisma = st.number_input("Charisma? We can tell (number):", min_value=1, max_value=100, step=1)

if st.button("Create Character"):
    result, st.session_state.fail_count = create_character(
        name, strength, intelligence, charisma, st.session_state.fail_count
    )
    st.text_area("Result", value=result, height=250)

st.markdown('</div>', unsafe_allow_html=True)
