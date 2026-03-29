import sqlite3

def connect_db():
    conn = sqlite3.connect("library.db")
    curr = conn.cursor()
    curr.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            status TEXT DEFAULT 'Available'
        )
    """)
    conn.commit()
    conn.close()

def add_book(title, author):
    conn = sqlite3.connect("library.db")
    curr = conn.cursor()
    curr.execute("INSERT INTO Books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()

def get_books(search_query=None):
    conn = sqlite3.connect("library.db")
    curr = conn.cursor()
    if search_query:
        curr.execute("SELECT * FROM Books WHERE title LIKE ? OR author LIKE ?", 
                     ('%'+search_query+'%', '%'+search_query+'%'))
    else:
        curr.execute("SELECT * FROM Books")
    rows = curr.fetchall()
    conn.close()
    return rows

def delete_book(book_id):
    conn = sqlite3.connect("library.db")
    curr = conn.cursor()
    curr.execute("DELETE FROM Books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

def reset_db():
    conn = sqlite3.connect("library.db")
    curr = conn.cursor()
    curr.execute("DELETE FROM Books") # Clear the table
    curr.execute("DELETE FROM sqlite_sequence WHERE name='Books'") # Reset the ID counter
    conn.commit()
    conn.close()