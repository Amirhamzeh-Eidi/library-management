# Library Management System

This project is for learning purposes.

A simple CLI-based library manager written in Python.
You can manage books, members, and borrowing operations directly from the terminal.

## Features
- Add / edit / delete books
- Add / edit / delete members
- Borrow and return books
- Search books and members
- JSON data storage
- History logging
- Reports generation

## Installation
```bash
git clone <https://github.com/Amirhamzeh-Eidi/library-management.git>
cd library-management
python main.py
```

# Project Structure
- main.py → CLI interface
- library.py → business logic
- modules.py → Book & Member models
- storage.py → JSON save/load
- logger.py → history logs
- data/ → stored files (auto generated)
# Requirements
- Python 3.10+