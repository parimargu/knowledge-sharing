# Git Commands

✅ Create a project locally

✅ Use Git to track changes

✅ Push code to GitHub

✅ Make future changes and collaborate

---

## Git Workflow and Commonly Used Commands

[Click here to view](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvpxeexqyfvf4hw3zxtbn.png)

[Reference link](https://dev.to/mollynem/git-github--workflow-fundamentals-5496)

---

## Git Config Commands

### 🔸 Set your username and email (identity)

```bash
git config --global user.name "Your Name"
git config --global user.email "your@example.com"
```

To set per-repository:

```bash
git config user.name "Repo-Specific Name"
git config user.email "repo@example.com"
```

---

### 🔸 Check current configuration

```bash
git config --list
```

---

## 🗃️ Step 1: Create a Local Project Folder

### Open terminal (Git Bash or Terminal) and run:

```bash
mkdir hello-git
cd hello-git
```

---

## 🔁 Step 2: Initialize Git & Make a Commit

```bash
git init                    # Start Git tracking
echo "# Hello Git!" > README.md
git status                  # See what's changed
git add README.md           # Stage the file
git commit -m "First commit"  # Save snapshot
```

---

## 🚀 Step 3: Push Code to GitHub

> Replace `<your-username>` with your GitHub username

```bash
git remote add origin https://github.com/<your-username>/hello-git.git
git branch -M main
git push -u origin main
```

✅ Go to your repo page on GitHub – you’ll now see the `README.md` file there!

---

## ✍️ Step 4: Make a Change and Push Again

Let’s add a new file:

```bash
echo "print('Hello, GitHub!')" > app.py
git add app.py
git commit -m "Add simple Python script"
git push
```

🔁 Every time you make changes:

```bash
git add .
git commit -m "Describe what changed"
git push
```

---

## 🎯 Summary of Git Commands

| Command                     | Purpose                          |
| --------------------------- | -------------------------------- |
| `git init`                  | Start Git in your project folder |
| `git status`                | Show tracked/untracked changes   |
| `git add filename`          | Stage file for commit            |
| `git commit -m "message"`   | Save snapshot                    |
| `git remote add origin URL` | Connect local to GitHub repo     |
| `git push`                  | Upload changes to GitHub         |
| `git pull`                  | Get latest changes from GitHub   |

---

## Git Commands - Part 2

[Click here](2_Git_Commands_Part_2.md) to learn more about Git Commands