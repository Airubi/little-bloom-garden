import random

print("🌷 Welcome to Ai's Little Garden 🌷")

name = input("What is your name? ")

flowers = ["Tulip 🌷", "Sunflower 🌻", "Daisy 🌼", "Sakura 🌸", "Rose 🌹", "Lavender 🪻"]

print(f"\nHello, {name}! Welcome home. 💗")
print("\nYour garden has:")

for flower in flowers:
    print(f"- {flower}")

print("\n✨ Today's special flower:")
print(random.choice(flowers))
