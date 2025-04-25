import sqlite3
from PyQt5 import QtWidgets, uic

# Define connection and cursor
connection = sqlite3.connect("apprenticeship_system.db")
cursor = connection.cursor()

# Create students table
student_table = """
CREATE TABLE IF NOT EXISTS students (
    student_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    mobile_number TEXT NOT NULL,
    email TEXT NOT NULL,
    gpa REAL NOT NULL CHECK(gpa BETWEEN 0 AND 5), 
    specialization TEXT NOT NULL, 
    preferred_locations TEXT NOT NULL,
    skills TEXT NOT NULL
)
"""
cursor.execute(student_table)

# Create openings table
opnening_table = """
CREATE TABLE IF NOT EXISTS openings (
    opening_id INTEGER PRIMARY KEY AUTOINCREMENT,
    specialization TEXT NOT NULL, 
    location TEXT NOT NULL, 
    stipend REAL NOT NULL CHECK(stipend > 0),
    required_skills TEXT NOT NULL
)
"""
cursor.execute(opnening_table)

# Commit changes and close connection
connection.commit()
connection.close()


