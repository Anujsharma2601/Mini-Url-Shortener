Mini URL Shortener

A simple command-line URL shortener built using Python 3 and only the Python standard library.

It converts long URLs into short codes, stores the mappings persistently, and allows users to resolve short codes back to their original URLs.

Features

- Shorten long URLs into random 6-character codes
- Resolve short codes to their original URLs
- Persistent storage using JSON
- List all shortened URLs
- Validate URLs
- Handle duplicate URLs
- Handle invalid or missing short codes
- Custom alias support
- Track the number of times a URL is resolved
- No external APIs or libraries required

Requirements

- Python 3.x
- No external Python packages are required.

Project Structure

mini-url-shortener/
│
├── main.py
├── urls.json
├── README.md
└── .gitignore

"urls.json" is automatically created when the first URL is shortened.

How to Run

Clone the repository:

git clone <YOUR-GITHUB-REPOSITORY-URL>

Move into the project directory:

cd mini-url-shortener

Run the program:

python main.py

On some systems you may need:

python3 main.py

Available Commands

1. Shorten a URL

shorten <url>

Example:

> shorten https://www.google.com
Short URL code: aB7xK2

2. Resolve a short code

resolve <code>

Example:

> resolve aB7xK2
Original URL: https://www.google.com
Total resolutions: 1

Every successful resolution increases the click/resolution counter.

3. List all URLs

list

Example:

> list

Shortened URLs
------------------------------------------------------------
Code   : aB7xK2
URL    : https://www.google.com
Clicks : 1
------------------------------------------------------------

4. Custom Alias

A custom alias can be specified using:

shorten <url> --alias <alias>

Example:

> shorten https://github.com --alias github
Short URL code: github

The alias can then be resolved:

> resolve github
Original URL: https://github.com
Total resolutions: 1

5. Help

help

Displays the available commands.

6. Exit

exit

Closes the program.

Data Persistence

The URL mappings are stored in "urls.json".

Example:

{
    "aB7xK2": {
        "url": "https://www.google.com",
        "clicks": 3
    },
    "github": {
        "url": "https://github.com",
        "clicks": 1
    }
}

Because the data is stored in a file, the mappings remain available even after the program is closed and restarted.

Error Handling

The program handles several common errors:

- Invalid URLs
- Duplicate URLs
- Duplicate custom aliases
- Missing short codes
- Invalid aliases
- Incorrect command syntax
- Empty URL database

Example:

> resolve xyz999
Error: Short code not found.

Technologies Used

- Python 3
- JSON
- "urllib.parse"
- "random"
- "string"

Only Python's standard library is used.

Future Improvements

Possible future improvements include:

- Opening resolved URLs automatically in the browser
- URL deletion
- Expiring links
- Statistics such as total links and most-used links
- A graphical user interface
- QR code generation
- SQLite database storage

Author

Anuj Sharma

Mini URL Shortener — Python CLI Project
