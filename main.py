"""
Concepts We Are Practicing:
- Functions
- Loops and Menu-Driven Programs
- Lists and Data Filtering
- Dictionaries
- Counter (from collections)

Modules and Libraries:
- API Requests (requests)
- Text Processing (re - regular expressions)
"""

"""
Author: Your Name
GitHub Link: https://github.com/your-username/your-repo
Project: Book Analyzer (CS I Project)
Extra credit: I have fixed the bug in line no:.... or 
              I implemeted a new feature:  if choice == '6', new feature ............ will be executed
"""

import requests
import re
from collections import Counter


# -----------------------------
# INITIAL DATA
# -----------------------------

my_library = {
    "Moby Dick": "https://www.gutenberg.org/files/2701/2701-0.txt"
}

with open("EN-Stopwords.txt", 'r') as file:
    STOP_WORDS = set(line.strip().lower() for line in file)

    

# -----------------------------
# FETCH BOOK
# -----------------------------
def fetch_book(url):
    """Download text from a URL."""
    # TODO 4: Handle exceptions (network errors, invalid URLs, etc.) (1 point)


    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        book_data = response.text
        return book_data

    except requests.exceptions.RequestException:
        print("Error: Could not fetch the book")
        return None


# -----------------------------
# CLEAN TEXT
# -----------------------------
def clean_text(raw_text):
    """Lowercase text and remove punctuation."""
    text = raw_text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split()

# -----------------------------
# ANALYZE TEXT
# -----------------------------
def analyze_text(words):
    """Remove stop words and count frequencies."""
    filtered_words = [] 
    for w in words: 
        if w not in STOP_WORDS and len(w) > 2:   #checking len(w)> 2 to remove tiny words((is, to, at))
            filtered_words.append(w)

    return Counter(filtered_words).most_common(10)



# -----------------------------
# VISUALIZATION (BAR CHART)
# -----------------------------
def plot_results(stats, title):
    print(f"\nTop Words in '{title}':\n")
    
    for word, count in stats:
        bar = "█" * max(1, count //50)
        print(f"{word:10} | {bar} ({count})")

    
       

# -----------------------------
# MENU SYSTEM
# -----------------------------
def main():
    while True:
        print("\n--- LIBRARY MANAGER ---")
        print(f"Current Books: {list(my_library.keys())}")
        print("1. Add New Book")
        print("2. Remove Book")
        print("3. Update Book URL")
        print("4. Analyze a Book")
        print("5. Show Total Word Count")
        print("6. Exit")

        choice = input("\nSelect (1-6): ")

        if choice == '1':
            name = input("Enter Book Title: ").strip().title()
            url = input("Enter Gutenberg .txt URL: ").strip()

            if name == "" or url == "":
                print("Error: Enter Book Title and URL")
                continue
            
            for title in my_library:
                if title.lower() == name.lower():
                    print("Error: Book already exists in your library")
                    break
            
            else:
                my_library[name] = url
                print(f"'{name}' added.")
            

        elif choice == '2':
            
            name = input("Enter title to remove: ").strip().lower()

            found_title = None
            
            for title in my_library:
                if title.lower() == name:
                    found_title = title
                    break

            if found_title:
                del my_library[found_title]
                print(f"'{found_title}' has been removed from library")

            else: 
                    print("Book title was not found")
            

        elif choice == '3':
            # UPDATE OPERATION
            name_input = input("Enter the book title to update: ").strip().lower()
            target_key = None  # Start with None in case we don't find it

            for title in my_library:
                if title.lower() == name_input:
                    target_key = title
                    break  # We found it, so stop looking

            if target_key:
                print(f"Current URL: {my_library[target_key]}")
                new_url = input("Enter new URL: ").strip()
                if new_url == "":
                    print("Invalid URL. Update cancelled.")
                else:
                    my_library[target_key] = new_url
                    print(f"'{target_key}' updated successfully.")
            else:
                print("Book not found.")

        elif choice == '4':
            name_input = input("Which book to analyze? ").strip().lower()
            
            target_key = None
            for title in my_library:
                if title.lower() == name_input:
                    target_key = title
                    break

            if target_key:
                url = my_library[target_key]
                print(f"Fetching and analyzing '{target_key}'...")
                raw_text = fetch_book(url)

                if raw_text:
                    words = clean_text(raw_text)
                    stats = analyze_text(words)
                    plot_results(stats, target_key)
            else:
                print("Error: Book not found")

        elif choice == '5':
            name_input = input("Enter book title: ").strip().lower()

            selected_book = None
            for title in my_library:
                if title.lower() == name_input:
                        selected_book = title
                        break
                   
            if selected_book:
                url = my_library[selected_book]
                print(f"Fetching and counting '{selected_book}'...")

                raw_text = fetch_book(url)

                if raw_text:
                    words = clean_text(raw_text)
                    print(f"Total words in '{selected_book}': {len(words):,}")

            else:
                print("Book not found.")

        elif choice == '6':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()