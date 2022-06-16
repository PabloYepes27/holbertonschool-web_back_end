#!/usr/bin/env python3
"""
Main file
"""

get_db = __import__('filtered_logger').get_db
hash_password = __import__('encrypt_password').hash_password

db = get_db()
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM users;")
for row in cursor:
    print(row[0])
cursor.close()
db.close()
password = "MyAmazingPassw0rd"
print(hash_password(password))
print(hash_password(password))
