import random

print("=" * 40)
print("      TREASURE HUNT ADVENTURE")
print("=" * 40)

print("RULES")
print("1. You start with 3 lives.")
print("2. You have 5 rounds.")
print("3. Find treasure to earn score.")
print("4. Collect coins.")
print("5. Avoid enemies.")
print("6. Game ends if lives become 0 or rounds become 0.")

lives = 3
score = 0
coins = 0
rounds = 5

while lives > 0 and rounds > 0:

    print("\n--------------------------")
    print("Lives :", lives)
    print("Score :", score)
    print("Coins :", coins)
    print("Rounds:", rounds)
    print("--------------------------")

    start = input("Enter 1 to Start : ")

    if start != "1":
        print("Invalid Input")
        continue

    print("\nChoose Direction")
    print("1. Straight")
    print("2. Left")
    print("3. Right")

    d = int(input("Enter Direction : "))

    if d < 1 or d > 3:
        print("Invalid Direction")
        continue

    #################################################
    ## DIRECTION 1
    #################################################

    if d == 1:

        event = random.randint(1,8)

        #################################################
        ## EVENT 1
        #################################################

        if event == 1:

            print("\nA Wild Wolf Appears!")

            print("1. Fight")
            print("2. Hide")
            print("3. Run")

            action = int(input("Choose : "))

            if action == 1:

                result = random.randint(1,2)

                if result == 1:

                    print("You defeated the wolf!")

                    score += 100
                    coins += 50

                    print("Treasure Chest Found!")

                    print("1.Open")
                    print("2.Ignore")

                    chest = int(input("Choice : "))

                    if chest == 1:

                        luck = random.randint(1,2)

                        if luck == 1:

                            print("Gold Treasure!")

                            score += 500
                            coins += 200
                            lives += 1

                        else:

                            print("It was a Trap!")

                            lives -= 1

                    elif chest == 2:

                        print("You safely continued.")

                        coins += 20

                    else:

                        print("Wrong Choice")

                else:

                    print("Wolf Defeated You")

                    lives -= 1

            elif action == 2:

                print("You Hid Behind A Rock")

                chance = random.randint(1,2)

                if chance == 1:

                    print("Wolf Left")

                    coins += 50

                else:

                    print("Wolf Found You")

                    lives -= 1

            elif action == 3:

                print("Running...")

                chance = random.randint(1,2)

                if chance == 1:

                    print("Escaped Successfully")

                else:

                    print("Wolf Caught You")

                    lives -= 1

            else:

                print("Invalid Choice")

        #################################################
        ## EVENT 2
        #################################################

        elif event == 2:

            print("\nYou Found An Old Treasure Map")

            print("1.Follow Map")
            print("2.Ignore")

            choice = int(input("Choice : "))

            if choice == 1:

                luck = random.randint(1,3)

                if luck == 1:

                    print("Hidden Temple Found")

                    score += 300
                    coins += 100

                elif luck == 2:

                    print("Secret Cave")

                    print("1.Enter")
                    print("2.Leave")

                    cave = int(input("Choice : "))

                    if cave == 1:

                        print("Treasure Found!")

                        score += 500
                        coins += 200
                        lives += 1

                    else:

                        print("You Left Safely")

                else:

                    print("Bandits Attacked")

                    lives -= 1

            elif choice == 2:

                print("You Continued Walking")

                coins += 20

            else:

                print("Invalid Choice")

        #################################################
        ## Remaining Events
        #################################################

        elif event == 3:
            print("Event 3 (Dragon) - Part 2")

        elif event == 4:
            print("Event 4 (Village) - Part 2")

        elif event == 5:
            print("Event 5 (River) - Part 2")

        elif event == 6:
            print("Event 6 (Bridge) - Part 2")

        elif event == 7:
            print("Event 7 (Merchant) - Part 2")

        elif event == 8:
            print("Event 8 (Trap) - Part 2")

    #################################################
    ## Direction 2
    #################################################

    elif d == 2:
        print("Direction 2 starts in Part 3")

    #################################################
    ## Direction 3
    #################################################

    elif d == 3:
        print("Direction 3 starts in Part 4")

    rounds -= 1

print("\n=========================")
print("GAME OVER")
print("=========================")
print("Final Score :", score)
print("Coins :", coins)
print("Lives :", lives)
 