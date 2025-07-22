# Introduction to Git

---

## Git

---

Git is a distributed version control system that tracks versions of files. It is often used to control source code by programmers who are developing software collaboratively.

---

### What is a Version Control System (VCS)?

A version control system (VCS) is a tool that helps manage changes to files over time. It keeps track of every modification, so you can:

1) See who changed what and when.
2) Revert to earlier versions if something goes wrong.
3) Let multiple people work on the same project without stepping on each other’s toes.

Git is a VCS, but it’s distributed.

### What Does “Distributed” Mean?

In a distributed version control system (DVCS) like Git, every user gets a complete copy of the entire project—including all its files and the full history of changes—on their own computer. 

This is a big difference from a centralized version control system, where there’s one main server holding the project’s history, and users only download the latest version of the files to work on.

Here’s a quick comparison:

**Centralized VCS:** One central server has the full history. Users connect to it to get files or save changes. If the server goes down, collaboration stops.

**Distributed VCS (Git):** Every user has their own full copy of the project (called a repository). You can work independently and sync with others later.

In Git, your local repository isn’t just a snapshot—it’s the whole story, from the first change to the latest.


### How Does This “Distribution” Work?

The “distributed” part comes from how Git handles these repositories:

**Full Local Repository:** When you “clone” a project in Git, you download the entire project history to your machine—not just the current files, but every version ever made. This means you have everything you need right there, locally.

**Work Offline:** Because you have the full repository, you can make changes, save them (called committing), and even look at past versions—all without an internet connection.

**Sync with Others:** When you’re ready, you can share your changes with other people’s repositories (like pushing to a shared platform such as GitHub) or pull their changes into yours. This syncing happens directly between repositories, not through a single central point.

Imagine you and your teammates are working on a software project:

You clone the project to your laptop.

You make changes and commit them to your local repository.

Your teammate does the same on their computer.

Later, you both sync up by sharing your changes—maybe through a shared repository online or directly with each other.

This peer-to-peer setup is what makes Git distributed. There’s no required central server that everyone depends on (though platforms like GitHub are often used for convenience).

### Why Does This Matter?

This distributed nature makes Git:

**Flexible:** You can work anywhere, anytime, without needing constant access to a server.

**Resilient:** If one computer crashes, the project isn’t lost—every other copy has the full history.

**Collaborative:** Multiple programmers can work independently and merge their changes later, making teamwork smoother.

---


## GitHub.com

---

GitHub is a proprietary developer platform that allows developers to create, store, manage, and share their code. 

It uses Git to provide distributed version control and GitHub itself provides access control, bug tracking, software feature requests, task management, continuous integration, and wikis for every project.

## Other Git Based Systems


| Git-Based System                     | Description                                                                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **GitLab**                           | Open-source Git hosting solution with built-in CI/CD, issue tracking, and DevOps lifecycle tools. Self-hosted or SaaS.               |
| **Bitbucket**                        | Atlassian’s Git solution, tightly integrated with Jira, Trello, and other Atlassian tools. Supports both Git and Mercurial (legacy). |
| **SourceForge**                      | One of the original open-source code repositories. Supports Git, Subversion (SVN), and Mercurial.                                    |
| **Azure Repos**                      | Part of Azure DevOps by Microsoft. Offers Git and Team Foundation Version Control (TFVC) support.                                    |
| **AWS CodeCommit**                   | Fully managed source control service by Amazon Web Services. Supports Git repositories.                                              |
| **Gitea**                            | Lightweight self-hosted Git service. Open source, fast and simple alternative to GitHub/GitLab.                                      |
| **Gogs**                             | A painless, self-hosted Git service. Focused on minimalism and simplicity. Predecessor to Gitea.                                     |
| **Phabricator**                      | A suite of open-source tools for peer code review, task management, and project communication. (Now discontinued but still used).    |
| **Assembla**                         | Git and Subversion hosting with enterprise focus, including code reviews and project management.                                     |
| **RhodeCode**                        | Unified repository management tool that supports Git, Mercurial, and Subversion. Enterprise-focused.                                 |
| **Perforce Helix TeamHub**           | Git-compatible repositories with Perforce enterprise features. Ideal for hybrid setups.                                              |
| **Sr.ht**                            | Pronounced "SourceHut", it’s a lightweight, hacker-friendly Git hosting with full control and scripting support.                     |
| **Google Cloud Source Repositories** | Git repositories hosted on Google Cloud with built-in integration with Google Cloud Platform (GCP) services.                         |

---

### 🔹 Traditional Centralized VCS Tools

| Centralized VCS                                      | Description                                                                                                                                   |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Apache Subversion (SVN)**                          | One of the most widely used centralized VCS systems. Open-source and still used in enterprise and legacy systems.                             |
| **Microsoft Team Foundation Version Control (TFVC)** | Part of Azure DevOps (formerly TFS). Centralized VCS tailored for Microsoft ecosystem.                                                        |
| **Perforce Helix Core**                              | High-performance centralized VCS for large codebases and game development. Offers fine-grained access control.                                |
| **CVS (Concurrent Versions System)**                 | One of the oldest VCS systems. Now largely obsolete but still found in older projects.                                                        |
| **IBM Rational ClearCase**                           | Enterprise-level VCS used in large regulated industries (aerospace, defense, etc.). Centralized with powerful access and compliance features. |
| **PVCS (Serena Dimensions)**                         | A proprietary centralized version control system used in older enterprise environments.                                                       |
| **Visual SourceSafe (VSS)**                          | Microsoft’s legacy centralized VCS (now discontinued and replaced by TFVC/Git).                                                               |
| **BitKeeper**                                        | Originally a distributed system but with centralized control; historically used for Linux kernel before Git. Now open-source.                 |
| **AccuRev**                                          | Centralized VCS by Micro Focus, focused on parallel development and enterprise scalability.                                                   |
| **StarTeam**                                         | Another centralized solution by Micro Focus with strong role-based access and branching capabilities.                                         |

---

## Git Installation

Download the Git installer(software) from below URL based on your OS and install it

[Click Here](https://git-scm.com/downloads)

## 🧰 Step 1: Install Git

### 🔹 On Windows:

* Download Git from: [https://git-scm.com/download/win](https://git-scm.com/download/win)
* Install with default settings (include Git Bash)
* After install, open **Git Bash**

### 🔹 On Linux:

```bash
sudo apt update
sudo apt install git
```

### 🔹 On macOS:

```bash
brew install git
```

### ✅ Verify:

```bash
git --version
```

---

## 🌐 Step 2: Create a GitHub Account and Repo

1. Go to [https://github.com](https://github.com)
2. Sign up or log in
3. Click ➕ **"New Repository"**

   * Repository name: `hello-git`
   * Description: *My first Git + GitHub project*
   * Keep it **public**
   * Don’t initialize with README (we'll do it ourselves)
   * Click **Create repository**

You will now see a page with commands like:

```bash
git remote add origin https://github.com/yourusername/hello-git.git
```

---

## Git Commands - Part 1

[Click here](2_Git_Commands_Part_1.md) to learn about Git Commands

