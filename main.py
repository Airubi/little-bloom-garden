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
print("\n🌱 Which flower would you like to plant?")

for i, flower in enumerate(flowers, start=1):
    print(f"{i}. {flower}")

choice = input("\nEnter the flower number: ")

if choice.isdigit():
    number = int(choice)

    if 1 <= number <= len(flowers):
        planted_flower = flowers[number - 1]

        print(f"\nYou planted {planted_flower} 💗")

        water = input("Would you like to water it? (y/n): ").lower()

        if water == "y":
            print(f"You watered {planted_flower} 💧")
            print("Your flower is happy! 🌸")

        elif water == "n":
            print("Maybe we can water it later. 🌱")

        else:
            print("Please enter y or n.")

    else:
        print("Sorry! This flower number does not exist.")

else:
    print("Please enter a number only!")
    
