from flask import Flask, request
import html

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', '')
    sanitized_name = html.escape(name)  # Sanitize user input
    return '<h1>Hello, This is a test web app {}!</h1>{}'.format(sanitized_name, name)

if __name__ == '__main__':
    app.run()
#add this in the url:
# http://localhost:5000/?name=<script>alert('This is a malicious script!')</script>
