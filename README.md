* Mini URL Shortener

A lightweight command-line URL Shortener built using Python 3 and the Python standard library.

The application converts long URLs into short, unique codes, stores the mappings persistently using JSON, and allows users to resolve short codes back to their original URLs.

It also includes custom aliases, click tracking, URL validation, and automatic browser opening as additional features.

---

* Features

Required Features

-  Shorten long URLs into unique 6-character codes
-  Resolve short codes to their original URLs
-  Persistent data storage using JSON
-  List all shortened URLs
-  Handle invalid URLs gracefully
-  Handle duplicate URLs
-  Handle missing/invalid short codes
-  Uses only Python's standard library

Bonus Features

-  Custom alias support
-  Track the number of times a URL is resolved
-  Automatically open the original URL in the default browser
-  Interactive help command
-  Clean command-line interface

---

* Technologies Used

- Python 3
- JSON – persistent data storage
- urllib.parse – URL validation
- random – short-code generation
- string – character generation
- webbrowser – opening resolved URLs

No external libraries or URL-shortening APIs are used.

---

📁 Project Structure

Mini-Url-Shortener
│
├── main.py
├── README.md
└── .gitignore

"main.py"

Contains the complete URL-shortener application and command-line interface.

"README.md"

Project documentation and usage instructions.

".gitignore"

Contains files and folders that should not be uploaded to GitHub.

---

Version used:

- Python 3.x



How to Run:

1. Clone the repository

git clone https://github.com/Anujsharma2601/Mini-Url-Shortener.git

2. Open the project directory

cd Mini-Url-Shortener

3. Run the program

python main.py

If your system uses "python3":

python3 main.py

---

Available Commands

1. Shorten a URL

shorten (url)

Example:

> shorten https://www.google.com

Output:

URL shortened successfully!
Short code: aB7xK2

---

2. Resolve a Short Code

resolve (code)

Example:

> resolve aB7xK2

Output:

Original URL: https://www.google.com
Total resolutions: 1
Opening URL in browser...

The original URL will also be opened in the system's default web browser.

Each successful resolution increases the resolution/click counter.

---

3. List All Stored URLs

list

Example:

> list

Output:

=================================================================
                    STORED URLS
=================================================================
Code   : aB7xK2
URL    : https://www.google.com
Clicks : 2
-----------------------------------------------------------------
Code   : github
URL    : https://github.com
Clicks : 1
-----------------------------------------------------------------

---

4. Create a Custom Alias

A custom alias can be created using:

shorten <url> --alias <alias>

Example:

> shorten https://github.com --alias github

Output:

URL shortened successfully!
Short code: github

The custom alias can then be resolved normally:

> resolve github

---

5. Display Help

help

Displays all available commands and examples.

---

6. Exit the Program

exit

or:

quit

---

* Data Persistence

The application stores URL mappings in a file called:

urls.json

This file is automatically created when the first URL is shortened.

Example:

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

Because the data is stored in a JSON file, the mappings remain available even after the program is closed and restarted.

---

* Error Handling

The program handles common errors such as:

Invalid URL

> shorten hello
Error: Invalid URL.

Duplicate URL

> shorten https://www.google.com
This URL has already been shortened.
Short code: aB7xK2

Missing Short Code

> resolve xyz999
Error: Short code not found.

Duplicate Alias

> shorten https://example.com --alias github
Error: This alias is already in use.

Invalid Alias

> shorten https://example.com --alias my-alias
Error: Alias must contain only letters and numbers.

---

* How It Works

The basic workflow is:

                    Long URL
                       │
                       ▼
                URL Validation
                       │
                       ▼
              Generate Short Code
                       │
                       ▼
                Store in JSON
                       │
                       ▼
                 Short Code
                       │
                       ▼
              User enters code
                       │
                       ▼
               Find original URL
                       │
                       ▼
                Open the URL

For example:

https://www.google.com
          ↓
       aB7xK2
          ↓
https://www.google.com

---

* Short Code Generation

When no custom alias is provided, the program generates a random 6-character code using:

- Uppercase letters
- Lowercase letters
- Numbers

For example:

aB7xK2
P91mQa
x7L2Bc

The program checks the existing stored codes to ensure that the generated code is unique.

---

* Click Tracking

Every time a short code is successfully resolved, its resolution count increases.

For example:

First resolution:
Clicks : 1

Second resolution:
Clicks : 2

Third resolution:
Clicks : 3

This information is also stored permanently in "urls.json".

---

* No External APIs

This project does not use services such as:

- Bitly
- TinyURL
- Any other external URL-shortening API

Everything is implemented locally using Python's standard library.

---

* Future Improvements

Some possible future improvements include:

- Delete shortened URLs
- Add URL expiration dates
- Add password-protected links
- Add statistics and usage analytics
- Store data using SQLite
- Create a graphical user interface
- Generate QR codes for shortened URLs
- Add an HTTP/web interface

---

* Author

Anuj Sharma

GitHub:
https://github.com/Anujsharma2601

---

* License

This project is created for educational and learning purposes.
