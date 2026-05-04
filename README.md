How the code works:
  1. fetches data using API
     - uses "requests.get()"
     - extracts text with ".txt"
  2. text cleaning
     - lowercases all words
     - handles whitespace
  3. text analysis
     - stop words are removed
     - counts most frequent words
     - counts total words
  4. visualization
     - top 10 used words are displayed in bar chart 
  5. library manaagement
     - key = book title
     - value = URL
     - allows the program to perform CRUD operations

Why it matters:

  This project demonstrates the fundamentals of Python concepts and how they can be applied to real-world problems using data gathered from the internet. It helped develop an understanding of how to work with APIs by showing how Python programs can request, recieve, and handle data from external sources. This project also highlights the importance of data cleaning, considering that raw text taken from the internet can often be inconsistent. Further, this project utilizes dictionaries, loops, and functions in order to organize and manage data. The added feature calculates the total word count in a book which demonstrates how existing code can be extended and refined, which reinforces the idea that programs can contintue to grow and improve. 


How to run:

pip install requests
