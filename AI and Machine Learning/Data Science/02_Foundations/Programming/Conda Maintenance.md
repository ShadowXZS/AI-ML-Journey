| **Task**                                  | **Command**                                                                                       |     |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------- | --- |
| **Check Environment Health**              | `conda list`                                                                                      |     |
| **Sync Environment with YAML**            | `conda env update --file environment.yml --prune`                                                 |     |
| **Add a New "Tool"**                      | `conda install <package>` followed by `conda env export > environment.yml`                        |     |
| **Nuclear Option** (If everything breaks) | `conda deactivate`, `conda env remove -n aiandml_env`, then `conda env create -f environment.yml` |     |
| Cross Reference                           | conda compare environment.yml                                                                     |     |
| Ubuntu <br>Perfect Environment.           | conda env export > environment_perfect.yml                                                        |     |



---

# 🛠️ AI Workstation: Safe Exit Sequence

Date Created: 2026-01-05

Purpose: To safely deactivate the AI environment, backup changes, and close the WSL2 bridge without corruption.

### 1. The "Blueprint" Backup

Always update your environment file if you installed new libraries during the session.

Bash

```
conda env export --no-builds > environment_perfect.yml
```

### 2. The Cloud Sync (Git)

Push your code and the new blueprint to GitHub.

Bash

```
git add .
git commit -m "Update session: [Briefly describe what you did]"
git push origin main
```

### 3. The "Cold Storage" Backup (Optional)

Run this if you made major changes to the environment itself (like fixing CUDA/NumPy).

Bash

```
tar -czvf /mnt/d/Learning/aiandml_env_session_backup.tar.gz -C /home/shadowz/miniconda3/envs aiandml_env
```

### 4. System Shutdown

The ritual to "close the garage" properly.

Bash

```
# Deactivate the AI Environment
conda deactivate

# Return to Ubuntu Home directory
cd ~

# Close the Terminal
exit
```

---

### 💡 Pro-Tip for Obsidian

> [!IMPORTANT]
> 
> Why we do this: Skipping conda deactivate or closing the laptop while a script is running can sometimes "lock" the GPU memory or corrupt the Conda metadata. This sequence ensures your RTX 3060 is "released" back to the system.

---



---

### **1. The "Heartbeat" Check (NVIDIA-SMI)**

You can run this in PowerShell at any time (even while you are gaming or coding) to see exactly how much VRAM is being used and how hot your GPU is.

**Command:**

PowerShell

```
nvidia-smi
```

- **Why it matters:** If your code crashes with an "Out of Memory" (OOM) error, run this in PowerShell to see if another app (like Chrome or a game) is "stealing" VRAM from your AI.
    

---

### **2. The "Deep Sleep" Command**

Sometimes, even after you close the Ubuntu terminal, WSL2 stays running in the background, consuming System RAM. If you want to "flush" everything and give your PC a fresh start, run this in **PowerShell (Admin)**:

**Command:**

PowerShell

```
wsl --shutdown
```

- **What it does:** It completely kills the virtual Linux machine.1 The next time you open Ubuntu, it will perform a "Cold Boot," which is great for clearing out "ghost" processes.
    

---

### **3. The "Obsidian" Summary for PowerShell**

Add this small section to your `Maintenance_Rules.md` in Obsidian:

|**Scenario**|**PowerShell Command**|
|---|---|
|**Check GPU Heat/VRAM**|`nvidia-smi`|
|**Kill Linux/Reset Environment**|`wsl --shutdown`|
|**Check WSL Version**|`wsl -l -v`|

---

