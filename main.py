
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
