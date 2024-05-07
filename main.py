from functions import *
from book import *


add_book('9383093943', 'Python Crash Course', 'No Starch Press', 'English', 10, True)
add_book("978-0262013199", "Introduction to Machine Learning", "MIT Press", "English", 50, False)

print("What would you like to do?:")
print("a. Display all book records")
print("b. Add new book records")
print("c. Sort books by their Publisher in ascending order using only Bubble Sort")
print("d. Sort books by their Number of Copies in descending order using only Insertion Sort")
print("e. Exit the program.\n")

#choice = input("Enter your choice: ").lower()
choice = 'a'

if choice == 'a':
    display_all_books()
    print(len(books))


