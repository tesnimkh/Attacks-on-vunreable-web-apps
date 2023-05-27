import psycopg2

# Establish a connection to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="postgres",
    password="root"
)
cursor = conn.cursor()

# Create the users table
create_table_query = '''CREATE TABLE users
                        (id SERIAL PRIMARY KEY,
                         username TEXT,
                         password TEXT)'''
cursor.execute(create_table_query)
conn.commit()

# Insert some sample data into the table
insert_query = '''INSERT INTO users (username, password)
                  VALUES (%s, %s)'''
sample_data = [('admin', 'password123'),
               ('user1', 'pass123'),
               ('user2', 'abc456')]
cursor.executemany(insert_query, sample_data)
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Database created successfully.")
