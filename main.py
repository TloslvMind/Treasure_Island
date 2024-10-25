print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

print("You're at a crossroad. Where do you want to go?")
way =  input('      Type "left" to go left, "right" to go right\n').lower()
if way == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    way_to_move = input('      Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if way_to_move == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door = input("      One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if door == 'yellow':
            print("You found the treasure! You win! Congrats!")
        elif door == 'red':
            print("It's a room full of fire. Game over.")
        elif door == 'blue':
            print("You entered a room of beasts. Game over.")
        else:
            print("There is no such a door! You lose. Game over.")
    else:
        print("You were destroyed by piranhas. Game Over.")
else:
    print("You were eaten by dinosaur. Game Over.")