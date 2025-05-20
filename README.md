# 🏫 Student Class Manager

A simple command-line student management system written in Python. This project allows users to manage students by classroom. Users can add, remove, search, and view students in each class. All data is stored persistently in text files for each class.

---

## 📁 Project Structure


---

## ✅ Features

- Add a student to a specific class
- Remove a student from a class
- Search for a student by name
- View all students in a class
- Data saved persistently in `.txt` files

---

## 🧱 Classes Overview

**studentclass.py** contains:

- `Student`: The base class with core methods:
  - `add()`: Adds a student to the class file
  - `remove()`: Removes a student by name
  - `exist()`: Searches for a student by name
  - `see()`: Displays all students in the class

- Subclasses:
  - `Student1_1`
  - `Student1_2`
  - `Student1_3`
  - `Student1_4`

Each subclass represents a specific class level and inherits from `Student`.

---

## 🖥️ How to Use

1. Make sure Python 3 is installed on your system.
2. Download or clone the project directory `StudentManagerClass`.
3. Navigate to the folder in your terminal or command prompt.
4. Run the main program:

```bash
python studentUI.py
