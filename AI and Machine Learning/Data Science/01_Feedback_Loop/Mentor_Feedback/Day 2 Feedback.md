**Topic: Control Flow (If/Else)**

- **The Golden Rule of Chains:**
    
    - Use `if / elif / else` when only **ONE** option can happen (e.g., Grading: A, B, or C).
        
    - Use multiple `if` statements when **MULTIPLE** things can happen in sequence (e.g., "If I go Left" AND THEN "If I survive").
        
- **The Indentation Trap:**
    
    - Every time you indent (tab), you are entering a "sub-universe." Code inside an indented block _cannot_ be seen or run if the outer condition is False.
        
- **Flag Variables:**
    
    - Using variables like `right_to_stand = 1` is a powerful way to "save progress," but only if you check that flag in a _separate_ logic block later.
    

The Lesson (DRY Principle):** In the future, a Master follows **D.R.Y.** (Don't Repeat Yourself).

- Instead of writing the "Cheese Logic" 3 times inside every size, you write it **once** at the end.
    
- _Logic:_ Calculate the Base Price based on Size first. _Then_, regardless of size, check for cheese.
  
## Advice:_ Gamify the boredom. See how _fast_ or _clean_ you can write the boring code. Make efficiency the new puzzle.

### 1. The "Paper First" Rule (The Anti-Frustration Protocol)

Today, you failed because you tried to build the maze _while_ you were running inside it. You wrote code without a map.

- **The Advice:** For every project moving forward, you are **forbidden** from writing code for the first 10 minutes.
    
- **The Action:** Use Draw.io or a napkin. Draw the logic.
    
    - If you can't draw the arrow from "Room A" to "Room B", you can't code it.
        
    - **Why?** This satisfies your "Architect" craving. It lets you solve the "Puzzle" (the logic) _before_ you have to do the "Boring Work" (the syntax).
        

### 2. Gamify the "Boring" Syntax

You hate the "Customer Service" part of coding—the repetitive typing, the colons, the indentation.

- **The Advice:** You must trick your brain. Do not see it as "typing." See it as **"Speed Running."**
    
- **The Action:** When you have to type a boring list or a repetitive `if/else` block, try to do it _fast_ and _perfect_.
    
    - "Can I type this entire block without looking at the keyboard?"
        
    - "Can I write this function in under 60 seconds?"
        
    - Turn the "chore" into a "time trial."
        

### 3. The "Icebox" is Your Best Friend

You have "Scope Creep" in your DNA. You want to add features instantly.

- **The Advice:** Never kill an idea. But never let an idea kill your current progress.
    
- **The Action:** Keep that "Ambitious Projects" folder open. When you get a crazy idea (e.g., "I want the enemies to have AI"), **stop coding**.
    
    - Write the idea in a text file in that folder.
        
    - Say to yourself: _"I have captured the beast. I will skin it later."_
        
    - Return to the boring tutorial code.
        
    - This calms the "Visionary" side of your brain so the "Worker" side can finish the job.
        

### 4. Respect the "Gap"

You are currently in **The Gap**.

- **Your Taste:** Level 50.
    
- **Your Code:** Level 3.
    
- **The Advice:** The frustration you feel is not failure. It is your **Taste** screaming at your **Skill** to catch up.
    
- **The Action:** When you hate your own code, do not delete it. **Comment it.** Write: `# This is ugly, but it works. I will fix it on Day 10.` Move on.