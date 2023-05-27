from flask import Flask, request
import html
import psycopg2

app = Flask(__name__)

# Establish a connection to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="postgres",
    password="root"
)
cursor = conn.cursor()

@app.route('/')
def index():
    name = request.args.get('name', '')

    # Sanitize user input
    sanitized_name = html.escape(name)

    # Vulnerable SQL query with potential injection
    query = "SELECT * FROM users WHERE username = '{}'".format(sanitized_name)

    # Execute the query
    cursor.execute(query)
    results = cursor.fetchall()

    return '<h1>Hello, This is a test web app {}!</h1>{}'.format(sanitized_name, name)

if __name__ == '__main__':
    app.run()

# Close the cursor and connection
cursor.close()
conn.close()
