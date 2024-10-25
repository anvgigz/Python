#book title collection


def printing_list(sorted_book_Titled_list):
    #print the sorted list of book titles
    for book in sorted_book_Titled_list:
        print(book)

#Main function
def main():
    #book titles list
    book_titles = []
    #counter
    books = 0
    #counter for book titles
    while books <10:
        #request user input for book titles
        title = input("Enter a book title: ")
        #capitilize book titles with title function
        title = title.title()
        #add the book to the list (book_titles)
        book_titles.append(title)
        #increment books counter
        books += 1
    #copy list to new list and sort them
    sorted_book_Titled_list = sorted(book_titles)
    #call the printing_list function
    printing_list(sorted_book_Titled_list)

if __name__ == "__main__":
    main()


