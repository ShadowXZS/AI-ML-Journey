
---

### **1. The GPU Monitor (`nvidia-smi` & `nvitop`)**

These tools allow you to see exactly how much of your **12GB VRAM** is being used in real-time.

- **`nvidia-smi`**: The industry standard. Run this to see a snapshot of your GPU health.
    
    Bash
    
    ```
    nvidia-smi
    ```
    
    > **Key Metric:** Look at the `Memory-Usage` column. If it hits 12GB, your model is too big for your GPU.
    
- **`nvitop`**: The "prettier" interactive version.1 It works like a task manager for your GPU.
    
    Bash
    
    ```
    nvitop
    ```
    
    - **Pro Tip:** Use your mouse or arrow keys to scroll. Press `q` to exit.
        

---

### **2. Local Model Engine (`ollama`)**

Since Ollama is now a system service, you can control it entirely from the terminal.2

- **Pull a model** (Download it to your HDD):
    
    Bash
    
    ```
    ollama pull llama3.2:3b
    ```
    
- **Run and Chat** (Immediate interaction):
    
    Bash
    
    ```
    ollama run llama3.2:3b
    ```
    
- **List your models**:
    
    Bash
    
    ```
    ollama ls
    ```
    
- **See what's running right now**:
    
    Bash
    
    ```
    ollama ps
    ```
    

---

### **3. GPU Data Science (`cuDF` & `cuML`)**

You can now run **Pandas** and **Scikit-Learn** code on your GPU with **zero code changes**.

- Accelerate any script instantly:
    
    Instead of running python script.py, use the RAPIDS module flag:
    
    Bash
    
    ```
    # For Pandas acceleration
    python -m cudf.pandas your_script.py
    
    # For Scikit-Learn (ML) acceleration
    python -m cuml.accel your_script.py
    ```
    
- In VS Code/Jupyter Notebooks:
    
    Add this as the very first line of your notebook to activate the GPU:
    
    Python
    
    ```
    %load_ext cudf.pandas
    import pandas as pd
    ```
    

---

### **4. Agentic AI (`crewai`)**

CrewAI is best used through its built-in CLI for project management.

- **Create a new project structure**:
    
    Bash
    
    ```
    crewai create crew my_first_agent_project
    ```
    
- Run your crew:
    
    Navigate to the project folder and run:
    
    Bash
    
    ```
    crewai run
    ```
    
- **Train your agents** (to improve their performance over time):
    
    Bash
    
    ```
    crewai train -n 5
    ```
    

---

### **5. Polars (The Speed Demon)**

Polars doesn't need a special CLI; it's a high-performance library you import directly in your code.

Python

```
import polars as pl

# This reads files 10-20x faster than standard Pandas
df = pl.read_csv("large_data.csv")
print(df.head())
```

---

### **Summary of Your "Power Commands"**

|**Goal**|**Command**|
|---|---|
|**Check GPU Temp/VRAM**|`nvitop`|
|**Talk to a Local LLM**|`ollama run llama3.1`|
|**Run Python with GPU Pandas**|`python -m cudf.pandas script.py`|
|**Start an Agent Project**|`crewai create crew name`|
|**Sync to GitHub**|`git push`|

