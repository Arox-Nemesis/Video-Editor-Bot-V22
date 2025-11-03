# 🚀 Railway Deployment Guide

## Step 1: Push to GitHub

```bash
# If you haven't already
git init
git add .
git commit -m "Deploy Telegram Video Editor Bot"
git branch -M main
git remote add origin https://github.com/yourusername/Video-Editor-Bot-V22.git
git push -u origin main
```

## Step 2: Deploy on Railway

1. **Go to [railway.app](https://railway.app)**

2. **Sign up with GitHub** (free)

3. **Click "New Project"** → "Deploy from GitHub repo"

4. **Select your repository** (`Video-Editor-Bot-V22`)

5. **Configure Environment Variables:**
   ```
   API_ID=your_api_id_here
   API_HASH=your_api_hash_here
   BOT_TOKEN=your_bot_token_here
   MONGO_URI=mongodb://mongo:27017/video_editor_bot
   MAX_FILE_SIZE=2147483648
   PROCESSING_TIMEOUT=300
   LOG_LEVEL=INFO
   ```

6. **Click "Deploy"**

That's it! Your bot will be live in 2-3 minutes.

## Step 3: Get Your Bot URL

After deployment, Railway will give you a URL like:
`https://video-editor-bot.up.railway.app`

Your bot is now running 24/7 for free!

## Free Tier Limits

- **$5 credit** per month (enough for this bot)
- **750 hours** of runtime per month
- **100GB bandwidth** per month
- **1GB storage** per month

## Monitoring

- Check logs in Railway dashboard
- Monitor resource usage
- Automatic restarts on crashes