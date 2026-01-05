#Treassure Island
print("Welcome to Treassure Island- The Cursed Expedition")
print(''' ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----|
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \|//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //|\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    |"|      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------|
 \_/__________________________________________________________________/''')
#Need to Understand What print('''  ''') does, I was unable to include the ASCII art the normal way and Installed pip Install Art
print("--------------------------START-------------------------------\n You arrive at Treasure Island")
print("Instruction: Type Left, Right or Center. To Select Your Path.")
choice_one = input("Path at the Crossroads, You have 3 Options \n 1. Go Left [You go to Jungle] \n 2. Go Right [You go to Cliffside] \n 3. Go Straight [Leads to Village Ruins]\n :")
health = 2
luck = 2
trust = 0
relic = 0
clue = 0
map_fragment = 0
right_to_stand = 0
if choice_one == "Left":
    print("Instruction: Type Swim , Build Raft or Wait")
    choice_jungle= input("You have Arrived at the Jungle , There is a River You Need to Cross \n What Will You Do ?\n 1. Swim Across River \n 2. Build Raft \n 3. Wait\n :")
    if choice_jungle == "Swim":
        health -= 1
        print("You swam across the River, The Crocodiles in the River attacked you, You are Bleeding [-1 Health]")
    elif choice_jungle == "Build Raft":
        luck -= 1
        right_to_stand += 1
        print("You have crossed the River Safe, But You lost Time [-1 Luck]")
    elif choice_jungle == "Wait":
        trust += 1
        clue += 1
        print("You were waiting, A Hermit appeared and said \n Hermit: [There is a Bridge not to far away If you carry me I will show you the way] \n You carry him on your back .. You both cross the bridge He gives you a Clue about the Treasure [+1 Trust] \n : ")

elif choice_one == "Right":
    print("Instruction: Type Clim Carefully, Rush Climb or Explore Cave")
    choice_cliff= input("You have arrived at the Cliffside Path, You see a path as you gaze into the distance you see a cave. \n What Will You Do ? \n 1. Climb the Path Carefully  \n 2. Rush climb the path because you need to get to the Treasure Room \n 3. You Go to Explore the Cave ")
    if choice_cliff == "Clim Carefully":
        right_to_stand += 1
        print("You have arrived at the Treasure Room")
    elif choice_cliff == "Rush Climb":
        health -= 2
        print("You Rushed the Climb, You Slipped and You fell [ You are Gravely Injured -2 Health")
    elif choice_cliff == "Explore Cave":
        relic += 1
        luck -= 2
        right_to_stand += 1
        print(" You Explore the Cave , You find a Old Relic [ The Relic is Cursed -2 Luck ]")

elif choice_one== "Center":
    print("Instruction: Type Enter Ruins, Search Huts or  Ignore Huts")
    choice_village= input("You have arrived at a Village Ruins, You have 3 Options \n What will you do ? \n 1. Enter Ruins \n 2. Search Huts \n 3. Ignore Ruins")
    if choice_village == "Enter Ruins":
        trust -= 1
        print("You hear ghostly whispers, Ghostly whispers: [There is No Treasure][-1 Trust]")
    elif choice_village == "Search Huts":
        map_fragment += 1
        right_to_stand += 1
        print("You Search Huts, You find a Fragment of the Treasure Map ")
    elif choice_village == "Ignore Ruins":
        right_to_stand += 1
        print("You Choose to Ignore the Ruins,and you go to the Treasure Ruins")
elif health == 0:
    print("You Died, Game Over")
elif trust < 0:
    print("You Reached the Treassure Room, You are Too Scared to Move Forward, ")
elif health <= 1:
    print("You Reached the Treassure Room, Your Vision is Blurry")
elif right_to_stand == 1:
    choice_two = input("You have arrived at 3 Doors 1. Red,  2. Blue, 3. Yellow ")
    if choice_two == "Red":
        if clue ==1:
            print("Safe Passage")
        else:
            print("Game Over")
    if choice_two == "Blue":
        if relic == 1:
            print("Safe Passage")
        else:
            print("Game Over")
    if choice_two == "Yellow":
        if luck >= 0:
            print("You found Treasure")
        elif luck < 0:
            print(" Game Over, Cursed Ending")
        else:
            print("Please verify Your Choice")
    else:
        print("Please verify Your Choice")
elif right_to_stand == 1 and relic == 1:
    choice_two = input("You have arrived at 3 Doors 1. Red,  2. Blue, 3. Yellow  You Look Around See a Black Door ")
    if choice_two == "Red":
        if clue == 1:
            print("Safe Passage")
        else:
            print("Game Over")
    if choice_two == "Blue":
        if relic == 1:
            print("Safe Passage")
        else:
            print("Game Over")
    if choice_two == "Yellow":
        if luck >= 0:
            print("You found Treasure")
        else:
            print(" Game Over, Cursed Ending")
    if choice_two == "Black":
        if relic == 1:
            print("You Keep Wandering inside the Room")
        elif relic == 0:
            print(" Safe Passage")
        else:
            print("Please verify Your Choice")
    else:
        print("Please verify Your Choice")

elif right_to_stand == 1 and clue ==1 and trust ==1:
    choice_two = input("You have arrived at 3 Doors 1. Red,  2. Blue, 3. Yellow  You Look Around See a Hidden Green Door ")
    if choice_two == "Red":
        if clue == 1:
            print("Safe Passage")
        else:
            print("Game Over")
    if choice_two == "Blue":
        if relic == 1:
            print("Safe Passage")
        else:
            print("Game Over")
    if choice_two == "Yellow":
        if luck >= 0:
            print("You found Treasure")
        else:
            print(" Game Over, Cursed Ending")
    if choice_two == "Green":
        if clue == 1:
            print("Safe Passage, You get No Treassure")
        elif map_fragment == 1:
            print(" Safe Passage, You get No Treassure")
        elif clue == 0 and map_fragment == 0:
            print("You are Trapped and You died of Suffocation, Game Over")
        else:
            print("Please verify Your Choice")

else:
    print("Please verify Your Choice")

# Project Incomplete, Will Come Back and Crush this Project
#Perfect challenge 😎. The original *Treasure Island* flowchart you shared is a classic "choose-your-path" adventure, but it’s quite minimal. Let’s enhance it into a **multi-layered, complex text-based story game** with richer choices, branching consequences, and hidden paths. I’ll expand the narrative, add moral dilemmas, resource management, and multiple endings beyond just “Game Over” or “You Win.”

---

## 🌴 Enhanced Story Concept: *Treasure Island – The Cursed Expedition*

### Key Enhancements
- **Multiple Resources:** You must manage *health*, *trust*, and *luck*.
- **Moral Choices:** Decisions affect alliances and betrayals.
- **Hidden Paths:** Secret routes unlock if you make clever or patient choices.
- **Multiple Endings:** Treasure, cursed fate, survival escape, or eternal wandering.

---

## 🗺️ Enhanced Flowchart (Text Representation)

```
START → You arrive at Treasure Island.

Choice 1: Path at the Crossroads
- Left → Leads to Jungle
- Right → Leads to Cliffside
- Straight → Leads to Village Ruins

Jungle Path:
- Swim across river → Attacked by crocodiles (Lose Health)
- Build raft → Safe crossing, but lose time (Luck -1)
- Wait → Meet a hermit who gives a clue (Gain Trust)

Cliffside Path:
- Climb carefully → Reach cave entrance
- Rush climb → Fall, injured (Lose Health)
- Explore cave → Find cursed relic (Luck -2, unlock secret ending)

Village Ruins:
- Enter ruins → Ghostly whispers (Trust check)
- Search huts → Find map fragment
- Ignore ruins → Miss clue, but stay safe

Choice 2: At the Three Doors (Red, Blue, Yellow)
- Red → Fire trap (Game Over unless you have hermit’s clue → Safe passage)
- Blue → Beasts attack (Game Over unless you found relic → Relic scares beasts)
- Yellow → Treasure chamber (Win if Luck ≥ 0, else cursed ending)

Secret Paths:
- If you collected map fragment + hermit’s clue → Hidden Green Door → Escape ending (Survive without treasure)
- If you carry cursed relic → Black Door → Eternal wandering ending
```

---

## 🎮 New Endings
- **Treasure Ending:** You win with treasure if you balance luck and clues.
- **Cursed Ending:** You reach treasure but are cursed forever.
- **Survival Ending:** Escape alive but without treasure.
- **Eternal Wandering Ending:** Trapped in the island’s curse.
- **Game Over:** Classic death traps if careless.

---

## 🖌️ Why This Is More Complex
- Choices now **interconnect** (hermit’s clue saves you later, relic changes beast encounter).
- **Resource checks** (Luck, Trust, Health) add replayability.
- **Hidden doors** reward exploration.
- Multiple **narrative tones**: survival, horror, mystery, triumph.

---

🔥 This is now a **true story game system**, not just a linear puzzle. Would you like me to **draw the enhanced flowchart visually** (with nodes and arrows) so you can use it as a design blueprint?

