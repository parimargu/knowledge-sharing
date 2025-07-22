# Git and GitHub.com

---

## ✅ What is **Git**?

### 🔹 Git is a **version control system**.

* It helps you **track changes** to your code or project files over time.
* You can **go back to previous versions**, **compare changes**, and **collaborate** with others without overwriting each other's work.
* Git is **installed locally** on your computer.

### 🔧 Key Features:

* **Track versions** of files (especially code)
* **Branching**: Work on new features without affecting main code
* **Merging**: Combine changes from different branches
* **Staging area**: Choose which changes to commit
* Works completely **offline** (until you want to share it)

---

## ✅ What is **GitHub**?

### 🔹 GitHub is a **cloud-based platform** built around Git.

* It’s a **website** (github.com) where you can **store Git repositories online**.
* It allows you to **collaborate with others**, **review code**, and **manage projects**.
* GitHub uses Git under the hood.

### 🌐 Key Features:

* **Remote hosting** of Git repositories
* **Collaboration tools**: Pull Requests, Issues, Wiki, Project boards
* **CI/CD integrations**: Automate testing, deployment
* **Social coding**: Follow, star, fork others’ projects
* Web-based **code browsing and reviews**

---

## 🔄 Git vs GitHub – Comparison Table

| Feature            | Git                                     | GitHub                                     |
| ------------------ | --------------------------------------- | ------------------------------------------ |
| Type               | Version Control Tool                    | Web-Based Platform (Cloud Git Hosting)     |
| Installed On       | Local Computer (CLI or GUI)             | Online (via browser, also CLI access)      |
| Functionality      | Tracks and manages code history locally | Hosts Git repositories remotely            |
| Internet Required? | ❌ No (works offline)                    | ✅ Yes (for access/sharing)                 |
| Collaboration      | Manual sharing via files/patches        | Easy collaboration via pull requests       |
| Security           | Local security managed by user          | Repo privacy settings, 2FA, access control |
| Example Usage      | `git init`, `git commit`, `git push`    | `github.com/your-repo-name`                |
| Interface          | Command-line tools (or GUI apps)        | Web interface + Git CLI                    |
| Additional Tools   | Just version control                    | Issue tracking, wikis, CI/CD, project mgmt |
| Ownership          | Free & open-source software             | Owned by Microsoft                         |

---

## 🧠 Real-world Analogy

Think of **Git** as:

> 🔧 A powerful notebook that keeps every version of your code locally on your computer.

And **GitHub** as:

> 🌐 Google Drive for your Git notebook—accessible from anywhere and shareable with your team.

---

## 💻 Example Workflow

1. **Initialize Git** in your project folder:

   ```bash
   git init
   ```

2. **Make changes**, track them:

   ```bash
   git add .
   git commit -m "Initial commit"
   ```

3. **Push code to GitHub**:

   ```bash
   git remote add origin https://github.com/yourusername/repo-name.git
   git push -u origin main
   ```

4. **Collaborate** with team using GitHub features like Pull Requests, Issues, and Project Boards.

---

## 🎯 Summary

| Aspect         | Git                           | GitHub                          |
| -------------- | ----------------------------- | ------------------------------- |
| What is it?    | Version control software      | Git repository hosting platform |
| Where it runs? | Your local computer           | Online (cloud-based)            |
| Main purpose   | Track and manage code changes | Collaborate and share code      |

---


Read more about [Introduction to Git and GitHub.com](1_Introduction_to_Git.md)
