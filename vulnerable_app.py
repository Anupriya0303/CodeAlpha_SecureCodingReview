import os
import sqlite3
import pickle
import hashlib

# Vulnerability 1: Hardcoded password
password = "admin123"
secret_key = "mysecretkey123"

# Vulnerability 2: SQL Injection
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

# Vulnerability 3: OS command injection
def ping_host(host):
    os.system("ping " + host)

# Vulnerability 4: Weak hashing (MD5)
def hash_password(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()

# Vulnerability 5: Insecure deserialization
def load_data(data):
    return pickle.loads(data)

print("Application Running...")
print(hash_password("mypassword"))