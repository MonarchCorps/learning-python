print("It's midnight, and you stand before an old, crumbling mansion. \nThe door creaks open as if inviting you inside.\n")

first_action = input("Do you want to: \nENTER through the front door CIRCLE around to the back LEAVE immediately?\n> ").lower()

second_action = ""
third_action = ""

default_error_text = "The action you entered is not part of the following."

# if action is part of any of this enums

if first_action in ("enter", "circle", "leave"):

    # enter block of code

    if first_action == "enter":
        print("\nYou push open the heavy wooden door and step into a dusty hallway. \nA chandelier sways slightly above you. \nTo your left is a LIBRARY, and to your right is a STAIRCASE leading upward.\n")
        second_action = input("Do you go to the LIBRARY or the STAIRCASE?\n> ").lower()
        
        # if action is part of any of this enums
        if second_action in ("library", "staircase"):

            # if action is library
            if second_action == "library":
                print("\nYou walk into the library. Thousands of books line the shelves. \nOn the table lies an old DIARY. \nYou also notice a BROKEN WINDOW.\n")
                third_action = input("Do you READ the diary or CLIMB out the broken window?\n> ").lower()

                # if action is part of any of this enums

                if third_action in ("read", "climb"):

                    # if action is read

                    if third_action == "read":
                        print("\nYou open the diary. It whispers your name! \nThe words rearrange themselves: 'Leave… or stay forever.' \nSuddenly, the door slams shut.  \nYou are trapped forever. GAME OVER.")

                    # else
                    else:
                        print("\nYou climb out the broken window, scraping your hands, but escape into the night. \nYou survived! 🎉")

                # else display an error message
                else:
                    print(f"{default_error_text} READ or CLIMB")

            # if action is staircase
            elif second_action == "staircase":
                print("\nYou ascend the creaky staircase. At the top are two doors: LEFT and RIGHT.\n")
                third_action = input("Which door do you open?\n> ").lower()

                # if action is part of any of this enums

                if third_action in ("left", "right"):
                    
                    # if action is left
                    if third_action == "left":
                        print('\nThe left door opens into a candlelit bedroom. \nA ghostly figure rises from the bed and whispers, "Thank you for freeing me." \nThe ghost disappears, leaving behind a golden key. \nYou survive and gain treasure! 🎉')

                    # else
                    elif third_action == "right":
                        print("\nYou open the right door. \nA cold wind pushes you inside as the floor gives way beneath you. \nYou fall into darkness. GAME OVER.")

                # else display an error message
                else:
                    print(f"{default_error_text} LEFT or RIGHT")

        # else display an error message
        else:
            print(f"{default_error_text} LIBRARY or STAIRCASE")

    # circle block of code
    
    elif first_action == "circle":
        print("\nYou creep around to the back of the mansion. \nThere’s a cellar door and a broken fence leading into the woods.\n")
        second_action = input("Do you ENTER the cellar or RUN into the woods?\n> ").lower()
        
        # if action is part of any of this enums
        if second_action in ("enter", "run"):

            # if action is enter
            if second_action == "enter":
                print("\nThe cellar is damp and smells of mildew. \nYou see a chest in the corner and a staircase leading deeper underground.\n")
                third_action = input("Do you OPEN the chest or DESCEND the stairs?\n> ").lower()

                # if action is part of any of this enums

                if third_action in ("open", "descend"):

                    # if action is read

                    if third_action == "open":
                        print("\nYou open the chest and discover it filled with rotten bones. \nSuddenly, skeletal hands grab you! GAME OVER.")

                    # else
                    else:
                        print("\nYou descend deeper into the cellar, finding a secret passage out of the mansion. \nYou escape safely. 🎉")

                # else display an error message
                else:
                    print(f"{default_error_text} OPEN or DESCEND")

            # if action is run
            elif second_action == "run":
                print("\nYou run into the woods as the mansion groans behind you. \nBranches scratch your arms, but you spot a small cabin ahead.\n")
                third_action = input("Do you HIDE in the cabin or KEEP running?\n> ").lower()

                # if action is part of any of this enums

                if third_action in ("hide", "keep"):
                    
                    # if action is hide
                    if third_action == "hide":
                        print('\nYou hide in the cabin. It’s abandoned but safe. \nYou make it through the night. 🎉')

                    # else
                    if third_action == "keep":
                        print("\nYou keep running until you’re hopelessly lost in the forest. \nEventually, exhaustion takes you. GAME OVER.")

                # else display an error message
                else:
                    print(f"{default_error_text} HIDE or KEEP")

        # else display an error message
        else:
            print(f"{default_error_text} ENTER or RUN")

    # leave block of code
    elif first_action == "leave":
        print("\nYou turn away from the mansion, deciding not to enter. \nThe air feels heavy, and you swear you hear faint laughter behind you. \nBut you walk away unharmed. \nSometimes, the bravest choice is not to play the game. 🎉")

# else display an error message
else: 
    print(f"{default_error_text} ENTER or CIRCLE or LEAVE ")