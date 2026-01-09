
---

# 📐 Math Visualization: Dynamic Equations in Python

Context: Jupyter Notebook, SymPy Preparation, LaTeX, Dynamic Printing

Source: printingoutequations.ipynb

---

## 1. The Core Philosophy: "The Mirror"

In Data Science, we never "hardcode" numbers into a print statement. The output must change dynamically when the variables change.

- **The Typewriter (Bad):** Manually typing the result.
    
    - _Code:_ `display(Math('3 + 4 = 7'))`
        
    - _Flaw:_ If $x$ changes to 10, the text still says "3 + 4 = 7". It becomes a lie.
        
- **The Mirror (Good):** Using placeholders to reflect the variables.
    
    - _Code:_ `display(Math('%g + %g = %g' %(x, y, x+y)))`
        
    - _Benefit:_ The equation updates automatically.
        

---

## 2. The Tool: `%g` (General Format)

The `%g` format specifier is the "Cleaner" for floating-point numbers. It chooses the most compact way to represent a number.

|**Input Number**|**Default Print**|**With %g**|**Why?**|
|---|---|---|---|
|`5.0`|`5.000000`|`5`|Removes redundant zeros.|
|`0.3333333`|`0.333333333`|`0.333333`|Truncates reasonable length.|
|`0.0000001`|`0.0000001`|`1e-07`|Switches to Scientific Notation.|

---

## 3. LaTeX Syntax for Python

We use the `IPython.display.Math` function to render LaTeX inside Jupyter.

### A. Basic Operators

- **Multiplication:** Use `\\times` for the 'x' symbol.
    
    - _Code:_ `display(Math('3 \\times 4'))` $\rightarrow$ $3 \times 4$
        
- **Fractions:** Use `\\frac{numerator}{denominator}`.
    
    - _Code:_ `display(Math('\\frac{3}{4}'))` $\rightarrow$ $\frac{3}{4}$
        

### B. The Negative Sign Trap

When a variable is negative (e.g., $y = -2$), Python prints it directly.

- **The Problem:** `-%g` with $y=-2$ results in `--2` (Double dash).
    
- **The Fix:** Wrap the variable in parentheses in your template.
    
    - _Template:_ `-(%g)`
        
    - _Result:_ `-(-2)` (Mathematically clear).
        

---

## 4. Master Template: Solving & Printing

**Workflow:**

1. **Calculate** the answer in a Python variable first (`ans`).
    
2. **Construct** the LaTeX string using `%g` placeholders.
    
3. **Inject** the raw variables and the calculated answer.
    

**Example Code:**

Python

```
x = 7
y = -2
z = 5
ans = -y - (x+3)/z  # 1. Logic

# 2. Display (The Mirror)
display(Math('-(%g) - \\frac{%g+3}{%g} = %g' %(y, x, z, ans)))
```

Output:

$$-(-2) - \frac{7+3}{5} = 0$$

---

End of Log.

## Order of Operations 
Spacing for Visualization and Parentheses for grouping 
Parentheses 
Exponents 
Multiplication 
Division 
Addition 
Subtraction 
## Double Check Calculations, With a Calculator. 
