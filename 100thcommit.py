import random

quotes = [
    "Keep going, you're doing great!",
    "Code. Debug. Repeat.",
    "Small steps every day = big results.",
    "Consistency beats talent.",
    "Dream it. Build it."
]

def get_quote():
    return random.choice(quotes)

print("💡 Your Motivation for Today:")
print(get_quote())