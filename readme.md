# ✂️ Mini URL Shortener 🔗

A lightweight URL Shortener built with **Python** and **Flask**. Available as both a **command-line tool** and a **web application**.

The application converts long URLs into short, unique codes, stores the mappings persistently using JSON, and allows users to resolve short codes back to their original URLs.

---

## ✨ Features

### Core Features

- 🔗 Shorten long URLs into unique 6-character codes
- 🔄 Resolve short codes to their original URLs (with automatic redirect)
- 💾 Persistent data storage using JSON
- 📋 List all shortened URLs with click statistics
- ✅ Handle invalid URLs gracefully
- 🔁 Handle duplicate URLs
- ❌ Handle missing/invalid short codes

### Bonus Features

- 🏷️ Custom alias support (`--alias` in CLI, optional field in web UI)
- 📊 Track the number of times a URL is resolved (click counter)
- 📋 Copy shortened URL to clipboard (web UI)
- 🗑️ Delete shortened URLs (web UI)
- 🌐 Automatic redirect when visiting a short URL
- 🎨 Modern, responsive web interface with gradient design
- 💻 Interactive CLI with help command
- 🚀 Deployable to cloud platforms (Render, Heroku, Railway)

---

## 🛠️ Technologies Used

| Technology       | Purpose                          |
| ---------------- | -------------------------------- |
| Python 3         | Core language                    |
| Flask            | Web framework                    |
| Gunicorn         | Production WSGI server           |
| JSON             | Persistent data storage          |
| HTML/CSS         | Frontend (inline, no frameworks) |
| JavaScript       | Copy-to-clipboard functionality  |
| urllib.parse      | URL validation                   |

No external URL-shortening APIs are used. Everything runs locally.

---

## 📁 Project Structure

```
Mini-URL-Shortener/
├── app.py              # Flask web application
├── main.py             # Original CLI application
├── templates/
│   └── index.html      # Web UI template
├── urls.json           # Auto-generated data store
├── requirements.txt    # Python dependencies
├── Procfile            # Deployment (Gunicorn)
├── render.yaml         # Render deployment blueprint
├── readme.md           # Project documentation
└── .gitignore          # Git ignore rules
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Anujsharma2601/Mini-Url-Shortener.git
   cd Mini-Url-Shortener
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🌐 Running the Web Application

```bash
python app.py
```

Open your browser and go to: **http://localhost:5000**

You'll see a clean, modern interface where you can:
- Paste a long URL and get a short link instantly
- Set a custom alias (optional)
- View all your shortened URLs with click counts
- Copy short URLs to clipboard
- Delete URLs you no longer need
- Click any short URL to be redirected to the original

---

## 💻 Running the CLI Application

```bash
python main.py
```

### CLI Commands

| Command                                | Description                              |
| -------------------------------------- | ---------------------------------------- |
| `shorten <url>`                        | Shorten a URL with a random code         |
| `shorten <url> --alias <alias>`        | Shorten a URL with a custom alias        |
| `resolve <code>`                       | Open the original URL in your browser    |
| `list`                                 | Display all stored URLs and click counts |
| `help`                                 | Show available commands                  |
| `exit`                                 | Exit the program                         |

### CLI Examples

```
> shorten https://www.google.com
URL shortened successfully!
Short code: aB7xK2

> shorten https://github.com --alias github
URL shortened successfully!
Short code: github

> resolve github
Original URL: https://github.com
Total resolutions: 1
Opening URL in browser...

> list
=================================================================
                    STORED URLS
=================================================================
Code   : aB7xK2
URL    : https://www.google.com
Clicks : 2
-----------------------------------------------------------------
```

---

## 🌍 Deploying to the Web (Render)

Deploy your URL shortener to the internet for free using [Render](https://render.com):

### Option 1: One-Click Deploy

1. Push your code to a GitHub repository
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click **New → Web Service**
4. Connect your GitHub repo
5. Render will auto-detect the `render.yaml` blueprint
6. Click **Deploy** — your app will be live in minutes!

### Option 2: Manual Setup on Render

1. Create a new **Web Service** on Render
2. Connect your GitHub repository
3. Set the following:
   - **Runtime**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. Add environment variable: `SECRET_KEY` → generate a random string
5. Deploy!

Your app will be available at: `https://your-app-name.onrender.com`

---

## 📊 API Endpoint

The app also exposes a JSON API:

```
GET /api/urls
```

Returns all shortened URLs and their metadata:

```json
{
    "aB7xK2": {
        "url": "https://www.google.com",
        "clicks": 2
    },
    "github": {
        "url": "https://github.com",
        "clicks": 1
    }
}
```

---

## 💾 Data Persistence

URL mappings are stored in `urls.json`, which is auto-created on first use:

```json
{
    "aB7xK2": {
        "url": "https://www.google.com",
        "clicks": 2
    },
    "github": {
        "url": "https://github.com",
        "clicks": 1
    }
}
```

> **Note**: On cloud platforms like Render (free tier), the JSON file resets on redeploy. For production use, consider upgrading to a database like SQLite or PostgreSQL.

---

## 🔒 Error Handling

| Scenario                | Response                                           |
| ----------------------- | -------------------------------------------------- |
| Invalid URL             | `Invalid URL. Please enter a valid HTTP/HTTPS URL` |
| Duplicate URL           | `URL already shortened!`                           |
| Short code not found    | 404 page / error message                           |
| Duplicate alias         | `Alias is already taken`                           |
| Non-alphanumeric alias  | `Alias must be alphanumeric`                       |

---

## 🔮 Future Improvements

- [ ] URL expiration dates
- [ ] Password-protected links
- [ ] Usage analytics dashboard
- [ ] SQLite/PostgreSQL database
- [ ] QR code generation
- [ ] User authentication
- [ ] Rate limiting

---

## 👤 Author

**Anuj Sharma**

- GitHub: [Anujsharma2601](https://github.com/Anujsharma2601)

---

## 📄 License

This project is created for educational and learning purposes.