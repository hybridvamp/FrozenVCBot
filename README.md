<div align="center">

```
██╗  ██╗██╗   ██╗███████╗████████╗    ███╗   ███╗██╗   ██╗███████╗██╗ ██████╗
██║ ██╔╝██║   ██║██╔════╝╚══██╔══╝    ████╗ ████║██║   ██║██╔════╝██║██╔════╝
█████╔╝ ██║   ██║███████╗   ██║       ██╔████╔██║██║   ██║███████╗██║██║
██╔═██╗ ██║   ██║╚════██║   ██║       ██║╚██╔╝██║██║   ██║╚════██║██║██║
██║  ██╗╚██████╔╝███████║   ██║       ██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝
```

<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=20&pause=1000&color=00D4FF&center=true&vCenter=true&width=700&lines=🎧+Premium+Telegram+VC+Music+Bot;⚡+Powered+by+yt-dlp+%2B+PyTgCalls;🤖+Multi-Bot+Clone+System;🚀+Deploy+on+Render+%7C+Koyeb+%7C+Railway+%7C+Heroku"/>
</p>

<p align="center">
<a href="https://github.com/kustbots/kustmusic/stargazers"><img src="https://img.shields.io/github/stars/kustbots/kustmusic?color=black&logo=github&logoColor=white&style=for-the-badge" alt="Stars"/></a>
<a href="https://github.com/kustbots/kustmusic/network/members"><img src="https://img.shields.io/github/forks/kustbots/kustmusic?color=black&logo=github&logoColor=white&style=for-the-badge"/></a>
<a href="https://github.com/kustbots/kustmusic/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-Kust%20Protect-blueviolet?style=for-the-badge" alt="License"/></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Written%20in-Python-orange?style=for-the-badge&logo=python" alt="Python"/></a>
<a href="https://github.com/kustbots/kustmusic/commits/main"><img src="https://img.shields.io/github/last-commit/kustbots/kustmusic?color=blue&logo=github&logoColor=green&style=for-the-badge"/></a>
</p>

</div>

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🎧 **VC Playback** | Stream music directly into Telegram voice chats |
| ⚡ **yt-dlp Engine** | Downloads audio via yt-dlp — no external API dependency |
| 🍪 **Cookie Support** | Add `cookies.txt` to bypass rate limits and age restrictions |
| 🤖 **Clone System** | Deploy unlimited bots from a single instance with `/clone` |
| 🛡️ **Admin Controls** | Kick, ban, mute, unmute, and manage group members |
| 📊 **Live Progress Bar** | Real-time progress bar updates every 10 seconds |
| 🔄 **Queue System** | Add multiple songs, auto-plays next when current ends |
| ☁️ **Cloud Ready** | Runs on Render, Koyeb, Railway, Heroku, or your VPS |
| 🌱 **Zero Database** | No MongoDB required — pure in-memory state |

---

## 💡 Quick Deploy

<p align="center">
<a href="https://deploy.kustbotsweb.workers.dev"><img src="https://img.shields.io/badge/-Deploy%20to%20Render-blueviolet?style=for-the-badge&logo=render"></a>
<a href="https://deploy.kustbotsweb.workers.dev"><img src="https://img.shields.io/badge/-Deploy%20to%20Koyeb-green?style=for-the-badge&logo=koyeb"></a>
<a href="https://deploy.kustbotsweb.workers.dev"><img src="https://img.shields.io/badge/-Deploy%20to%20Railway-cyan?style=for-the-badge&logo=railway"></a>
<a href="https://deploy.kustbotsweb.workers.dev"><img src="https://img.shields.io/badge/-Deploy%20to%20Heroku-purple?style=for-the-badge&logo=heroku"></a>
</p>

<p align="center">
<a href="https://github.com/kustbots/kustmusic/fork"><img src="https://img.shields.io/badge/-Fork%20Repo-black?style=for-the-badge&logo=github"></a>
</p>

---

## 🔴 Render Deployment Guide

> ⚠️ **IMPORTANT — Read before deploying on Render**

**Step 1 — Fork this repo**
- Go to the top of this page and click **Fork**
- Do NOT deploy directly from the original repo

**Step 2 — Customize your `main.py`**
- You **MUST** modify `main.py` before deploying (see AI Customization below)
- Direct copies from the same repo will trigger Render's duplicate detection

**Step 3 — Connect to Render**
1. Go to [dashboard.render.com](https://dashboard.render.com)
2. Click **New +** → **Web Service**
3. Select **"Build and deploy from a Git repository"**
4. Connect your GitHub and select your **forked** repo
5. Render auto-detects `render.yaml` — all settings are pre-configured

**Step 4 — Set Environment Variables**

Add these in Render's **Environment** tab:

| Variable | Description | Required |
|---|---|---|
| `BOT_TOKEN` | Bot token from [@BotFather](https://t.me/BotFather) | ✅ |
| `ASSISTANT_SESSION` | Pyrogram string session | ✅ |
| `API_ID` | From [my.telegram.org](https://my.telegram.org) | ✅ |
| `API_HASH` | From [my.telegram.org](https://my.telegram.org) | ✅ |
| `OWNER_ID` | Your Telegram user ID | ✅ |
| `SEARCH_API_URL` | Leave blank for default | ❌ |

**Step 5 — Deploy**
- Click **"Create Web Service"** and wait for the build to finish

---

## 🤖 Clone System

Once deployed, you can host **multiple bots from a single instance** using the `/clone` command.

```
/clone <BOT_TOKEN>
```

- Send this command in **private chat** with your bot
- Get bot tokens from [@BotFather](https://t.me/BotFather)
- Each dyno supports up to **20 clones**
- Each clone runs independently with its own owner

**Check active clones:**
```
/active
```
*(Main owner only)*

---

## 🍪 Cookies Setup (Optional but Recommended)

Add a `cookies.txt` file to your repo to avoid YouTube rate limits.

**How to export cookies:**
1. Install **"Get cookies.txt LOCALLY"** extension on Chrome/Firefox
2. Open [youtube.com](https://youtube.com) and log in
3. Click the extension → Export cookies for `youtube.com`
4. Replace `cookies.txt` in the repo with your exported file

> ⚠️ Never share your `cookies.txt` publicly — it gives access to your YouTube account.

---

## 🤖 AI Customization (Required for Cloud Deploy)

To avoid platform bans, each deployment must have a **unique `main.py`**. Use any AI to generate a variant:

### Prompt to use with Claude / ChatGPT:

```
Please modify this main.py file for my Telegram music bot deployment.
Make these changes while keeping all functionality intact:

1. Rename variables and functions to unique names
2. Restructure the code flow and reorganize function order
3. Rewrite all comments in different wording
4. Reorganize import structure
5. Modify error/log messages to be unique
6. Change any hardcoded defaults to slightly different values
7. Rearrange the main() function logic

Keep everything working exactly the same — only change structure and naming
to make this deployment unique and avoid duplicate detection.

Here is my main.py:
[PASTE YOUR main.py CONTENT HERE]
```

**Steps:**
1. Go to [claude.ai](https://claude.ai) or [chatgpt.com](https://chatgpt.com)
2. Paste the prompt above + your `main.py` content
3. Get your unique version
4. Replace `main.py` in your fork with the AI-generated version
5. Deploy

---

## 🛠️ Required Environment Variables

Get your variables from [`kust.env`](https://github.com/kustbots/kustmusic/blob/master/kust.env)

**Test Bot ➣** [Kust Music](https://t.me/vcmusiclubot)

---

<h3 align="center">─「 ᴅᴇᴩʟᴏʏ ᴏɴ ʟᴏᴄᴀʟ ʜᴏsᴛ / ᴠᴘs 」─</h3>

<p align="center">
<a href="https://www.youtube.com/watch?v=LSlKMWmhh20"><img src="https://img.shields.io/badge/Watch%20on-YouTube-red?style=for-the-badge&logo=youtube" alt="YouTube Tutorial"/></a>
</p>

### 🔧 VPS Setup

1. **Upgrade & Update**
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   ```

2. **Install Required Packages**
   ```bash
   sudo apt-get install python3-pip ffmpeg -y
   ```

3. **Setup PIP**
   ```bash
   sudo pip3 install -U pip
   ```

4. **Install Node**
   ```bash
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash && source ~/.bashrc && nvm install v18
   ```

5. **Clone the Repository**
   ```bash
   git clone https://github.com/kustbots/kustmusic && cd kustmusic
   ```

6. **Install Requirements**
   ```bash
   pip3 install -U -r requirements.txt
   ```

7. **Setup Environment**
   ```bash
   cp kust.env .env
   vi .env
   ```
   - Press `I` to start editing
   - Fill in your variables
   - Press `Ctrl + C` then type `:wq` to save

8. **Run with tmux**
   ```bash
   sudo apt install tmux -y && tmux
   python3 main.py
   ```

---

## 📜 Commands

| Command | Description | Who |
|---|---|---|
| `/play <song>` | Play a song or YouTube URL | Everyone |
| `/skip` | Skip current song | Admins |
| `/stop` | Stop and clear queue | Admins |
| `/pause` | Pause playback | Admins |
| `/resume` | Resume playback | Admins |
| `/clear` | Clear the queue | Admins |
| `/ping` | Bot stats and latency | Everyone |
| `/clone <token>` | Clone a new bot instance | Anyone (private) |
| `/active` | List all active clones | Main Owner |
| `/kick` | Kick a user (reply) | Admins |
| `/ban` | Ban a user (reply) | Admins |
| `/unban` | Unban a user (reply) | Admins |
| `/mute` | Mute a user (reply) | Admins |
| `/unmute` | Unmute a user (reply) | Admins |

---

<h3 align="center">─「 sᴜᴩᴩᴏʀᴛ 」─</h3>

<p align="center">
<a href="https://t.me/kustbots"><img src="https://img.shields.io/badge/-Updates%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
<a href="https://t.me/kustbots"><img src="https://img.shields.io/badge/-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>

<p align="center">
<b>Special Thanks to <a href="https://github.com/kustbots">KustBots</a> for <a href="https://github.com/kustbots/kustmusic">Kust Music Bot</a></b>
</p>
