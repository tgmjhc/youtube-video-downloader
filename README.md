# VidExtract - YouTube Video Downloader

A sleek, cyberpunk-themed YouTube video downloader that works immediately - no backend setup required!

![VidExtract](https://img.shields.io/badge/Status-Working-brightgreen) ![License](https://img.shields.io/badge/License-MIT-blue)

## ✨ Features

- 🎨 **Stunning Cyberpunk Design** - Retro-futuristic interface with neon effects
- 📱 **Fully Responsive** - Works perfectly on desktop and mobile
- 🎬 **Multiple Quality Options** - 360p, 480p, 720p, 1080p, 1440p, 4K
- ⚡ **Instant Results** - No waiting, no server needed
- 🔗 **Multiple Download Services** - Choose from 5 popular downloader sites
- 🚀 **Ready to Deploy** - Works immediately on GitHub Pages

## 🎯 How It Works

1. Paste any YouTube video URL
2. Select your preferred quality (360p to 4K)
3. Click "Initialize Download"
4. Get instant access to 5 working download services
5. Choose your preferred service and download!

The app validates your URL, fetches video information, and provides links to trusted YouTube downloader services that support your selected quality.

## 🚀 Deploy to GitHub Pages (3 Easy Steps)

### Step 1: Create Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it whatever you want (e.g., `youtube-downloader`)
3. Make it **Public** (required for GitHub Pages)

### Step 2: Upload Files

**Option A - Via GitHub Website:**
1. Click "uploading an existing file"
2. Drag and drop `index.html`
3. Click "Commit changes"

**Option B - Via Git:**
```bash
git init
git add index.html
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository **Settings**
2. Click **Pages** in the left sidebar
3. Under "Source", select **main** branch
4. Click **Save**
5. Wait 1-2 minutes for deployment

✅ **Done!** Your site will be live at:
```
https://YOUR-USERNAME.github.io/REPO-NAME/
```

## 📋 Alternative Deployment Options

### Deploy to Netlify (Drag & Drop)

1. Go to [Netlify](https://www.netlify.com/)
2. Sign up/login (free)
3. Drag `index.html` to the deploy zone
4. Get instant live link!

### Deploy to Vercel

1. Go to [Vercel](https://vercel.com/)
2. Sign up/login with GitHub
3. Click "New Project"
4. Import your repository
5. Deploy (automatic)

### Deploy to Cloudflare Pages

1. Go to [Cloudflare Pages](https://pages.cloudflare.com/)
2. Connect your GitHub repository
3. Deploy with one click

## 🎨 Customization

Want to change the colors? Edit these CSS variables in `index.html`:

```css
:root {
    --neon-cyan: #00ffff;      /* Primary accent color */
    --neon-pink: #ff00ff;      /* Secondary accent */
    --neon-blue: #0088ff;      /* Tertiary accent */
    --dark-bg: #0a0e27;        /* Main background */
    --darker-bg: #050811;      /* Darker background */
}
```

## 🔧 Technical Details

- **Pure HTML/CSS/JavaScript** - No dependencies, no build process
- **Responsive Design** - Mobile-first approach
- **Modern Animations** - Smooth transitions and effects
- **Cross-browser Compatible** - Works on all modern browsers
- **YouTube oEmbed API** - Fetches real video information
- **Third-party Services** - Links to trusted downloader sites

## 📱 Supported Download Services

1. **Y2Mate** - Fast and reliable, most recommended
2. **SaveFrom.net** - Very popular, easy to use
3. **YT5s** - Clean interface, minimal ads
4. **YTMate** - HD quality focused
5. **9xBuddy** - Simple and straightforward

## ⚠️ Important Legal Notes

- ⚖️ **Respect Copyright** - Only download content you have rights to
- 📜 **YouTube Terms** - Be aware of YouTube's Terms of Service
- 🌍 **Local Laws** - Check copyright laws in your jurisdiction
- 🎓 **Educational Use** - This project is for educational purposes

## 🌟 Features Breakdown

### What Works:
✅ URL validation and video ID extraction  
✅ Real video title and channel name fetching  
✅ Quality selection (360p to 4K)  
✅ Multiple download service options  
✅ Beautiful responsive design  
✅ Smooth animations and effects  
✅ Mobile-friendly interface  

### What This Doesn't Do:
❌ Direct file downloads (uses third-party services)  
❌ Server-side processing (fully client-side)  
❌ File storage (no uploads, no storage)  

## 🎯 Perfect For:

- Personal video backup
- Offline viewing
- Content creators downloading their own videos
- Educational purposes
- Learning web development

## 🛠️ Browser Support

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers (iOS/Android)
- ✅ Opera, Brave, etc.

## 📝 FAQ

**Q: Do I need a server or backend?**  
A: No! This works entirely in the browser using GitHub Pages.

**Q: Is it really free?**  
A: Yes, completely free. GitHub Pages is free for public repositories.

**Q: Can I use this commercially?**  
A: Yes, MIT license allows commercial use. But respect copyright laws!

**Q: Why does it redirect to other sites?**  
A: Direct YouTube downloading requires server-side processing. This solution provides instant access to reliable services without needing your own server.

**Q: Can I add more download services?**  
A: Yes! Edit the `services` array in the JavaScript section to add more.

**Q: Does it work with private videos?**  
A: No, only public YouTube videos.

## 🤝 Contributing

Want to improve VidExtract? Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 💡 Ideas for Enhancement

- Add playlist support
- Include video preview thumbnails
- Add audio-only download options
- Implement download history
- Add dark/light theme toggle
- Support for other video platforms

## 📄 License

MIT License - Feel free to use, modify, and distribute!

## 🙏 Credits

- **Design Inspiration**: Cyberpunk 2077, Tron Legacy
- **Fonts**: Google Fonts (Orbitron, Rajdhani)
- **Icons**: Unicode emoji
- **YouTube API**: oEmbed endpoint

## 📞 Support

Having issues? Here's how to get help:

1. Check if your YouTube URL is correct
2. Try a different video
3. Make sure the video is public
4. Clear browser cache
5. Try a different browser
6. Open an issue on GitHub

## 🎉 Success Stories

After deploying, share your link! Tag it with:
- `#VidExtract`
- `#YouTubeDownloader`
- `#GitHubPages`

---

**Made with ⚡ and 💙 | VidExtract © 2026**

*Remember: Always respect content creators and copyright laws!*
