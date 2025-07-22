Excellent! Let’s continue with the next essential Git & GitHub skills:

---

## ✅ What you’ll learn now:

1. 🔁 **Clone** a GitHub repository
2. 🌿 Create and use **branches**
3. 🤝 Collaborate using **Pull Requests**

---

## 🔁 1. Clone a GitHub Repository

> Cloning means downloading a repository from GitHub to your local machine.

### 📌 Steps:

1. Find any public repo on GitHub (e.g., [https://github.com/octocat/Hello-World](https://github.com/octocat/Hello-World))
2. Click the **“Code”** button → Copy the HTTPS URL

### 💻 In terminal:

```bash
git clone https://github.com/octocat/Hello-World.git
cd Hello-World
```

Now you have a **local copy** of the GitHub repo.

---

## 🌿 2. Create & Use Git Branches

> Branches let you work on new features without changing the `main` branch.

### ✅ Create a new branch:

```bash
git checkout -b feature-1
```

This creates a **branch named `feature-1`** and switches to it.

### 📝 Make changes and commit:

```bash
echo "print('This is a new feature')" > new_feature.py
git add new_feature.py
git commit -m "Add new feature script"
```

---

### 🚀 Push the branch to GitHub:

```bash
git push -u origin feature-1
```

Now on GitHub, you’ll see the new branch listed.

---

## 🤝 3. Open a Pull Request (PR)

> A **pull request** asks someone to review and merge your code into the main branch.

### 🛠️ Steps:

1. Go to your repo on GitHub
2. GitHub will show: “Compare & pull request” – click it
3. Add a title and description of your change
4. Click **Create Pull Request**

🔍 Others (or yourself) can:

* Review code changes
* Comment and discuss
* Request changes or approve

### ✅ Once ready, click **Merge Pull Request**.

Your code is now merged into `main`.

---

## 🧠 Git Branch Summary

| Command                      | Description                       |
| ---------------------------- | --------------------------------- |
| `git branch`                 | List all branches                 |
| `git checkout -b new-branch` | Create & switch to a new branch   |
| `git checkout main`          | Switch to main branch             |
| `git merge branch-name`      | Merge another branch into current |
| `git push -u origin branch`  | Push branch to GitHub             |

---

## 👥 Real-world Collaboration Example:

Imagine you're working in a team:

1. Everyone clones the same repo
2. Each person creates their own feature branch (e.g., `login-feature`, `dashboard-ui`)
3. Team members push branches to GitHub
4. Open pull requests for code review
5. Merge PRs into `main` once approved

---

Would you like to try a **live demo repo** I can create for you, or learn about **resolving merge conflicts**, **forking repos**, or **setting up GitHub issues/project boards**?

Let me know your next interest!

[Click here](2_Git_Commands_Part_3.md)