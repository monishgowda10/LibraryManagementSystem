import tkinter as tk
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.configure(bg="purple")  # Set background color

        # Books data
        self.books = [
            {"title": "The Maze Runner", "author": "Monish", "isbn": "12345", "available": True},
            {"title": "To Kill Girls", "author": "Varun", "isbn": "1234", "available": True},
            {"title": "1984", "author": "George", "isbn": "123", "available": True}
        ]

        # Main window widgets
        self.title_label = tk.Label(master, text="Library Management System", font=('Helvetica', 18, 'bold'), fg="black", bg="orange")
        self.title_label.pack(pady=10)

        # Title Entry
        self.title_heading = tk.Label(master, font=('Helvetica', 10, 'bold'),text="Title:",fg="black", bg="light blue")
        self.title_heading.pack()
        self.title_entry = tk.Entry(master)
        self.title_entry.pack(pady=5)

        # Author Entry
        self.author_heading = tk.Label(master, font=('Helvetica', 10, 'bold'),text="Author:",fg="black", bg="light blue")
        self.author_heading.pack()
        self.author_entry = tk.Entry(master)
        self.author_entry.pack(pady=5)

        # ISBN Entry
        self.isbn_heading = tk.Label(master,font=('Helvetica', 10, 'bold'), text="ISBN:",fg="black", bg="light blue")
        self.isbn_heading.pack()
        self.isbn_entry = tk.Entry(master)
        self.isbn_entry.pack(pady=5)

        # Buttons
        self.add_book_button = tk.Button(master, text="Add Book", command=self.add_book)
        self.add_book_button.pack(pady=5)

        self.lend_book_button = tk.Button(master, text="Lend Book", command=self.lend_book)
        self.lend_book_button.pack(pady=5)

        self.return_book_button = tk.Button(master, text="Return Book", command=self.return_book)
        self.return_book_button.pack(pady=5)

        self.display_books_button = tk.Button(master, text="Display Books", command=self.display_books)
        self.display_books_button.pack(pady=5)

        self.search_book_button = tk.Button(master, text="Search Book", command=self.search_book)
        self.search_book_button.pack(pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=5)

    def add_book(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        isbn = self.isbn_entry.get().strip()
        if title and author and isbn:
            book = {"title": title, "author": author, "isbn": isbn, "available": True}
            self.books.append(book)
            messagebox.showinfo("Success", "Book added successfully.")
            # Clear entry fields after adding book
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
            self.isbn_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter valid input.")

    def lend_book(self):
        title = self.title_entry.get().strip()
        if title:
            for book in self.books:
                if book["title"] == title and book["available"]:
                    book["available"] = False
                    messagebox.showinfo("Success", f"{title} has been lent.")
                    return
            messagebox.showerror("Error", "Book not available or already lent.")
        else:
            messagebox.showerror("Error", "Please enter valid input.")

    def return_book(self):
        title = self.title_entry.get().strip()
        if title:
            for book in self.books:
                if book["title"] == title and not book["available"]:
                    book["available"] = True
                    messagebox.showinfo("Success", f"{title} has been returned.")
                    return
            messagebox.showerror("Error", "Book not found or already returned.")
        else:
            messagebox.showerror("Error", "Please enter valid input.")

    def display_books(self):
        if self.books:
            book_list = "\n".join([f"{book['title']} by {book['author']} (ISBN: {book['isbn']})" for book in self.books])
            messagebox.showinfo("Available Books", book_list)
        else:
            messagebox.showinfo("Available Books", "No books available in the library.")

    def search_book(self):
        search_query = self.title_entry.get().strip()
        if search_query:
            if search_query.isdigit():  # Check if the search query is a numeric string (ISBN)
                found_books = [book for book in self.books if search_query == book['isbn']]
                if found_books:
                    book_info = ""
                    for book in found_books:
                        book_info += f"Title: {book['title']}\n"
                        book_info += f"Author: {book['author']}\n"
                        book_info += f"ISBN: {book['isbn']}\n"
                        book_info += f"Status: {'Available' if book['available'] else 'Not available'}\n\n"
                    messagebox.showinfo("Search Results", book_info)
                else:
                    messagebox.showinfo("Search Results", "No books found matching the ISBN.")
            else:
                found_books = [book for book in self.books if search_query.lower() in book['title'].lower() 
                                                            or search_query.lower() in book['author'].lower()]
                if found_books:
                    book_list = "\n".join([f"{book['title']} by {book['author']}" for book in found_books])
                    messagebox.showinfo("Search Results", f"Found books:\n{book_list}\nTotal found: {len(found_books)}")
                else:
                    messagebox.showinfo("Search Results", "No books found matching the search query.")
        else:
            messagebox.showerror("Error", "Please enter a valid search query.")

def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    if username == "Monish" and password == "1016":
        login_window.destroy()
        root = tk.Tk()
        app = LibraryManagementSystem(root)
        root.mainloop()
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Login window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x150")
login_window.configure(bg="indigo")  # Set background color

username_label = tk.Label(login_window, text="Username:", bg="white",font=('Helvetica', 10, 'bold'))
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password:", bg="white",font=('Helvetica', 10, 'bold'))
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack()

login_window.mainloop()
