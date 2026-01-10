#Python Functions and Karel 
#Code Blocks #Functions #While Loops 
#Functions 
#def function_name():
#   instructions
#function_name() = To call the Function. 
def my_function():
    print("Hello")
    print("Bye")

my_function()
# ==========================================
# VS CODE HACK: MOCK FUNCTIONS
# (This stops the "Undefined Variable" errors)
# ==========================================
def move(): pass
def turn_left(): pass
def at_goal(): return False
def front_is_clear(): return True
def right_is_clear(): return True
def wall_on_right(): return False
def wall_in_front(): return False
# ==========================================
"""
DAY 6: WHILE LOOPS, LOGIC GATES & THE MAZE
------------------------------------------
The Mission: Navigate Reeborg's World using dynamic logic.
Key Concepts: 
1. Defining Functions (Abstraction)
2. While Loops (State-based stopping)
3. Edge Case Handling (Variable wall heights)
4. The "Scope" Trap (Global vs Local variables)

NOTE: This code is environment-specific (Reeborg's World).
It will not run in standard Python without the API (move(), turn_left(), etc).
"""

# ==========================================
# PART 1: THE TOOLKIT (My Custom Functions)
# ==========================================

def turn_right():
    """Simulates a right turn by turning left 3 times."""
    for _ in range(3):
        turn_left()

def jump():
    """
    The 'Smart' Jump Protocol (Final Version).
    Adapts to ANY wall height (Hurdle 4).
    Logic: 
    1. Climb UP while touching a wall.
    2. Move OVER when the wall ends.
    3. Climb DOWN until hitting the floor.
    """
    # 1. Prepare
    turn_left()
    
    # 2. The Ascent (Variable Height Logic)
    while wall_on_right():
        move()
    
    # 3. The Cross
    turn_right()
    move()
    turn_right()
    
    # 4. The Descent
    while front_is_clear():
        move()
        
    # 5. Reset orientation
    turn_left()

# ==========================================
# PART 2: THE SOLUTIONS (Evolution of Logic)
# ==========================================

# --- SOLUTION: HURDLE 1 (Fixed Count) ---
# Logic: We know there are exactly 6 hurdles.
# Use: For Loop (Static)
def solve_hurdle_1():
    for step in range(6):
        jump() # Note: Used simple jump here

# --- SOLUTION: HURDLE 2 (Unknown Count) ---
# Logic: We don't know the distance. 
# Use: While Loop (Sensor-based stopping)
def solve_hurdle_2():
    while not at_goal():
        jump()

# --- SOLUTION: HURDLE 3 (Random Intervals) ---
# Logic: Do not jump unless there is a wall.
# Use: Conditional Check (If/Else)
def solve_hurdle_3():
    while not at_goal():
        if front_is_clear():
            move()
        else:
            jump()

# --- SOLUTION: HURDLE 4 (Variable Heights) ---
# Logic: The wall height changes, so 'jump' must use 'while' loops internally.
# Use: The 'Smart' Jump function defined in Toolkit.
def solve_hurdle_4():
    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()

# ==========================================
# PART 3: THE SCOPE ARCHIVE (Common Errors)
# ==========================================

# --- ERROR LOG: THE "UNBOUND LOCAL" TRAP ---
# THE SCENARIO:
# I tried to modify a variable that was created OUTSIDE the function.
# 
# BAD CODE (Do not run):
# number = 6           <-- Lives in the "Hallway" (Global)
# def my_function():
#     while number > 0:
#         number -= 1  <-- ERROR! I tried to edit the Hallway variable from inside the Room.
# 
# THE LOGIC EXPLANATION:
# Python functions have "Read-Only" access to global variables by default.
# I can PRINT 'number', but I cannot CHANGE 'number'.
# When I try to change it, Python thinks I am trying to create a NEW 
# local variable, but I haven't defined it yet.
#
# THE FIX:
# Move the variable INSIDE the function (Ownership).
#
# CORRECT CODE:
# def my_function():
#     number = 6       <-- Now it lives inside the Room (Local).
#     while number > 0:
#         number -= 1  <-- Success.

# ==========================================
