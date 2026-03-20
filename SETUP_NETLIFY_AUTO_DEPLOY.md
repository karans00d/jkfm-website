# JKFM — Auto-Deploy from GitHub to Netlify

This guide turns your jkfm-website folder into a GitHub repo and connects it to Netlify for automatic deployment on every push.

**Time:** ~15 minutes

---

## Part 1: Put the website on GitHub

### Step 1: Create a new repo on GitHub

1. Go to [github.com](https://github.com) and sign in
2. Click the **+** (top right) → **New repository**
3. **Repository name:** `jkfm-website` (or `jkfm.co`)
4. **Description:** *Optional* — e.g. "JK Facilities Management website"
5. **Public**
6. **Do NOT** check "Add a README" or .gitignore — we have existing files
7. Click **Create repository**

### Step 2: Initialize Git in your website folder

Open a terminal in `C:\Users\jingj\projects\jkfm-website` and run:

```powershell
cd C:\Users\jingj\projects\jkfm-website

git init
git add .
git commit -m "Initial commit - JKFM website"
```

### Step 3: Connect to GitHub and push

Replace `YOUR_USERNAME` with your GitHub username (e.g. karans00d):

```powershell
git remote add origin https://github.com/YOUR_USERNAME/jkfm-website.git
git branch -M main
git push -u origin main
```

You'll be prompted for your GitHub username and password. If you use 2FA, use a **Personal Access Token** instead of your password:
- GitHub → Settings → Developer settings → Personal access tokens → Generate new token
- Give it `repo` scope

---

## Part 2: Connect Netlify to GitHub

### Step 4: Add site in Netlify (or reconnect)

1. Go to [app.netlify.com](https://app.netlify.com)
2. Click **Add new site** → **Import an existing project**
3. Click **Deploy with GitHub**
4. Authorize Netlify to access your GitHub if asked
5. Find **jkfm-website** in the list → click **Import**

### Step 5: Build settings (important for static HTML)

For a plain HTML site, Netlify needs almost nothing:

| Setting | Value |
|---------|-------|
| **Branch to deploy** | `main` |
| **Build command** | *(leave blank)* |
| **Publish directory** | `.` (just a dot — the root) |

Click **Deploy site**.

### Step 6: Domain (if jkfm.co is already on Netlify)

If jkfm.co is already set up on this Netlify account:

- Netlify may create a **new** site with a random URL (e.g. `random-name-123.netlify.app`)
- Go to **Domain settings** → **Add custom domain** → enter `jkfm.co`
- Or: Delete the old manual-deploy site and use this new one as primary

If you had drag-and-drop deploys before, you may have an existing site. You can either:
- **Replace it:** Point the existing site to the new GitHub repo (Site settings → Build & deploy → Link repository)
- **Keep both:** Use the new GitHub-connected site and update your custom domain to point to it

---

## Part 3: Verify

### Step 7: Test the flow

1. Make a tiny change (e.g. add a comment in `index.html`)
2. Commit and push:
   ```powershell
   cd C:\Users\jingj\projects\jkfm-website
   git add .
   git commit -m "Test deploy"
   git push
   ```
3. Go to Netlify → **Deploys** — you should see a new deploy start automatically
4. When it finishes, check https://jkfm.co — your change should be live

---

## From now on

Every time you:
```powershell
git add .
git commit -m "Your message"
git push
```

Netlify will automatically rebuild and deploy. No more drag-and-drop.

---

## Troubleshooting

**"Publish directory" warning** — For a static HTML site, use `.` (current directory). Don't use `dist` or `public` unless you have a build step.

**Domain not working** — In Netlify: Domain settings → Verify DNS. You may need to add CNAME or A records at your domain registrar.

**Old site still showing** — Clear browser cache or try incognito. DNS can take a few minutes to propagate.
