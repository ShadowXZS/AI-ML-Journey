# =================================================================
# DAY 6 PROJECT: THE MAZE (USER SOLUTION: "THE SPRINTER")
# =================================================================

# --- VS CODE SILENCER (MOCK FUNCTIONS) ---
# This block stops VS Code from showing errors for Reeborg commands.
def move(): pass
def turn_left(): pass
def at_goal(): return False
def front_is_clear(): return True
def right_is_clear(): return True
def wall_on_right(): return False
def wall_in_front(): return False
# -----------------------------------------

def turn_right():
    """Simulates a right turn."""
    for step in range(3):
        turn_left()

# --- THE MAIN ALGORITHM ---
while not at_goal():
    
    # 1. THE SPRINT (The Hunter's Innovation)
    # Run full speed until a wall is hit.
    while front_is_clear():
        move()
    
    # 2. THE DECISION (Once stopped)
    if right_is_clear():
        turn_right()
        # Note: You might need a 'move()' here if the turn doesn't move you
        # But based on your logic, you turn and then let the loop sprint again.
    elif wall_on_right():
        turn_left()
    else:
        # If right is blocked and front is blocked, turn right (or left? check logic)
        # Your original code had 'elif wall_in_front(): turn_right()'
        turn_right()
# Solved 