import json
import random
import string
import webbrowser
from urllib.parse import urlparse

DATA_FILE = "urls.json"


# -------------------- File Handling --------------------

def load_data():
    """Load saved URL data from the JSON file."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_data(data):
    """Save URL data to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# -------------------- URL Validation --------------------

def is_valid_url(url):
    """Check whether the URL has a valid HTTP/HTTPS format."""
    try:
        parsed = urlparse(url)

        return (
            parsed.scheme in ("http", "https")
            and bool(parsed.netloc)
        )

    except Exception:
        return False


# -------------------- Short Code Generation --------------------

def generate_code(data):
    """Generate a unique 6-character short code."""
    characters = string.ascii_letters + string.digits

    while True:
        code = "".join(random.choices(characters, k=6))

        if code not in data:
            return code


# -------------------- Shorten URL --------------------

def shorten_url(url, alias=None):
    """Create a short code for a URL."""

    if not is_valid_url(url):
        print("Error: Invalid URL.")
        return

    data = load_data()

    # Check if the URL already exists
    for code, details in data.items():
        if details["url"] == url:
            print("This URL has already been shortened.")
            print(f"Short code: {code}")
            return

    # Handle custom alias
    if alias:

        if not alias.isalnum():
            print("Error: Alias must contain only letters and numbers.")
            return

        if alias in data:
            print("Error: This alias is already in use.")
            return

        code = alias

    else:
        code = generate_code(data)

    # Store URL information
    data[code] = {
        "url": url,
        "clicks": 0
    }

    save_data(data)

    print("\nURL shortened successfully!")
    print(f"Short code: {code}")


# -------------------- Resolve URL --------------------

def resolve_url(code):
    """Find and open the original URL."""

    data = load_data()

    if code not in data:
        print("Error: Short code not found.")
        return

    url = data[code]["url"]

    # Increase click count
    data[code]["clicks"] += 1

    save_data(data)

    print(f"\nOriginal URL: {url}")
    print(f"Total resolutions: {data[code]['clicks']}")

    # Open URL in default browser
    print("Opening URL in browser...")
    webbrowser.open(url)


# -------------------- List URLs --------------------

def list_urls():
    """Display all stored URL mappings."""

    data = load_data()

    if not data:
        print("\nNo shortened URLs found.")
        return

    print("\n" + "=" * 65)
    print("                    STORED URLS")
    print("=" * 65)

    for code, details in data.items():
        print(f"Code   : {code}")
        print(f"URL    : {details['url']}")
        print(f"Clicks : {details['clicks']}")
        print("-" * 65)


# -------------------- Help --------------------

def show_help():
    """Display available commands."""

    print("""
============================================================
                    MINI URL SHORTENER
============================================================

Commands:

  shorten <url>
      Shorten a URL using a randomly generated code.

  shorten <url> --alias <alias>
      Shorten a URL using a custom alias.

  resolve <code>
      Find and open the original URL.

  list
      Display all stored URL mappings and click counts.

  help
      Display this help message.

  exit
      Exit the program.

Examples:

  shorten https://www.google.com

  shorten https://github.com --alias github

  resolve github

  list

============================================================
""")


# -------------------- Command Processing --------------------

def process_command(command):
    """Process a single user command."""

    parts = command.split()

    if not parts:
        return True

    command_name = parts[0].lower()

    # ----- Shorten -----
    if command_name == "shorten":

        if len(parts) < 2:
            print("Usage: shorten <url>")
            return True

        url = parts[1]
        alias = None

        if "--alias" in parts:
            alias_index = parts.index("--alias")

            if alias_index + 1 >= len(parts):
                print("Usage: shorten <url> --alias <alias>")
                return True

            alias = parts[alias_index + 1]

        shorten_url(url, alias)

    # ----- Resolve -----
    elif command_name == "resolve":

        if len(parts) != 2:
            print("Usage: resolve <code>")
            return True

        resolve_url(parts[1])

    # ----- List -----
    elif command_name == "list":

        if len(parts) != 1:
            print("Usage: list")
            return True

        list_urls()

    # ----- Help -----
    elif command_name == "help":

        show_help()

    # ----- Exit -----
    elif command_name in ("exit", "quit"):

        print("\nThank you for using Mini URL Shortener!")
        return False

    # ----- Unknown command -----
    else:

        print(
            "Unknown command. "
            "Type 'help' to see available commands."
        )

    return True


# -------------------- Main Program --------------------

def main():

    print("=" * 60)
    print("              MINI URL SHORTENER")
    print("=" * 60)
    print("Type 'help' to see available commands.")
    print("Type 'exit' to close the program.")

    while True:

        try:
            command = input("\n> ").strip()

            if not process_command(command):
                break

        except KeyboardInterrupt:
            print("\n\nProgram interrupted.")
            print("Goodbye!")
            break

        except EOFError:
            print("\n\nGoodbye!")
            break


# -------------------- Program Entry Point --------------------

if __name__ == "__main__":
    main()