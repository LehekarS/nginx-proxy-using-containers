from flask import Flask, send_from_directory, request
import requests

app = Flask(__name__)

# Serve index.html directly
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Serve CSS directly
@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

# Simple reverse proxy route
@app.route('/proxy/<path:url>')
def proxy(url):
    target_url = f'http://example.com/{url}'  # Change this to your backend service
    response = requests.get(target_url)
    return response.content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

