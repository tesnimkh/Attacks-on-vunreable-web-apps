from flask import Flask, request
import html

app = Flask(__name__)

ALLOWED_FILES = ['file1.txt', 'file2.txt', 'file3.txt']
FILE_PATH = '/path/to/files/'

@app.route('/')
def index():
    name = request.args.get('name', '')
    sanitized_name = html.escape(name)  # Sanitize user input

    # Validate file name against the whitelist
    if name not in ALLOWED_FILES:
        return '<h1>Invalid file name</h1>'

    # Construct the file path
    file_path = FILE_PATH + name

    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return '<h1>Hello, This is a test web app {}!</h1>{}'.format(sanitized_name, content)
    except FileNotFoundError:
        return '<h1>File not found</h1>'

if __name__ == '__main__':
    app.run()
