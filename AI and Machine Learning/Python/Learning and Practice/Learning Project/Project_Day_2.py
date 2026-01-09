#Treassure Island
print("Welcome to Treassure Island- The Original Expedition")
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
# Three single quotes to have multiple lines of string. 
print("--------------------------START-------------------------------\n You arrive at Treasure Island")
print("welcome to Treasure Island")
print("Instruction: Type Left or Right . To Select Your Path.")
choice_one = input("Which Direction You wish to go Left Or Right ? :")
if choice_one.lower() == "right":
    #Lower Function,  the lower() function is a string method that returns a new string where all uppercase alphabetic characters are converted to lowercase.
    #In Python, this logic does not mean "If choice is 'Right' OR choice is 'right'". It is evaluated as: (if choice_one == "Right") OR ("right"). Since the string "right" is not empty, Python considers it True. Therefore, this if statement ALWAYS evaluates to True. Even if I type "Left", the game will think I typed "Right".
    print("Game Over (Fall into a Hole)")
elif choice_one.lower() == "left":
    print("Continue.")
    print("Instruction: Type Swim or Wait. To Select Your Path.")
    choice_two = input("There is a River Would you Swim or Wait ? :")
    if choice_two.lower() == "swim":
        print("Game Over (Attacked by trout)")
    elif choice_two.lower() == "wait":
        print("Continue.")
        print("Instruction: Type Red, Yellow or Blue. To Select Your Path.")
        choice_three = input("Which Door ? Red, Yellow, Blue : ")
        if choice_three.lower() == "red":
            print("Game Over (Burned By Fire)")
        elif choice_three.lower() == "blue":
            print("Game Over (Eaten By Beasts)")
        elif choice_three.lower() == "yellow":
            print("YOU WIN!")
        else:
            print("Please Check your Choice and Try Again ")
    else:
        print("Please Check your Choice and Try Again ")
else:
    print("Please Check your Choice and Try Again")

