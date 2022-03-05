from multiprocessing.sharedctypes import Value


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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. \n")


def get_choice(instruction, *choices):
    print(instruction)
    for id, choice in enumerate(choices):
        print(id+1, choice)

    while True:
        user_input = input('-> ')
        try:
            if user_input == '0':
                raise IndexError
            return choices[int(user_input)-1]
        except ValueError:
            print('Value error, enter a number not text')
        except IndexError:
            print('No choice available for the choosen number')

# Choice 1
left_or_right = get_choice(
    'You are at a crossroad. Where do you want to go?',
    'left',
    'right').lower()


if left_or_right == 'left':
    # Choice 2
    story_text = ("You have come to a lake. There is an island in the"
                  "middle of the lake. What you want to do wait for a boat."
                  "or swim across")
    wait_or_swim = get_choice(
        story_text,
        'Wait',
        'Swim').lower()

    if wait_or_swim == 'wait':
        # Choice 3
        door_color = get_choice(
            'You arrive at the island unharmed. There is a house \
            with 3 doors. One red, one yellow and one blue. \
            Which colour do you choose?',
            'Yellow',
            'Blue',
            'Red').lower()

        if door_color == 'yellow':
            print('You Win 🥳')
        else:
            print('....Game Over 😭')

    else:
        print('Attacked....Game Over 😭')
else:
    print('Fall into a hole.....Game Over 😭')
