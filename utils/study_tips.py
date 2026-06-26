import random

tips = [
    "📚 Study for 25 minutes, then take a 5-minute break.",
    "🧠 Teach someone else what you learned today.",
    "✍️ Write short notes after every study session.",
    "🎯 Focus on understanding, not memorizing.",
    "💧 Drink enough water while studying.",
    "📱 Keep your phone away during study time.",
    "🌙 Sleep well before an exam.",
    "🔁 Revise within 24 hours for better retention.",
    "📖 Practice active recall instead of rereading.",
    "🎧 Study in a distraction-free environment."
]

def get_study_tip():
    return random.choice(tips)