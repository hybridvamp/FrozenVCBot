<div align="center">

```
 ██╗  ██╗██╗   ██╗███████╗████████╗
 ██║ ██╔╝██║   ██║██╔════╝╚══██╔══╝
 █████╔╝ ██║   ██║███████╗   ██║
 ██╔═██╗ ██║   ██║╚════██║   ██║
 ██║  ██╗╚██████╔╝███████║   ██║
 ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝

     🎵 MUSIC BOT 🎵

  ⚡ yt-dlp Powered
  🤖 Clone System
  🚀 Cloud Ready
```

<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=20&pause=1000&color=00D4FF&center=true&vCenter=true&width=700&lines=🎧+Premium+Telegram+VC+Music+Bot;⚡+Powered+by+yt-dlp+%2B+Kurigram;🤖+Multi-Bot+Clone+System;🚀+Deploy+on+Render+%7C+Koyeb+%7C+Railway+%7C+VPS"/>
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
| ⚡ **yt-dlp Engine** | Downloads audio via yt-dlp — no external API needed |
| 🍪 **Cookie Support** | Add `cookies.txt` to bypass YouTube rate limits |
| 🤖 **Clone System** | Add unlimited bot instances with `/clone` |
| 🛡️ **Admin Controls** | Kick, ban, mute, unmute group members |
| 📊 **Live Progress Bar** | Real-time progress updates every 10 seconds |
| 🔄 **Queue System** | Add multiple songs, auto-plays next in queue |
| ☁️ **Cloud Ready** | Runs on Render, Koyeb, Railway, or your VPS |
| 🌱 **Zero Database** | No MongoDB — pure in-memory state |
| 🔥 **Kurigram Powered** | Built on Kurigram — latest Telegram API features |

---

## 📁 Project Structure

```
kustmusic/
├── main.py              ← Entry point, starts all services
├── config.py            ← All environment variables
├── state.py             ← In-memory state (queues, clients)
├── clients.py           ← Pyrogram + PyTgCalls client setup
├── server.py            ← Dummy HTTP server for Render/Koyeb
├── kust.env             ← Environment variable template
├── render.yaml          ← Render deployment config
├── Procfile             ← Koyeb/Heroku start command
├── cookies.txt          ← YouTube cookies (optional)
├── requirements.txt     ← Python dependencies
├── core/
│   ├── api.py           ← YouTube search + yt-dlp download
│   ├── guards.py        ← Admin check + rate limiting
│   ├── helpers.py       ← Formatting utilities
│   └── playback.py      ← Music streaming core logic
└── handlers/
    ├── router.py        ← Registers all command handlers
    ├── music.py         ← /play, /stop, /skip, /pause, /resume
    ├── admin.py         ← /kick, /ban, /mute, /unmute
    ├── system.py        ← /start, /ping, /clone, /active
    └── callbacks.py     ← Inline button handler
```

---

## 💡 Quick Deploy

<p align="center">
<a href="https://deploy.kustbotsweb.workers.dev"><img src="https://img.shields.io/badge/-Deploy%20to%20Render-blueviolet?style=for-the-badge&logo=render"></a>
<a href="https://deploy.kustbotsweb.workers.dev"><img src="https://img.shields.io/badge/-Deploy%20to%20Koyeb-green?style=for-the-badge&logo=koyeb"></a>
<a href="https://deploy.kustbotsweb.workers.dev"><img src="https://img.shields.io/badge/-Deploy%20to%20Railway-cyan?style=for-the-badge&logo=railway"></a>
</p>

<p align="center">
<a href="https://github.com/kustbots/kustmusic/fork"><img src="https://img.shields.io/badge/-Fork%20Repo-black?style=for-the-badge&logo=github"></a>
</p>

---

## 🔴 Deploy on Render

> ⚠️ **IMPORTANT — Fork the repo first. Do NOT deploy directly from the original.**

**Step 1 — Fork**
- Click **Fork** at the top of this page
- This creates your own copy you can deploy from

**Step 2 — Connect to Render**
1. Go to [dashboard.render.com](https://dashboard.render.com)
2. Click **New +** → **Web Service**
3. Select **"Build and deploy from a Git repository"**
4. Connect your GitHub and select your **forked** repo
5. Render auto-detects `render.yaml` — all settings are pre-configured

**Step 3 — Set Environment Variables**

Add these in Render's **Environment** tab:

| Variable | Description | Required |
|---|---|---|
| `BOT_TOKEN` | Bot token from [@BotFather](https://t.me/BotFather) | ✅ |
| `ASSISTANT_SESSION` | Pyrogram string session for userbot | ✅ |
| `API_ID` | From [my.telegram.org](https://my.telegram.org) | ✅ |
| `API_HASH` | From [my.telegram.org](https://my.telegram.org) | ✅ |
| `OWNER_ID` | Your Telegram user ID | ✅ |
| `SEARCH_API_URL` | Leave blank for default | ❌ |

**Step 4 — Deploy**
- Click **"Create Web Service"** — build takes ~3 minutes

> 💡 **How to get ASSISTANT_SESSION:** Use [@StringFatherBot](https://t.me/StringFatherBot) to generate a Pyrogram string session from your Telegram account.

---

## 🤖 Clone System

Once deployed, you can add **multiple bot instances** with `/clone`:

```
/clone <BOT_TOKEN>
```

- Send this in **private chat** with your deployed bot
- Get new bot tokens from [@BotFather](https://t.me/BotFather)
- Each clone runs independently with its own owner
- No limit — add as many as you need

**Check active bots:**
```
/active
```
*(Main owner only)*

---

## 🍪 Cookies Setup (Optional)

Add a `cookies.txt` to bypass YouTube rate limits and age restrictions.

**How to export:**
1. Install **"Get cookies.txt LOCALLY"** extension on Chrome/Firefox
2. Open [youtube.com](https://youtube.com) and log in to your account
3. Click the extension → Export cookies for `youtube.com`
4. Replace the `cookies.txt` in your forked repo with the exported file

> ⚠️ Never share your `cookies.txt` — it gives access to your YouTube account.

---

## 🤖 AI Customization (Avoid Platform Bans)

Each deployment needs a **unique codebase** to avoid platform duplicate detection. Use any AI to help:

### Prompt for Claude / ChatGPT:

```
I have a modular Telegram music bot with these files:
main.py, config.py, state.py, clients.py, server.py,
core/api.py, core/guards.py, core/helpers.py, core/playback.py,
handlers/router.py, handlers/music.py, handlers/admin.py,
handlers/system.py, handlers/callbacks.py

Please help me make this deployment unique by:
1. Renaming variables and functions to unique names across all files
2. Rewriting log/error messages to be different
3. Reorganizing code flow within functions (keeping same behavior)
4. Changing any hardcoded string literals to different wording

Keep all functionality exactly the same — only change names and structure
to make this deployment unique. Show me each file separately.

Here are the files: [PASTE EACH FILE CONTENT]
```

**Steps:**
1. Open [claude.ai](https://claude.ai) or [chatgpt.com](https://chatgpt.com)
2. Paste the prompt + all your file contents
3. Get unique versions of each file
4. Replace the files in your fork
5. Deploy

---

## 🛠️ Environment Variables Reference

Copy [`kust.env`](https://github.com/kustbots/kustmusic/blob/master/kust.env) and rename it to `.env` for local/VPS use.

**Test Bot ➣** [Kust Music](https://t.me/vcmusiclubot)

---

<h3 align="center">─「 ᴅᴇᴩʟᴏʏ ᴏɴ ᴠᴘs / ʟᴏᴄᴀʟ 」─</h3>

<p align="center">
<a href="https://www.youtube.com/watch?v=LSlKMWmhh20"><img src="https://img.shields.io/badge/Watch%20on-YouTube-red?style=for-the-badge&logo=youtube" alt="YouTube Tutorial"/></a>
</p>

### 🔧 VPS Setup

1. **Update system**
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   ```

2. **Install dependencies**
   ```bash
   sudo apt-get install python3-pip ffmpeg -y
   ```

3. **Clone the repo**
   ```bash
   git clone https://github.com/kustbots/kustmusic && cd kustmusic
   ```

4. **Install Python packages**
   ```bash
   pip3 install -U -r requirements.txt
   ```

5. **Setup environment**
   ```bash
   cp kust.env .env
   nano .env
   ```
   Fill in your variables, then `Ctrl+X` → `Y` → Enter to save.

6. **Run with tmux**
   ```bash
   sudo apt install tmux -y
   tmux new -s music
   python3 main.py
   ```
   Press `Ctrl+B` then `D` to detach (bot keeps running).

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
| `/clone <token>` | Add a new bot instance | Anyone (private) |
| `/active` | List all active bots | Main Owner |
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
<b>Made with ❤️ by <a href="https://github.com/kustbots">KustBots</a></b>
</p>
