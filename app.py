import os
import json
import string
import random
from urllib.parse import urlparse
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, abort

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
DATA_FILE = 'urls.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme in ['http', 'https'], result.netloc])
    except ValueError:
        return False

@app.route('/')
def index():
    urls = load_data()
    return render_template('index.html', urls=urls)

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('url', '').strip()
    alias = request.form.get('alias', '').strip()

    if not long_url:
        flash('URL is required.', 'error')
        return redirect(url_for('index'))

    if not is_valid_url(long_url):
        flash('Invalid URL. Please enter a valid HTTP/HTTPS URL.', 'error')
        return redirect(url_for('index'))

    data = load_data()

    # Check for duplicate URL if no alias is provided
    if not alias:
        for code, info in data.items():
            if info['url'] == long_url:
                flash('URL already shortened!', 'success')
                return redirect(url_for('index'))
    
    if alias:
        if not alias.isalnum():
            flash('Alias must be alphanumeric.', 'error')
            return redirect(url_for('index'))
        if alias in data:
            flash('Alias is already taken. Please choose another one.', 'error')
            return redirect(url_for('index'))
        short_code = alias
    else:
        short_code = generate_short_code()
        while short_code in data:
            short_code = generate_short_code()

    data[short_code] = {'url': long_url, 'clicks': 0}
    save_data(data)
    
    flash('URL successfully shortened!', 'success')
    return redirect(url_for('index'))

@app.route('/<code>')
def redirect_to_url(code):
    data = load_data()
    if code in data:
        data[code]['clicks'] += 1
        save_data(data)
        return redirect(data[code]['url'])
    abort(404)

@app.route('/delete/<code>', methods=['POST'])
def delete_url(code):
    data = load_data()
    if code in data:
        del data[code]
        save_data(data)
        flash('URL deleted successfully.', 'success')
    else:
        flash('URL not found.', 'error')
    return redirect(url_for('index'))

@app.route('/api/urls')
def api_urls():
    return jsonify(load_data())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
