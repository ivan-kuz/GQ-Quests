import sys
import time
i = set()#Inventory
#Inventory won't be availible in version 0.1 (the current version)
def start():
    print("---------------------------------------------------------")
    i = set()#Inventory
    print("Welcome to my text quest game!")
    print("At any point in the game press q to quit, r to restart and i to see your inventory")
    time.sleep(2)
    first_stage()
def first_stage():
    print("------FIRST-STAGE------")
    print("The year is 2222. The Martians are invading Earth.")
    first_input = input("You manage to run away from Martian assasins and you approach a junction. Do you want to go left or right?")
    if first_input == "left":
        print("You walk for 3 days in this direction, when suddenly you approach a Sphinks.")
        def left1():
            second_input = input("The Sphinks proposes to you her famous riddle - 'When I eat, I'm fine, when I drink, I die. What am I? If you don't solve the riddle you get eaten!")
            if second_input == "fire":
                print("It great that you figured it out! Your intellect made the Sphinks feel so ashamed that she exiled herself!")
                def left2():
                    third_input = input("You find out that, by getting rid of the Sphinks, saved the city of Totusmortuus from death. The city's inhabitants want you to become king. Do you accept the offer?")
                    if third_input in ["Yes", "yes", "accept", "Accept"]:
                        print("Oh no. You forgot that 'totus mortuus' in Latin means 'completely dead'! The city's inhabitants are actually dead Martians. They kill you and you become one of them.")
                        print("GAME OVER!")
                        start()
                    elif third_input in ["No", "no", "don't accept", "Don't accept"]:
                        print("It's good that you remembered that 'totus mortuus' in Latin means 'completely dead'! You know that humans are searching for this 'City of Dead Martians' and thus you need to report this to the humans.")
                        second_stage()
                    elif third_input == "q":
                        print("GAME OVER!")
                    elif third_input == "r":
                        start()
                    elif third_input == "i":
                        if i == set():
                            print("There are no items in your inventory")
                            left2()
                        else:
                            print("You have: " + i)
                            left2()
                    else:
                        print("Sorry. You have to pick either 'yes' or 'no'")
                        left2()
                left2()
            elif second_input == "q":
                print("GAME OVER!")
            elif second_input == "i":
                if i == set():
                    print("There are no items in your inventory")
                    left1()
                else:
                    print("You have: " + i)
                    left1()
            elif second_input == "r":
                start()
            else:
                print("Unfortunally you are wrong. The answer is 'fire' and the Sphinks eats you. You die")
                print("GAME OVER")
                start()
        left1()
    elif first_input == "right":
        print("You walk for three minutes in this direction, when you approach an ancient building. It is a small bungalow. ")
        def right1():
            second_input = input("It has a sign on it that reads 'NBSUJBO IFBERVBSUFST. BMM IVNBOT UIBU FOUFS XJMM EJF!' Do want to go in or hide?")
            if second_input == "HIDE" or second_input == "Hide" or second_input == "hide":
                print("Wise choice! (The sign actually reads 'MARTIAN HEADQUARRTERS. ANY HUMANS THAT COME IN WILL DIE!' in encrypted form)")
                def right2():
                    third_input = input("So, you wait and see the head Martian (Mar. Nichtstark) coming out of the building. Do you want to fight him?")
                    if third_input in ["fight him", "yes", "Fight him", "Yes"]:
                        print("It's good that you remembered that 'nicht stark' in Martian (and in German) 'not strong'! You easily kill him with one punch in the head. You now need to report this to the humans.")
                        second_stage()
                    elif third_input in ["No","no"]:
                        print("Oh no. You forgot that in Martian (and in German) 'nicht stark' means 'not strong'. Now, because you haven't killed the head Martian, he ends the world with one order. You die, too")
                        print("GAME OVER")
                        start()
                    elif third_input == "r":
                        start()
                    elif third_input == "q":
                        print("GAME OVER!")
                    elif second_input == "i":
                        if i == set():
                            print("There are no items in your inventory")
                            right2()
                        else:
                            print("You have: " + i)
                            right2()
                    else:
                        print("Sorry, you have to pick either 'yes' or 'no'.")
                        right2()
                right2()
            elif second_input in ["Go in", "go in", "GO IN"]:
                print("Oh no! (The sign actually reads 'MARTIAN HEADQUARRTERS. ANY HUMANS THAT COME IN WILL DIE!' in encrypted form) The Martian guards kill you instantly with their hi-tech guns.")
                print("GAME OVER")
                start()
            elif second_input == "q":
                print("GAME OVER!")
            elif second_input == "r":
                start()
            elif second_input == "i":
                if i == set():
                    print("There are no items in your inventory")
                    right1()
                else:
                    print("You have: " + i)
                    right1()
            else:
                print("Sorry, you have to either pick 'go in' or 'hide'")
                right1()
        right1()
    elif first_input == "q":
        print("GAME OVER!")
    elif first_input == "i":
        if i == set():
            print("There are no items in your inventory")
            first_stage()
        else:
            print("You have: " + i)
            first_stage()
    elif first_input == "r":
        start()
    else:
        print("Sorry. You have to pick either left or right")
        first_stage()
def second_stage():
    print("------SECOND-STAGE------")
    print("After walking for a whole month, you arrive at a large, underground house. It is the main human base on this continent.")
    fourth_input = input("When you go in, you remember that you are very hungry and thirsty. Do you go into the restaurant or into the bar?")
    fourth_input.lower()
    if fourth_input == "restaurant":
        print("You're really delighted to eat - you haven't eaten anything but berries and nuts in the last month! Everything seems perfect... until your hear a Martian bomb falling.")
        def restaurant1():
            fifth_input = input("You realise that you have to do something urgently. Do you hide under the piano or do you hold on to it?")
            fifth_input.lower()
            if fifth_input == "hide under the piano" or fifth_input == "hide under it" or fifth_input == "hide":
                print("It's great you remembered this from World War Two history - the bomb hits the piano, but you don't get a single scar")
                def restaurant2():
                    sixth_input = input("Now you can go what you were planning to do before - report info to the 'Head Earthling'. But you realise that you have forgotten it (and LOOOOADS of other things as well) and you should visit the doctor. If the name your condition correctly, the doctor will cure you. If you don't you'll become insane.")
                    sixth_input.lower()
                    if sixth_input in ["dementia", "amnesia", "alzheimer's", "parkinson's","ptsd"]:
                        print("You named the correct disease and the doctor cures you. You remember everything and rush to the 'Head Earthling's' office. When you arrive there , you feel that there's something in the air...")
                        final_stage()
                    elif sixth_input == "r":
                        start()
                    elif sixth_input == "q":
                        print("GAME OVER!")
                    elif sixth_input == "i":
                        if i == set():
                            print("Your inventory is empty.")
                            restaurant2()
                        else:
                            print("You have: " + i)
                            restaurant2()
                    else:
                        print("Oh no, you didn't name disease correctly and the doctor gets angry at you. He kills you with his sharp scalpel. You die.")
                        print("GAME OVER!")
                        start()
                restaurant2()
            elif fifth_input == "hold on to it" or fifth_input == "hold on to the piano":
                print("Oh no! You forgot how people survived the bombings in World War Two! The bomb hits you directly and you get blown into pieces.")
                print("GAME OVER!")
                start()
            elif fifth_input == "r":
                start()
            elif fifth_input == "q":
                sys.exit()
            elif fifth_input == "i":
                if i == set():
                    print("Your inventory is empty")
                    restaurant1()
                else:
                    print("You have: " + i)
                    restaurant1()
            else:
                print("Please enter either 'hold onto it' or 'hide under it'.")
                restaurant1()
        restaurant1()
    elif fourth_input == "bar":
        print("You're really delighted to drink something other that water for once. Everything seems perfect... until you see a Martian coming at you with a massive sword.")
        def bar1():
            fifth_input = input("You look around for objects to defend yourself with - and two shields catch your eye. One shield is made out of Cesium and one is made out of Chromium. Which one do you defend yourself with?")
            fifth_input.lower()
            if fifth_input in ["chromium shield", "chromium"]:
                print("Great! You remembered from your chemistry lessons that chromium is the hardest metal on Earth - the Martian sword breaks when it hits your shield and the Martian flees, acidentaly leaving something on the floor.")
                def bar2():
                    print("You're really delighted that you scared the Martian away. But unfortunately, all humans that were in the bar died, except you and a random biologist.")
                    sixth_input = input("Miss Ews (that random biologist that survived) tells you that the object the Martian dropped is a 'vipera berus'. Now you suddenly remember that you need to buy a pet for your child. Do you pick up the 'vipera berus'?")
                    sixth_input.lower()
                    if sixth_input in ["no", "don't pick up"]:
                        print("HOORAY! You remembered from your biology lessons that the normal name for a 'vipera berus' is 'common viper'! If you would have touched it, it would have stung you. But suddenly you remember that the Head Earthling collects these vipers. You need to tell him that there's one here. But there's something in the air... ")
                        final_stage()
                    elif sixth_input in ["yes","pick up", "don't pick up"]:
                        print("Oh no! You forgot that the normal name for a 'vipera berus' is 'common viper'! As you pick it up, it hisses at you and kills you with its poison. You die instantly.")
                        print("GAME OVER!")
                        start()
                    elif sixth_input == "r":
                        start()
                    elif sixth_input == "q":
                        print("GAME OVER!")
                    elif sixth_input == "i":
                        if i == set():
                            print("Your inventory is empty")
                            bar2()
                        else:
                            print("You have: " + i)
                            bar2()
                    else:
                        print("Sorry, you an either pick 'yes' or 'no'")
                        bar2()
                bar2()
            elif fifth_input in ["cesium shield","cesium"]:
                print("Oh no! You forgot from your chemistry lessons that cesium is one of the most softest metals on Earth! The Martian slices the shield and you with it using his sword. You die.")
                print("GAME OVER!")
                start()
            elif fifth_input == "r":
                start()
            elif fifth_input == "q":
                print("GAME OVER!")
            elif fifth_input == "i":
                if i == set():
                    print("Your inventory is empty")
                    bar1()
                else:
                    print("You have: " + i)
                    bar1()
            else:
                print("Sorry, you have to pick either 'chromium shield' or 'cesium shield'")
                bar1()
        bar1()
    elif fourth_input == "r":
        start()
    elif fourth_input == "q":
        print("GAME OVER!")
    elif fourth_input == "i":
        if i == set():
            print("There are no items in your inventory")
            second_stage()
        else:
            print("You have: " + i)
            second_stage()
    else:
        print("Sorry, you have to either pick 'bar' or 'restaurant'")
        second_stage()
def final_stage():
    print("------FINAL-STAGE------")
    print("After an hour of searching through the bombed base, you find the Head Earthling's office. Luckily, not a single bomb has hit it.")
    seventh_input = input("You can see two doors in front of you - a door that says 'Head Earthling' and a door that says 'Head Earthing - for NBSUJBO use only! Which one do you go in: the first or the second door?")
    seventh_input.lower()
    if seventh_input in ["first", "first door", "the first door"]:
      print("You slowly open the door, only to find out that the Head Earthling is not at his desk. Not even his bodyguards are there. But the AK 47 (which was the Head's oldest gun in his collection) is still on the shelf.")
      def first1():
        eighth_input = input("Being very polite, you ring the bell and sit down patiently. However, you notice an old book on his table: it is called 'The Martian Chronicles'. Who is the author of that book?")
        eighth_input.lower()
        if eighth_input in ["ray bradbury", "bradbury"]:
          print("As you mumble the word 'bradbury', a shelf collapses which reveals the entrance to a secret chamber.")
          def first2():
            print("Inside, you catch a Martian putting on a mask of the Head Earthling. THAT was his secret!!! The Head Earthling died a few days ago and a Martian took his place!")
            ninth_input = input("The Martian slowly turns around, thinking you are his assistant who is supposed to return from the battlefield. But as he sees an ordinary Earthling, he frowns and reaches out for you with his dagger. By instinct, you grab the antique AK 47 from the shelf. But what ammo do you use: the 7.62 or the 12 gauge?")
            if ninth_input in ["7.62", "7.62 ammo"]:
              print("Congratulations! You picked the correct ammo type and you shoot the Martian in the heart. Suddenly, his (Martian) assistant rushes in but you shoot him down too.")
              print("Outside, the Earthlings praise you and accept you as their leader. Battle after battle you free people from Martian rule and by 2223 the Earth is free once again!")
              print("You have won the game! Congratulations!")
            elif ninth_input in ["12 gauge", "12 gauge ammo"]:
              print("Oh no! This ammunition does not fit the AK 47! Before you even try to step back, a martian dagger slices your lungs. You die, of course.")
              print("GAME OVER!")
              start()
            elif ninth_input == "r":
              start()
            elif ninth_input == "q":
              print("GAME OVER!")
            elif ninth_input == "i":
              if i == set():
                print("Your inventory is empty")
                first2()
              else:
                print("You have: " + i)
                first2()
            else:
              print("Sorry, please pick either '12 gauge' or '7.62'.")
              first2()
          first2()
        elif eighth_input == "r":
          start()
        elif eighth_input == "q":
          print("GAME OVER!")
        elif eighth_input == "i":
          if i == set():
            print("Your inventory is empty")
            first1()
          else:
            print("You have: " + i)
            first1()
        else:
          print("What on earth did you say...?! That was the Head's secret 'smart home' command for suicide. Carbon monoxide is released through the walls, and you die almost instantly. And there's no one around to put a grave for you!")
          print("GAME OVER!")
          start()
      first1()
    elif seventh_input in ["second", "second door", "the second door"]:
      print("Reach out to open the door, but then you realise that it is locked. To your surprise, the lock is an old one, which only requires a 4 digit code to open it.")
      def second1():
        eighth_input = input("As you are an avid codebreaker, the lock doesn't stop you. Suddenly, you remember that the Head Earthling likes collecting antique mobile phones. When was the first iPhone released?")
        eighth_input.lower()
        if eighth_input == "2007":
          print("It's great tht you remember it: the door opens instantly! Unfortunately for you, there's a meeting going on inside. All men present are Martians.")
          def second2():
            print("But luckily, you're very tall, so they mistake you for one of their kind, and you sit down at the end of the table, by a computer. You're not fluent in Martian, but you make out words like 'death', 'all', 'humans' and 'now'")
            ninth_input = input("You feel like the earth is in great danger and you need to act fast. On the desktop, you see two programs: mySQL and Django. Which one is used for interacting with databases? You'll want to delete that one!")
            ninth_input.lower()
            if ninth_input == "mysql":
              print("Congrats, that was the right one! The Martians panic, run to their ship and fly off. There are no more Martian generals left on Earth, and that means the remaining soldiers would be easy to defeat!")
              print("Outside, the Earthlings praise you and accept you as their leader. Battle after battle you free people from Martian rule and by 2223 the Earth is free once again!")
              print("You have won the game! Congratulations!")
            elif ninth_input == "django":
              print("Oh no! Django is used to ceate dynamic webpages! You delete the Martian website, but it does nothing except reveal that YOU are an Earthling! The Martians kill you, and then everyone on earth.")
              print("GAME OVER!")
              start()
            elif ninth_input == "r":
              start()
            elif ninth_input == "q":
              print("GAME OVER!")
            elif ninth_input == "i":
              if i == set():
                print("Your inventory is empty")
                second2()
              else:
                print("You have: " + i)
                second2()
            else:
              print("Sorry, you have to pick either 'django' or 'mysql'.")
              second2()
          second2()
        elif eighth_input == "r":
          start()
        elif eighth_input == "q":
          print("GAME OVER!")
        elif eighth_input == "i":
          if i == set():
            print("Your inventory is empty")
            second1()
          else:
            print("You have: " + i)
            second1()
        else:
          print("Oh no, that was the wrong number! You type in countless other numbers such as '1234' and '0000', but none of them work. The Martians shoot you before you get the right combnation. Bad luck.")
          print("GAME OVER!")
          start()
      second1()
    elif seventh_input == "r":
      start()
    elif seventh_input == "q":
      print("GAME OVER!")
    elif seventh_input == "i":
      if i == set():
        print("Your inventory is empty")
        final_stage()
      else:
        print("You have: " + i)
        second_stage()
    else:
      print("Sorry, you have to pick either 'first door' or 'second door'. There's no turning back now!")
      final_stage()
start()
