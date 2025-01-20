# work with SQLite3 in python

import sqlite3

DB_NAME = "sqlite_db.db"

# Read values from the table
with sqlite3.connect(DB_NAME) as sqlite_conn:
     sql_request = "SELECT * FROM courses WHERE reviews_qty>=20"
     sql_cursor = sqlite_conn.execute(sql_request)
     for record in sql_cursor:
         print(record)


# Create new table (step#1)
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     print(sqlite_conn)
#     print(sqlite3.version_info)

# Addin one record in to the table
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     sqlite_conn.execute(sql_request, (251, "Python Course", 100, 30))
#     sqlite_conn.commit() 

# # Create new table (with -> to auto close the connection)    
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#     );"""
#     sqlite_conn.execute(sql_request)



# Adding values in cycle for in
# courses = [
#     (2513, "Python Course", 100, 30),
#     (2344, "Python Course", 100, 30),
#     (2532, "Python Course", 100, 30),
#     (25111, "Python Course", 100, 30)
# ]

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit() 

