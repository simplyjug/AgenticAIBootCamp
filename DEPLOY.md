# Deploying this repo on GitHub

## Fork and clone

1. Click **Fork** on GitHub (top right of the upstream repo).
2. Clone **your** fork:
   ```bash
   git clone https://github.com/<your-username>/AgenticAIBootCamp.git
   cd AgenticAIBootCamp
   ```

## Enable CI

1. In your fork: **Settings → Actions → General → Actions permissions** → allow actions.
2. Push a branch; [.github/workflows/ci.yml](.github/workflows/ci.yml) runs lint + tests on Python 3.11.

## Optional: documentation site (MkDocs + GitHub Pages)

The repo includes `mkdocs.yml` and the `handbook/` directory (snippets that **include** the real markdown under `curriculum/`, `docs/`, and the repo root). This follows modern MkDocs rules: the published site is not the whole repo root.

**Local preview:**

```bash
pip install mkdocs mkdocs-material
mkdocs serve
```

Open `http://127.0.0.1:8000`.

**Publish to GitHub Pages** (after `pip install mkdocs mkdocs-material`):

```bash
mkdocs gh-deploy
```

Or rely on **GitHub Actions**: [.github/workflows/docs.yml](.github/workflows/docs.yml) builds and deploys to the `gh-pages` branch when you push to `main`.

**First-time GitHub Pages setup:**

1. Repo **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: **gh-pages** / **/ (root)**

Your site will be at `https://<user>.github.io/AgenticAIBootCamp/` (path may match repo name).

## Environment secrets (CI)

If you add integration tests that call live APIs, use **Settings → Secrets and variables → Actions** and never commit API keys. The default CI does not require `OPENAI_API_KEY`.

## Docker stack (local)

See [SETUP.md](SETUP.md) for `docker-compose` and databases used in later weeks.
