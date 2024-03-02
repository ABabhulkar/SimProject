import json
import os
import sqlite3

# # Connect to the database
# conn = sqlite3.connect("testDb.db")
# cursor = conn.cursor()

# # Create the users table (if it doesn't exist)
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   data JSON
# );
# ''')

# # Sample user data
# user_data = {
#     "name": "John Doe",
#     "email": "johndoe@example.com",
#     "age": 30,
#     "isActive": True,
# }

# **Create (Insert)** a new user


# def create_user(data):
#     json_data = json.dumps(data)  # Convert data to JSON string
#     cursor.execute("INSERT INTO users (data) VALUES (?)", (json_data,))
#     conn.commit()
#     print(f"User created successfully! ID: {cursor.lastrowid}")

# # **Read (Select)** user information


# def get_user(user_id):
#     cursor.execute("SELECT data FROM users WHERE id = ?", (user_id,))
#     user_data = cursor.fetchone()
#     if user_data:
#         # Convert JSON string back to dictionary
#         return json.loads(user_data[0])
#     else:
#         print(f"User with ID {user_id} not found.")
#         return None

# # **Update (Modify)** user information

# # Retrieve and extract data
# # cursor.execute("SELECT json_extract(data, '$.name') FROM users")
# # name = cursor.fetchone()[0]  # Extracted name
# # print(name)  # Output: Alice

# # # Update JSON data
# # updated_data = {"name": "Bob", "age": 30}
# # json_data = json.dumps(updated_data)
# # cursor.execute("UPDATE users SET data = ? WHERE id = 1", (json_data,))
# # conn.commit()


# def update_user(user_id, data):
#     json_data = json.dumps(data)
#     cursor.execute("UPDATE users SET data = ? WHERE id = ?",
#                    (json_data, user_id))
#     conn.commit()
#     print(f"User with ID {user_id} updated successfully.")

# # **Delete (Remove)** a user


# def delete_user(user_id):
#     cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
#     conn.commit()
#     print(f"User with ID {user_id} deleted.")


# Example usage
# create_user(user_data)
# updated_data = {"age": 35, "isActive": False}
# update_user(1, updated_data)
# user = get_user(1)
# if user:
#     print(f"User name: {user['name']}")
# delete_user(1)

# # Close the connection
# conn.close()


class QueryManager:
    sql_dir = None
    sql_files = None

    def __init__(self, sql_dir):
        self.sql_dir = sql_dir
        # - Find all .sql files for the given directory and put them in a list
        self.sql_files = files = [
            f for f in os.listdir(self.sql_dir) if os.path.isfile(os.path.join(self.sql_dir, f)) and '.sql' in f
        ]

    def __getattr__(self, item):
        """
           Lets query file be fetched by calling the query manager class object with the name of the query as the attribute
        """

        if item + '.sql' in self.sql_files:
            # - This is where the file is actually read
            with open(os.path.join(self.sql_dir, item + '.sql'), 'r') as f:
                return f.read()
        else:
            raise AttributeError(
                f'QueryManager cannot find file {str(item)}.sql')


# sql_dir = os.path.join(os.path.dirname(__file__), 'sql_files')

# qm = QueryManager(sql_dir)
# select_query = qm.fetch_data
# insert_query = qm.insert_data
# update_query = qm.update_data
# delete_query = qm.delete_data
