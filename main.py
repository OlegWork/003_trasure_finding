print('''

       ________   ________    _________  ____________;_
      - ______ \ - ______ \ / _____   //.  .  ._______/
     / /     / // /     / //_/     / // ___   /
    / /     / // /     / /       .-'//_/|_/,-'
   / /     / // /     / /     .-'.-'
  / /     / // /     / /     / /
 / /     / // /     / /     / /
/ /_____/ // /_____/ /     / /
\________- \________-     /_/
''')

print("Welcome to the Treasure Island")
print("Your mission is to find the Treasure")
first_crossroad = input("You're at the cross road. Where do you want to go? (\"left\" or \"right\")\n")

if first_crossroad == "left":
    first_crossroad_left = input("You at the lake. Do you want to \"swim\" or \"wait\"\n")
    if first_crossroad_left == "wait":
            wait_boat = input("Boat came to you. Now you are in the cave. Chose \"cave1\" or \"cave2\"\n")
            if wait_boat == "cave1":
                print("Great you find a huge chunk of gold")
            else:
                print("You were killed by a troll!")
    else:
        print("Shark eat you!")
else:
    print("Wrong choose. You were killed by robbers")