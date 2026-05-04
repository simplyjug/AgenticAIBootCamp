# Publish this repository to GitHub

Your machine cannot push to GitHub **until you authenticate**. This guide covers the standard path.

## 1. One-time: GitHub account & auth

- Create an account at [github.com](https://github.com/) if needed.
- Install [Git](https://git-scm.com/downloads) and optionally [GitHub CLI](https://cli.github.com/) (`gh`).

**HTTPS + Personal Access Token (classic):**  
GitHub → **Settings → Developer settings → Personal access tokens** — generate with `repo` scope. Use the token as the password when Git prompts (username = your GitHub username).

**Or SSH:** add an SSH key in GitHub settings and use `git@github.com:USER/AgenticAIBootCamp.git`.

## 2. Initialize git (if not already)

From the project root:

```bash
git init
git add .
git commit -m "Initial commit: AI engineering bootcamp curriculum and labs"
git branch -M main
```

This repo ships with a **`.gitignore`** (`.venv`, `site/`, `.env`, etc.).

## 3. Create the remote repository

**Option A — GitHub website:** New repository → name `AgenticAIBootCamp` → **do not** add README (you already have one). Copy the remote URL.

**Option B — GitHub CLI:**

```bash
gh auth login
gh repo create AgenticAIBootCamp --public --source=. --remote=origin --push
```

## 4. Connect and push

```bash
git remote add origin https://github.com/<YOUR_USER>/AgenticAIBootCamp.git
git push -u origin main
```

## 5. Enable CI & Pages

- **Actions:** Settings → Actions → allow workflows. The **CI** workflow runs on `main` / PRs.
- **Pages (optional):** follow [DEPLOY.md](DEPLOY.md); enable **GitHub Pages** from `gh-pages` after the docs workflow runs.

## 6. Polish your profile

- Pin the repository on your GitHub profile.
- Replace `YOUR_GITHUB_USERNAME` in [README.md](README.md) and `mkdocs.yml`.
- Add **`portfolio/NOTES.md`** in your fork describing *your* extensions (see [docs/CAREER_PORTFOLIO.md](docs/CAREER_PORTFOLIO.md)).

### Note for Cursor / AI assistants

Assistants **cannot** complete OAuth or push with your credentials from this environment. You run `git push` locally after `gh auth login` or credential helper setup.
