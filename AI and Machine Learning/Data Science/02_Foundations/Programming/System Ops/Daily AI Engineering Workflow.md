
---

# 

### 1. The "Ignition" (PowerShell)

Before starting, check if your GPU is being "hogged" by other Windows apps (like Chrome or Games).

- **Open PowerShell** and run:
    
    PowerShell
    
    ```
    nvidia-smi
    ```
    
- **Check:** Is the "Memory-Usage" low? (Ideally < 2GB used if you aren't gaming).
    

### 2. The "Garage Door" (VS Code)

- Open **VS Code**.
    
- Look at the **Bottom-Left Corner**.
    
- **If it doesn't say "WSL: Ubuntu":**
    
    1. Click the green/blue icon.
        
    2. Select **"Connect to WSL"**.
        
- **Open Terminal** inside VS Code (`Ctrl + ~`). It should automatically be an Ubuntu bash prompt.
    

### 3. The "Engine Start" (Ubuntu Terminal)

Never run code in the `(base)` environment. Always wake up your AI brain:

Bash

```
conda activate aiandml_env
```

- **Verification (Optional):** If you feel paranoid, run your check script:
    
    Bash
    
    ```
    python Tools/final_check.py
    ```
    

### 4. The "Build" Phase (Development)

- **Code:** Write your Python scripts in VS Code.
    
- **Run:** Execute them in the terminal while `(aiandml_env)` is active.
    
- **GPU Monitor:** Keep a separate terminal window open with `watch -n 1 nvidia-smi` to see your 3060 working in real-time.
    

---

### 5. The "Save & Shutdown" (Exit)

When you are done for the day, follow the **Safe Exit Sequence**:

1. **Sync to GitHub:**
    
    Bash
    
    ```
    git add .
    git commit -m "Describe today's progress"
    git push origin main
    ```
    
2. **Deactivate & Close:**
    
    Bash
    
    ```
    conda deactivate
    exit
    ```
    

---

### 💡 Troubleshooting Tip

If the terminal feels "laggy" or PyTorch can't find the GPU after your PC wakes up from sleep, run this in **PowerShell**:

PowerShell

```
wsl --shutdown
```

Then reopen VS Code. This "reboots" the Linux layer and fixes 99% of connection issues.

---

