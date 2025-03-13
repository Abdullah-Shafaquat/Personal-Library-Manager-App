from altair import Title
import streamlit as st
import json

# load & save library data
def load_library_data():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library_data():
    with open("library.json" , "w") as file:
        json.dump(library , file , indent=4)

# initialize library
library = load_library_data()


# app title
st.title("Personal Library Manager App 📚")

# menu
menu = st.sidebar.radio(" 📌 Select an option" ,[ "Add Books 🆕" , "Remove Books  ❌" , "Search Book 🔍" , "Save & Exit 💾" ,"View Library 📗" ,])
# View Library
if menu == "View Library 📗":
    st.title("Your Library 📗")
    total_books = len(library)
    if library:
        st.write(f"Total Books: {total_books}")
        st.table(library)
    else:
        st.write("Your Library Is Empty 🚫")

# Add Books
elif menu == "Add Books 🆕":
    st.title("Add A New Books ➕➖📗")
    title = st.text_input("Title" , placeholder="Enter Your Book Title")
    author = st.text_input("Author Name" , placeholder="Enter A Book Author Name")
    year = st.number_input("Year" , min_value=2000 , max_value=2025 ,step=1  )
    categories = st.selectbox("Select a category of book",[ "Dystopian", "Classics", "Literary Fiction", "History", "Fantasy", "Science Fiction", "Other"])
    quantity = st.number_input("Quantity", min_value=1 , step=1 , placeholder="Enter A Books Quantity") 

    


    if st.button("Add Book"):
        library.append({
            "title": title,
            "author": author,
            "year": year,
            "categories": categories ,
            "books quantity" : quantity
        })
        save_library_data()
        st.success(f"Book {title} Added Successfully! 🎉")
       
# remove book 
elif menu == "Remove Books  ❌" :
    st.title("Remove Books 📗➖🗑️")
    book_title = [book["title"] for book in library]

    if book_title :
        selected_book = st.selectbox("Select a book to remove" , book_title)
        if st.button("Remove a book") :
            library = [book for book in library if book ["title"] != selected_book]
            save_library_data()
            st.success(f"Book {book_title} Remove Successfully!")
            
    else :
        st.warning("Library Is Empty")

# Search Book
elif menu == "Search Book 🔍" :
    st.title("Search A Book 🔍➖📖")
    serchbook = st.text_input("Enter a book title or author name to Search Book")

    if st.button("Search Book") :
        result = [book for book in library if serchbook.lower() in book["title"].lower() or serchbook.lower() in book["author"].lower()]
        if result :
            st.table(result)
        else :
            st.warning("Book Not Found")

elif menu == "Save & Exit 💾":
   st.success("💾 Library Saved! Successfully👋")