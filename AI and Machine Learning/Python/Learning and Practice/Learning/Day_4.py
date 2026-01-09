#Python Loops 
#For Loop With Python Lists 

fruits = ["Apple", "Peach", "Orange", "Pear"]
for fruit in fruits:
    print(fruit)
# Allows to Execute Same Line of Code Multiple Times 
student_scores = [150, 142, 185, 120, 171, 184 , 149 , 24 , 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_exam_score = sum(student_scores)
print(total_exam_score)
#Sum Function 
sum = 0
for score in student_scores:
    sum += score
print(sum)

# For Loops and the Range() Function 
total = 0
for number in range(1,101):
    total += number
print(total)
# += Accumulator Function 
# Other way of doing this print(sum(range(1,101)))
# 1. The Two Types of Loops
# The biggest mistake is confusing "Iterating a Source" with "Iterating a Count."

# Type A: The "Inspector" (Iterate Source)

# Use when: You want to look at every single item in a list.

# Code: for fruit in fruits:

# Logic: The loop runs once for every item in the bag. If the bag has 100 items, it runs 100 times.

# Analogy: The Security Guard checking every bag in the line.

# Type B: The "Counter" (Iterate Count)

# Use when: You want to perform an action X times (regardless of any list).

# Code: for _ in range(10):

# Logic: The loop runs exactly 10 times. It creates numbers (0-9) to keep track.

# Analogy: Doing 10 pushups. You don't check a list; you just count.



# 2. The range() Function
# Think of range() as a Number Generator.

# Rule: "Start is IN. Stop is OUT."

# range(4) → 0, 1, 2, 3 (Generates 4 numbers. Starts at 0).

# range(1, 5) → 1, 2, 3, 4 (Starts at 1. Stops before 5).

# range(0, 10, 2) → 0, 2, 4, 6, 8 (Jumps by 2).




# 3. The Loop Variable (char or i)
# What is it? It is a temporary "nametag" for the current number.

# The Reassignment: In every single step of the loop, this variable is wiped clean and given the next number.

# Step 1: char = 0

# Step 2: char = 1

# The "Dumb Container": It does not remember the past. It only knows the "Now."




# 4. The "Scope" Trap
# The Error: list = [] inside the loop.

# Result: You buy a new wallet every day and throw away the old one.

# The Fix: list = [] OUTSIDE the loop.

# Result: You keep the same wallet and keep adding money to it.