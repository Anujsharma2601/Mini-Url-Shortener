#  Mini URL Shortener 🔗

A lightweight URL Shortener built with **Python** and **Flask**. 

The application converts long URLs into short, unique codes, stores the mappings persistently using JSON, and allows users to resolve short codes back to their original URLs.

---

##  Features

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
| urllib.parse     | URL validation                   |

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

##  Running the Web Application

Open your browser and go to: **https://mini-url-shortener-1.onrender.com/**

You'll see a clean, modern interface where you can:
- Paste a long URL and get a short link instantly
- Set a custom alias (optional)
- View all your shortened URLs with click counts
- Copy short URLs to clipboard
- Delete URLs you no longer need
- Click any short URL to be redirected to the original

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
