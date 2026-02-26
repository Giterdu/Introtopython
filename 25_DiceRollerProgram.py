import random
#print(" \u25cf \u250c \u2500 \u2510 \u2502 \u2514 \u2518")
# the code above prints the following unicode characters: ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),
    2: ("┌─────────┐", 
        "│  ●      │", 
        "│         │", 
        "│      ●  │", 
        "└─────────┘"),
    3: ("┌─────────┐", 
        "│  ●      │", 
        "│    ●    │", 
        "│      ●  │", 
        "└─────────┘"),
    4: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│         │", 
        "│  ●   ●  │", 
        "└─────────┘"),
    5: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│    ●    │", 
        "│  ●   ●  │", 
        "└─────────┘"),
    6: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

#for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]): #this line in charge of printing every tuple
#        print(line)
#mute lines 51-53 and enter the following code to print each individual dice roll on the same line:

for line in range(5): #because each image of the dice contains 5 lines
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"total: {total}") #prints the sum total of the numbers you get from however number of dice you roll after printing the invidivual dice rolls on their own line 