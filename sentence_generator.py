import random

print("ברוך הבא למחולל המשפטים!")

name = input("הכנס שם: ")

sentences = [
    f"{name} יצא למסע אפי להציל את העולם!",
    f"היום {name} שותה קפה כמו מתכנת אמיתי.",
    f"{name} תכף ממציא אפליקציה שתשנה את העולם!",
    f"{name} הופך לגיבור־על בעזרת פייתון!",
    f"כש{name} מתכנת – המחשב מקשיב."
]

chosen = random.choice(sentences)

print(chosen)