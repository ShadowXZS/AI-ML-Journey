# Password Generator 
import random

how_many_letters = int(input("How Many Letters Would You like in Your Password ? : "))
how_many_symbols = int(input("How Many Symbols Would You like in Your Password ? : "))
how_many_number = int(input("How Many Numbers Would You like in Your Password ? : "))

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols =["!", "#" , "$" , "%", "&", "(", ")", "*", "+" , "," , "-", ".", "/", ":", ";", "<", "?", "@", "`", ">", "{", "~", "=", "}", "|"]

password_list = []

for char in range(how_many_letters):
    password_list.append(random.choice(letters))

for char in range(how_many_symbols):
    password_list.append(random.choice(symbols))
    
for char in range(how_many_number): 
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
print(password_list)
password = ""

for char in password_list: 
    password += char
    
print(f"Your password is : {password}")
# """
# ========================================================================
# POST-MORTEM ANALYSIS: THE LOGIC TRAP (Jan 9, 2026)
# ========================================================================
# My initial logic failed because I was thinking like a Human, not a Machine.

# ERROR 1: The "Buffet" Fallacy (Looping Source vs. Requirement)
# - WHAT I DID: `for letter in letters:`
# - MY LOGIC: "Go to the alphabet list to find letters."
# - THE REALITY: This forces the loop to run 52 times (size of alphabet), 
#   regardless of how many letters I actually wanted.
# - THE FIX: Loop through the *count* needed using `range(nr_letters)`.

# ERROR 2: The "Suicide" Math (Counter Reset)
# - WHAT I DID: `how_many_letters -= how_many_letters`
# - MY LOGIC: "I need to subtract from the total."
# - THE REALITY: X - X = 0. I instantly set the counter to zero, killing 
#   the loop immediately.
# - THE FIX: Subtract 1 at a time (`-= 1`) or just use `range()`.

# ERROR 3: The "Groundhog Day" Amnesia (Scope Issue)
# - WHAT I DID: Created `lettering = []` INSIDE the loop.
# - MY LOGIC: "I need a basket for this letter."
# - THE REALITY: The loop creates a NEW empty list every single time, 
#   destroying the previous data.
# - THE FIX: Create the list OUTSIDE the loop (Persistence).
# ========================================================================
# """

# """
# ========================================================================
# THE 3 RULES OF LOGIC (To Avoid Future Errors)
# ========================================================================

# RULE 1: THE BUCKET RULE (Scope)
# - QUESTION: "Where do I put the items I collect?"
# - MISTAKE: Creating the list INSIDE the loop.
# - REALITY: If you create a list inside the loop, it resets every time.
# - THE LAW: "Born Outside, Lives Inside." Always create your empty list 
#   BEFORE the loop starts.

# RULE 2: THE DRIVER RULE (Iteration)
# - QUESTION: "Who decides how many times we run?"
# - MISTAKE: Looping through the Source (e.g., `for x in alphabet`).
# - REALITY: The Source is huge (52 letters). You only want 4.
# - THE LAW: "Loop the Count, Not the Source." If you need X items, 
#   use `range(X)`. Only loop the source if you need to check EVERY item.

# RULE 3: THE ONE-WAY STREET (Variables)
# - QUESTION: "How do I count down?"
# - MISTAKE: `x -= x` (Subtracting itself).
# - REALITY: This equals zero instantly.
# - THE LAW: "Step by Step." Decrease by 1 (`x -= 1`) or let `range()` 
#   handle the counting automatically.
# ========================================================================
# """