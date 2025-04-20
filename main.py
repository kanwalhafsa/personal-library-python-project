

# import json

# class BookCollection:
#     """Handles all library operations including adding, removing, searching, and saving books."""

#     def __init__(self):
#         """Initialize a new book collection with an empty list and set up file storage."""
#         self.book_list = []
#         self.storage_file = "books_data.json"
#         self.read_from_file()  # Call the function, not assign to a variable

#     def read_from_file(self):
#         """Load saved books from a JSON file into memory."""
#         try:
#             with open(self.storage_file, "r") as file:
#                 self.book_list = json.load(file)
#         except (FileNotFoundError, json.JSONDecodeError):
#             self.book_list = []

#     def save_to_file(self):
#         """Store the current book collection to a JSON file."""
#         with open(self.storage_file, "w") as file:
#             json.dump(self.book_list, file, indent=4)

#     def create_new_book(self):
#         """Add a new book to the collection."""
#         book_title = input("Enter book title: ")
#         book_author = input("Enter author: ")
#         publication_year = input("Enter publication year: ")
#         book_genre = input("Enter genre: ")
#         is_book_read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

#         new_book = {
#             "title": book_title,
#             "author": book_author,
#             "publish": publication_year,
#             "genre": book_genre,
#             "read": is_book_read
#         }

#         self.book_list.append(new_book)
#         self.save_to_file()
#         print("Book added successfully!\n")

#     def delete_book(self):
#         """Remove a book from the collection."""
#         book_title = input("Enter the title of the book to remove: ")

#         for book in self.book_list:
#             if book["title"].lower() == book_title.lower():
#                 self.book_list.remove(book)
#                 self.save_to_file()
#                 print("Book removed successfully!\n")
#                 return

#         print("Book not found!\n")

#     def find_book(self):
#         """Search for books in the collection by title or author."""
#         search_text = input("Enter search term: ").lower()
#         found_books = [
#             book for book in self.book_list
#             if search_text in book["title"].lower() or search_text in book["author"].lower()
#         ]

#         if found_books:
#             print("Matching books:")
#             for index, book in enumerate(found_books, 1):
#                 reading_status = "Read" if book["read"] else "Unread"
#                 print(
#                     f"{index}. {book['title']} by {book['author']} ({book['publish']} - {book['genre']} - {reading_status})"
#                 )
#         else:
#             print("No matching books found.\n")

#     def update_book(self):
#         """Update book details."""
#         book_title = input("Enter the title of the book you want to edit: ")
#         for book in self.book_list:
#             if book["title"].lower() == book_title.lower():
#                 print("Leave blank to keep existing value.")
#                 book["title"] = input(f"New title ({book['title']}): ") or book["title"]
#                 book["author"] = input(f"New author ({book['author']}): ") or book["author"]
#                 book["publish"] = input(f"New year ({book['publish']}): ") or book["publish"]
#                 book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
#                 read_input = input("Have you read this book? (yes/no): ").strip().lower()
#                 book["read"] = True if read_input == "yes" else False
#                 self.save_to_file()
#                 print("Book updated successfully!\n")
#                 return

#         print("Book not found!\n")

#     def display_all_books(self):
#         """Show all books in the collection."""
#         if not self.book_list:
#             print("Your book collection is empty.\n")
#             return

#         print("Your Book Collection:")
#         for index, book in enumerate(self.book_list, 1):
#             reading_status = "Read" if book["read"] else "Unread"
#             print(
#                 f"{index}. {book['title']} by {book['author']} ({book['publish']}) - {book['genre']} - {reading_status}"
#             )
#         print()

#     def show_reading_progress(self):
#         """Show reading statistics."""
#         total_books = len(self.book_list)
#         completed_books = sum(1 for book in self.book_list if book["read"])
#         completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0
#         print(f"Total books in collection: {total_books}")
#         print(f"Reading progress: {completion_rate:.2f}%\n")

#     def start_application(self):
#         """Run the interactive application."""
#         while True:
#             print("\n📚 Welcome to Your Personal Library! 📚")
#             print("1. Add a new book")
#             print("2. Remove a book")
#             print("3. Search for a book")
#             print("4. Update book details")
#             print("5. Display all books")
#             print("6. View reading progress")
#             print("7. Exit")
#             user_choice = input("Please choose an option (1-7): ")

#             if user_choice == "1":
#                 self.create_new_book()
#             elif user_choice == "2":
#                 self.delete_book()
#             elif user_choice == "3":
#                 self.find_book()
#             elif user_choice == "4":
#                 self.update_book()
#             elif user_choice == "5":
#                 self.display_all_books()
#             elif user_choice == "6":
#                 self.show_reading_progress()
#             elif user_choice == "7":
#                 self.save_to_file()
#                 print("Thank you for using Book Collection Manager. Goodbye!")
#                 break
#             else:
#                 print("Invalid choice. Please try again!\n")

# if __name__ == "__main__":
#     book_manager = BookCollection()
#     book_manager.start_application()



# import json
# import streamlit as st

# class BookCollection:
#     def __init__(self):
#         self.book_list = []
#         self.storage_file = "books_data.json"
#         self.read_from_file()

#     def read_from_file(self):
#         try:
#             with open(self.storage_file, "r") as file:
#                 self.book_list = json.load(file)
#         except (FileNotFoundError, json.JSONDecodeError):
#             self.book_list = []

#     def save_to_file(self):
#         with open(self.storage_file, "w") as file:
#             json.dump(self.book_list, file, indent=4)

#     def create_new_book(self, title, author, year, genre, read):
#         new_book = {
#             "title": title,
#             "author": author,
#             "publish": year,
#             "genre": genre,
#             "read": read,
#         }
#         self.book_list.append(new_book)
#         self.save_to_file()

#     def delete_book(self, title):
#         for book in self.book_list:
#             if book["title"].lower() == title.lower():
#                 self.book_list.remove(book)
#                 self.save_to_file()
#                 return True
#         return False

#     def find_book(self, search_text):
#         search_text = search_text.lower()
#         return [
#             book for book in self.book_list
#             if search_text in book["title"].lower() or search_text in book["author"].lower()
#         ]

#     def update_book(self, old_title, title, author, year, genre, read):
#         for book in self.book_list:
#             if book["title"].lower() == old_title.lower():
#                 book["title"] = title or book["title"]
#                 book["author"] = author or book["author"]
#                 book["publish"] = year or book["publish"]
#                 book["genre"] = genre or book["genre"]
#                 book["read"] = read
#                 self.save_to_file()
#                 return True
#         return False

#     def display_all_books(self):
#         return self.book_list

#     def show_reading_progress(self):
#         total_books = len(self.book_list)
#         completed_books = sum(1 for book in self.book_list if book["read"])
#         completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0
#         return total_books, completion_rate


# book_manager = BookCollection()
# st.title("📚 My Personal Library")

# menu = st.sidebar.selectbox("Choose an option", [
#     "Add a New Book", "Remove a Book", "Search Book", "Update Book",
#     "Display All Books", "View Reading Progress"
# ])

# if menu == "Add a New Book":
#     st.subheader("Add a New Book")
#     title = st.text_input("Book Title")
#     author = st.text_input("Author")
#     year = st.text_input("Publication Year")
#     genre = st.text_input("Genre")
#     read = st.checkbox("Have you read this book?")
#     if st.button("Add Book"):
#         if title and author and year and genre:
#             book_manager.create_new_book(title, author, year, genre, read)
#             st.success("Book added successfully!")
#         else:
#             st.error("Please fill all fields!")

# elif menu == "Remove a Book":
#     st.subheader("Remove a Book")
#     title = st.text_input("Enter title to remove")
#     if st.button("Remove"):
#         if book_manager.delete_book(title):
#             st.success("Book removed successfully!")
#         else:
#             st.error("Book not found!")

# elif menu == "Search Book":
#     st.subheader("Search Books")
#     query = st.text_input("Enter title or author name to search")
#     if query:
#         results = book_manager.find_book(query)
#         if results:
#             for book in results:
#                 st.write(f"📖 **{book['title']}** by {book['author']} - {book['publish']} | {book['genre']} | {'Read' if book['read'] else 'Unread'}")
#         else:
#             st.warning("No matching books found.")

# elif menu == "Update Book":
#     st.subheader("Update Book")
#     old_title = st.text_input("Enter the title of the book to update")
#     new_title = st.text_input("New Title")
#     new_author = st.text_input("New Author")
#     new_year = st.text_input("New Year")
#     new_genre = st.text_input("New Genre")
#     read = st.checkbox("Mark as Read")
#     if st.button("Update Book"):
#         updated = book_manager.update_book(old_title, new_title, new_author, new_year, new_genre, read)
#         if updated:
#             st.success("Book updated successfully!")
#         else:
#             st.error("Book not found!")

# elif menu == "Display All Books":
#     st.subheader("Your Book Collection")
#     books = book_manager.display_all_books()
#     if books:
#         for i, book in enumerate(books, 1):
#             st.write(f"{i}. **{book['title']}** by {book['author']} ({book['publish']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
#     else:
#         st.info("No books in your collection.")

# elif menu == "View Reading Progress":
#     st.subheader("Reading Progress")
#     total, progress = book_manager.show_reading_progress()
#     st.write(f"Total books: {total}")
#     st.write(f"Completion: {progress:.2f}%")
#     st.progress(progress / 100)




# import json
# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import os

# class BookCollection:
#     def __init__(self):
#         self.book_list = []
#         self.storage_file = "books_data.json"
#         self.load_books()

#     def load_books(self):
#         try:
#             with open(self.storage_file, "r") as file:
#                 self.book_list = json.load(file)
#         except (FileNotFoundError, json.JSONDecodeError):
#             self.book_list = []

#     def save_books(self):
#         with open(self.storage_file, "w") as file:
#             json.dump(self.book_list, file, indent=4)

#     def add_book(self, title, author, year, genre, read, favorite, story=""):
#         new_book = {
#             "title": title,
#             "author": author,
#             "year": year,
#             "genre": genre,
#             "read": read,
#             "favorite": favorite,
#             "story": story  # Add the story field
#         }
#         self.book_list.append(new_book)
#         self.save_books()

#     def delete_book(self, title):
#         self.book_list = [book for book in self.book_list if book["title"] != title]
#         self.save_books()

#     def update_book(self, title, updated_book):
#         for i, book in enumerate(self.book_list):
#             if book["title"] == title:
#                 self.book_list[i] = updated_book
#                 self.save_books()
#                 break

#     def get_filtered_books(self, genre=None, read=None):
#         books = self.book_list
#         if genre:
#             books = [b for b in books if b["genre"] == genre]
#         if read is not None:
#             books = [b for b in books if b["read"] == read]
#         return books

#     def get_favorite_books(self):
#         return [b for b in self.book_list if b["favorite"]]

#     def export_to_pdf(self):
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_font("Arial", size=12)
#         pdf.cell(200, 10, txt="Book List", ln=True, align="C")
        
#         for book in self.book_list:
#             # Check if 'read' is None and assign a default value if necessary
#             read_status = 'Read' if book.get("read", False) else 'Unread'
            
#             # Prepare book details
#             details = f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}"
#             pdf.cell(200, 10, txt=details, ln=True)
        
#         pdf_path = "book_list.pdf"
#         pdf.output(pdf_path)
#         return pdf_path



#     def get_sorted_books(self, key):
#         return sorted(self.book_list, key=lambda x: x[key])

#     def get_reading_progress(self):
#         total = len(self.book_list)
#         read = sum(1 for b in self.book_list if b["read"])
#         return read, total


# book_manager = BookCollection()
# st.title("📚 Personal Library Manager")

# menu = st.sidebar.selectbox("Choose an action", ["Add Book", "View Books", "Filter Books", "Favorite Books", "Reading Progress", "Export PDF", "Sort Books", "Write Your Story"])

# if menu == "Add Book":
#     st.subheader("➕ Add a New Book")
#     title = st.text_input("Book Title")
#     author = st.text_input("Author")
#     year = st.text_input("Publication Year")
#     genre = st.text_input("Genre")
#     read = st.checkbox("Have you read this book?")
#     favorite = st.checkbox("Mark as favorite")
#     story = st.text_area("Write a story or review about this book (optional)")
#     if st.button("Add Book"):
#         book_manager.add_book(title, author, year, genre, read, favorite, story)
#         st.success("Book added successfully!")

# elif menu == "View Books":
#     st.subheader("📖 All Books")
#     for book in book_manager.book_list:
#         st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']}")
#         st.write(f"Status: {'Read' if book['read'] else 'Unread'}")
#         if book["story"]:
#             st.write(f"**Story/Review**: {book['story']}")
#         st.write("-----")

# elif menu == "Filter Books":
#     genre = st.text_input("Genre")
#     read_status = st.selectbox("Read Status", ["All", "Read", "Unread"])
#     read = None if read_status == "All" else (read_status == "Read")
#     books = book_manager.get_filtered_books(genre or None, read)
#     for book in books:
#         st.write(book)

# elif menu == "Favorite Books":
#     st.subheader("❤️ Favorite Books")
#     favorites = book_manager.get_favorite_books()
#     for book in favorites:
#         st.write(book)

# elif menu == "Reading Progress":
#     st.subheader("📈 Reading Progress")
#     read, total = book_manager.get_reading_progress()
#     st.write(f"You've read {read} out of {total} books.")
#     fig, ax = plt.subplots()
#     ax.pie([read, total - read], labels=["Read", "Unread"], autopct="%1.1f%%")
#     st.pyplot(fig)

# elif menu == "Export PDF":
#     st.subheader("📤 Export Book List to PDF")
#     if st.button("Generate PDF"):
#         path = book_manager.export_to_pdf()
#         with open(path, "rb") as f:
#             st.download_button("Download PDF", f, file_name="book_list.pdf")

# elif menu == "Sort Books":
#     st.subheader("🗃️ Sort Books")
#     sort_by = st.selectbox("Sort by", ["title", "author", "year"])
#     sorted_books = book_manager.get_sorted_books(sort_by)
#     for book in sorted_books:
#         st.write(book)

# elif menu == "Write Your Story":
#     st.subheader("📝 Your Book Corner")
#     story = st.text_area("Write your story or review")
#     if st.button("Save Story"):
#         with open("my_stories.txt", "a") as f:
#             f.write(story + "\n\n")
#         st.success("Story saved!")




import json
import streamlit as st
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

class BookCollection:
    def __init__(self):
        self.book_list = []
        self.storage_file = "books_data.json"
        self.load_books()

    def load_books(self):
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_books(self):
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def add_book(self, title, author, year, genre, read, favorite, story=""):
        new_book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read,
            "favorite": favorite,
            "story": story
        }
        self.book_list.append(new_book)
        self.save_books()

    def delete_book(self, title):
        self.book_list = [book for book in self.book_list if book["title"] != title]
        self.save_books()

    def update_book(self, title, updated_book):
        for i, book in enumerate(self.book_list):
            if book["title"] == title:
                self.book_list[i] = updated_book
                self.save_books()
                break

    def get_filtered_books(self, genre=None, read=None):
        books = self.book_list
        if genre:
            books = [b for b in books if b["genre"] == genre]
        if read is not None:
            books = [b for b in books if b["read"] == read]
        return books

    def get_favorite_books(self):
        return [b for b in self.book_list if b.get("favorite", False)]

    def export_to_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Book List", ln=True, align="C")

        for book in self.book_list:
            year = book.get("year", "Unknown Year")
            genre = book.get("genre", "Unknown Genre")
            read_status = "Read" if book.get("read", False) else "Unread"
            title = book.get("title", "Untitled")
            author = book.get("author", "Unknown Author")
            details = f"{title} by {author} ({year}) - {genre} - {read_status}"
            pdf.cell(200, 10, txt=details, ln=True)

        pdf_path = "book_list.pdf"
        pdf.output(pdf_path)
        return pdf_path

    def get_sorted_books(self, key):
        return sorted(self.book_list, key=lambda x: x.get(key, ""))

    def get_reading_progress(self):
        total = len(self.book_list)
        read = sum(1 for b in self.book_list if b.get("read", False))
        return read, total


book_manager = BookCollection()
st.title("📚 Personal Library Manager")

menu = st.sidebar.selectbox("Choose an action", [
    "Add Book", "View Books", "Filter Books", "Favorite Books",
    "Reading Progress", "Export PDF", "Sort Books", "Edit Book", "Delete Book"
])

if menu == "Add Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.text_input("Publication Year")
    genre = st.text_input("Genre")
    story = st.text_area("Write a short story or review about the book (optional)")
    read = st.checkbox("Have you read this book?")
    favorite = st.checkbox("Mark as favorite")

    if st.button("Add Book"):
        book_manager.add_book(title, author, year, genre, read, favorite, story)
        st.success("Book added successfully!")

elif menu == "View Books":
    st.subheader("📖 All Books")
    for book in book_manager.book_list:
        title = book.get("title", "Untitled")
        author = book.get("author", "Unknown Author")
        year = book.get("year", "Unknown Year")
        genre = book.get("genre", "Unknown Genre")
        story = book.get("story", "")

        st.write(f"**{title}** by {author} ({year}) - {genre}")
        if story:
            st.markdown(f"> _{story}_")
        st.markdown("---")

elif menu == "Filter Books":
    genre = st.text_input("Genre")
    read_status = st.selectbox("Read Status", ["All", "Read", "Unread"])
    read = None if read_status == "All" else (read_status == "Read")
    books = book_manager.get_filtered_books(genre or None, read)
    for book in books:
        st.write(book)

elif menu == "Favorite Books":
    st.subheader("❤️ Favorite Books")
    favorites = book_manager.get_favorite_books()
    for book in favorites:
        st.write(book)

elif menu == "Reading Progress":
    st.subheader("📈 Reading Progress")
    read, total = book_manager.get_reading_progress()
    st.write(f"You've read {read} out of {total} books.")
    fig, ax = plt.subplots()
    ax.pie([read, total - read], labels=["Read", "Unread"], autopct="%1.1f%%")
    st.pyplot(fig)

elif menu == "Export PDF":
    st.subheader("📤 Export Book List to PDF")
    if st.button("Generate PDF"):
        path = book_manager.export_to_pdf()
        with open(path, "rb") as f:
            st.download_button("Download PDF", f, file_name="book_list.pdf")

elif menu == "Sort Books":
    st.subheader("🗃️ Sort Books")
    sort_by = st.selectbox("Sort by", ["title", "author", "year"])
    sorted_books = book_manager.get_sorted_books(sort_by)
    for book in sorted_books:
        st.write(book)


elif menu == "Edit Book":
    st.subheader("✏️ Edit a Book/Story")
    titles = [book["title"] for book in book_manager.book_list]
    if titles:
        selected_title = st.selectbox("Select a book to edit", titles)
        selected_book = next((book for book in book_manager.book_list if book["title"] == selected_title), None)

        if selected_book:
            new_title = st.text_input("Book Title", selected_book["title"])
            new_author = st.text_input("Author", selected_book["author"])
            new_year = st.text_input("Publication Year", selected_book["year"])
            new_genre = st.text_input("Genre", selected_book["genre"])
            new_story = st.text_area("Write your story", selected_book.get("story", ""))
            new_read = st.checkbox("Have you read this book?", selected_book["read"])
            new_favorite = st.checkbox("Mark as favorite", selected_book["favorite"])

            if st.button("Update Book"):
                updated_book = {
                    "title": new_title,
                    "author": new_author,
                    "year": new_year,
                    "genre": new_genre,
                    "story": new_story,
                    "read": new_read,
                    "favorite": new_favorite
                }
                book_manager.update_book(selected_title, updated_book)
                st.success("Book updated successfully!")        

elif menu == "Delete Book":
    st.subheader("❌ Delete a Book")
    all_titles = [book["title"] for book in book_manager.book_list]
    if all_titles:
        book_to_delete = st.selectbox("Select a book to delete", all_titles)
        if st.button("Delete"):
            book_manager.delete_book(book_to_delete)
            st.success(f"'{book_to_delete}' has been deleted.")
    else:
        st.info("No books to delete.")
