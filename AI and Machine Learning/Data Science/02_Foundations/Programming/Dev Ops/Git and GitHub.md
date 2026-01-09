
---

# 📘 Master Git & GitHub Notes

## 🔹 1. Repository & Setup

- **Initialize Repository**

```bash
git init
```

Creates a new Git repository in the current directory.

- **Clone Repository**

```bash
git clone <url>
```

Downloads a repository from a remote source.

- **Link Remote Repository**

```bash
git remote add origin <url>
```

Adds a remote repository to your local repo.

- **Add Upstream (for forks)**

```bash
git remote add upstream <url>
```

Links your fork to the original repository.

- **List Remotes**

```bash
git remote -v
```

Shows all linked remote repositories.

---

## 🔹 2. File & Directory Management (Linux Basics)

- `ls` → List files in directory
- `cd <directory>` → Change directory
- `mkdir <name>` → Create directory
- `touch <filename>` → Create empty file
- `cat <filename>` → View file contents

---

## 🔹 3. Staging & Committing

- **Stage All Files**

```bash
git add .
```

Adds all changes to staging area.

- **Stage Specific File**

```bash
git add <filename>
```

Adds a specific file to staging area.

- **Unstage File**

```bash
git restore --staged <filename>
```

Removes file from staging area.

- **Commit Changes**

```bash
git commit -m "Message"
```

Commits staged changes with a message.

---

## 🔹 4. Branching & Workflow

- **Create Branch**

```bash
git branch <branch-name>
```

- **Switch Branch**

```bash
git checkout <branch-name>
```

or modern:

```bash
git switch <branch-name>
```

- **Rename Branch**

```bash
git branch -m <old-name> <new-name>
```

- **Delete Branch**

```bash
git branch -d <branch-name>
```

- **Merge Branch**

```bash
git merge <branch-name>
```

- **Delete Remote Branch**

```bash
git push origin --delete <branch-name>
```

---

## 🔹 5. Syncing & Collaboration

- **Fetch Changes**

```bash
git fetch
```

Downloads changes without merging.

- **Pull Changes**

```bash
git pull origin <branch-name>
```

Fetches and merges changes from remote.

- **Rebase Pull**

```bash
git pull --rebase
```

Keeps history linear.

- **Fetch All**

```bash
git fetch --all
```

---

## 🔹 6. Logs & History

- **View Commit History**

```bash
git log
```

- **Show Commit Details**

```bash
git show <commit-hash>
```

- **Reset to Commit**

```bash
git reset <commit-hash>
```

⚠️ Alters history.

- **Revert Commit**

```bash
git revert <commit-hash>
```

Safely undoes a commit by creating a new commit.

- **Reflog**

```bash
git reflog
```

Shows history of HEAD movements (recover lost commits).

---

## 🔹 7. Stashing

- **Stash Changes**

```bash
git stash
```

- **Apply Stash**

```bash
git stash pop
```

- **Clear Stash**

```bash
git stash clear
```

---

## 🔹 8. Diff & Inspection

- **View Differences**

```bash
git diff
```

- **Blame File**

```bash
git blame <filename>
```

Shows who modified each line.

---

## 🔹 9. Tagging & Releases

- **Create Tag**

```bash
git tag <tag-name>
```

- **Annotated Tag**

```bash
git tag -a v1.0 -m "Release version 1.0"
```

- **Push Tags**

```bash
git push origin --tags
```

---

## 🔹 10. Cleanup & Optimization

- **Garbage Collection**

```bash
git gc
```

Optimizes repo size/performance.

- **Remove Untracked Files**

```bash
git clean -fd
```

⚠️ Irreversible.

---

## 🔹 11. Configuration

- **Set Identity**

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

- **View Config**

```bash
git config --list
```

---

# ✅ Best Practices

- Never commit directly to `main` → Always use feature branches.
- Use `git pull --rebase` for cleaner history.
- Protect `main` branch on GitHub (branch protection rules).
- Pair Git with Python scripts for automation (CI/CD, auto-commits).

---

