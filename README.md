<h2 align="center">
    ──「 ⛦🦋 Kust Music - Premium Telegram VC Bot 🦋⛦ 」──
</h2>

<p align="center">
  <i>A powerful, open-source music bot for Telegram voice chats with custom deployment support</i>
</p>

<p align="center">
  <img src="https://files.catbox.moe/836l2k.jpg">
</p>
<p align="center">
<a href="https://github.com/kustbots/kustmusic/stargazers"><img src="https://img.shields.io/github/stars/kustbots/kustmusic?color=black&logo=github&logoColor=black&style=for-the-badge" alt="Stars" /></a>
<a href="https://github.com/kustbots/kustmusic/network/members"> <img src="https://img.shields.io/github/forks/kustbots/kustmusic?color=black&logo=github&logoColor=black&style=for-the-badge" /></a>
<a href="https://github.com/kustbots/kustmusic/blob/master/LICENSE"> <img src="https://img.shields.io/badge/License-Kust%20Protect-blueviolet?style=for-the-badge" alt="License" /> </a>
<a href="https://www.python.org/"> <img src="https://img.shields.io/badge/Written%20in-Python-orange?style=for-the-badge&logo=python" alt="Python" /> </a>
<a href="https://github.com/kustbots/kustmusic/commits/main"> <img src="https://img.shields.io/github/last-commit/kustbots/kustmusic?color=blue&logo=github&logoColor=green&style=for-the-badge" /></a>
</p>

---

## 🚀 Features

- 🎧 Play music in Telegram VC groups.
- 💥 Fully open source and free.
- ☁️ Can run easily on **Render**, **Koyeb**, or your VPS.
- 🌱 Easy to set up with one-click deploy buttons.
- ❄️ Uses custom KustGram fork for enhanced stability.

---


## 💡 Quick Deploy

<p align="center">
<a href="https://deploy.kustbotsweb.workers.dev"><img src="https://img.shields.io/badge/-Deploy%20to%20Render-blueviolet?style=for-the-badge&logo=render"></a>
<a href="https://deploy.kustbotsweb.workers.dev"><img src="https://img.shields.io/badge/-Deploy%20to%20Koyeb-green?style=for-the-badge&logo=koyeb"></a>
<a href="https://deploy.kustbotsweb.workers.dev"><img src="https://img.shields.io/badge/-Deploy%20to%20Railway-cyan?style=for-the-badge&logo=railway"></a>
<a href="https://deploy.kustbotsweb.workers.dev"><img src="https://img.shields.io/badge/-Deploy%20to%20Heroku-purple?style=for-the-badge&logo=heroku"></a>
</p>




## ⚡ One-click Setup

<p align="center">
<a href="https://github.com/kustbots/kustmusic/fork"><img src="https://img.shields.io/badge/-Fork%20Repo-black?style=for-the-badge&logo=github"></a>
</p>

---

## 🔴 Render Deployment Guide

**⚠️ IMPORTANT:** To deploy on **Render**, you must follow these steps:

1. **Import the Repository to Render:**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click **"New +"** → **"Web Service"**
   - Select **"Deploy an existing repository"**
   - Connect your GitHub and select the **kustmusic** repo

2. **Modify main.py for Render:**
   - You **MUST** modify the `main.py` file to work on Render
   - Change the host configuration from `localhost` to `0.0.0.0`
   - Update any hardcoded local paths to use environment variables
   - Ensure the bot can bind to the port provided by Render (`$PORT` environment variable)

3. **Set Environment Variables:**
   - Add all required variables from `kust.env` in Render's **Environment** settings
   - Never hardcode sensitive data

4. **Deploy:**
   - Set the start command to: `python3 main.py`
   - Click **"Deploy Web Service"**

⚠️ **Without modifying main.py, the deployment will fail!**

---

## 🤖 Customize Your Bot Using AI

To protect the original repository and ensure each deployment is unique, **you MUST modify main.py before deploying**.

### Easy Method: Use Any AI (Claude, ChatGPT, etc.)

1. **Copy the AI Prompt below**
2. **Open Claude, ChatGPT, or any AI tool**
3. **Paste the prompt and your main.py file**
4. **Get your custom version instantly!**

### 📋 AI Prompt to Customize main.py

```
Please modify this main.py file for my Telegram music bot deployment. Make the following changes:

1. Change variable names and function names to unique names (not generic like "bot", "player", etc.)
2. Restructure the code flow - reorganize function order and logic
3. Modify all comments and docstrings to be different wording
4. Change the way imports are structured
5. Modify error handling messages to be unique
6. Add unique logging patterns and debug messages
7. Change any hardcoded values or defaults to different values
8. Reorganize the main() function logic
9. Modify string literals and messages to be different

Keep all functionality intact - only change the code structure, naming, and comments. Make it unique so it won't trigger platform detection systems.

Here's the main.py file to modify:

[PASTE YOUR main.py FILE HERE]
```

### Steps:

1. Go to [Claude.ai](https://claude.ai) or [ChatGPT](https://chatgpt.com)
2. Copy the prompt above
3. Replace `[PASTE YOUR main.py FILE HERE]` with your actual main.py content
4. Submit and get your customized version
5. Use your custom version for deployment
6. **IMPORTANT:** Fork the repository before deploying!

---

## 🛠️ Required environment variables




**𝙏𝙀𝙎𝙏 𝘽𝙊𝙏 ➣ [kust music](https://t.me/vcmusiclubot)**



<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ʟᴏᴄᴀʟ ʜᴏsᴛ/ ᴠᴘs 」─
</h3>

- Get your [Necessary Variables](https://github.com/kustbots/kustmusic/blob/master/kust.env)
- <p align="center">
<a href="https://www.youtube.com/watch?v=LSlKMWmhh20"><img src="https://img.shields.io/badge/Watch%20on-YouTube-red?style=for-the-badge&logo=youtube" alt="YouTube Tutorial"/></a>
</p>

---

### 🔧 Quick Setup

1. **Upgrade & Update:**
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   ```

2. **Install Required Packages:**
   ```bash
   sudo apt-get install python3-pip ffmpeg -y
   ```
3. **Setting up PIP**
   ```bash
   sudo pip3 install -U pip
   ```
4. **Installing Node**
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
7. **Create .env  with sample.env**
   ```bash
   cp kust.env .env
   ```
   - Edit .env with your vars
8. **Editing Vars:**
   ```bash
   vi .env
   ```
   - Edit .env with your values.
   - Press `I` button on keyboard to start editing.
   - Press `Ctrl + C`  once you are done with editing vars and type `:wq` to save .env or `:qa` to exit editing.
9. **Installing tmux**
    ```bash
    sudo apt install tmux -y && tmux
    ```
10. **Run the Bot**
    ```bash
    python3 main.py
━━━━━━━━━━━━━━━━━━━━

<h3 align="center">
    ─「 sᴜᴩᴩᴏʀᴛ 」─
</h3>

<p align="center">
<a href="https://t.me/Frozensupport1"><img src="https://img.shields.io/badge/-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>

<p align="center">
<a href="https://t.me/Frozensupport1"><img src="https://img.shields.io/badge/-Support%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>

- <b> _sᴩᴇᴄɪᴀʟ ᴛʜᴀɴᴋs ᴛᴏ [KustBots](https://github.com/kustbots) ғᴏʀ [ᴍᴜsɪᴄ ʙᴏᴛ](https://github.com/kustbots/kustmusic)_</b>
