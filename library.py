import json
import csv
import os


collection = "books.json"


def read_collection(books):
    if not os.path.exists(books):
        print("\nThe Book Collection does not Exist.\n")
        return None
    try:
        with open(books,'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("\nThere is an issue with opening the file.\n")
        return None


def main():

    # list of actions
    actions = [
        "Book Management",
        "1. Display Books",
        "2. Add Books",
        "3. Search a Book",
        "4. Sort Books",
        "5. Find Newest Book",
        "6. Find Oldest Book",
        "7. Export Titles to CSV",
        "8. Export Years to CSV",
        "9. Count Titles by Author",
        "10. Exit"
        ]
    
    # find the longest text
    # 30
    length = max(len(action) for action in actions)

    print()
    print("-" * 30)
    print(f"|{actions[0]: ^28}|")
    print(f"|{' '*28}|")
    print(f"| {actions[1]: <27}|")
    print(f"| {actions[2]: <27}|")
    print(f"| {actions[3]: <27}|")
    print(f"| {actions[4]: <27}|")
    print(f"| {actions[5]: <27}|")
    print(f"| {actions[6]: <27}|")
    print(f"| {actions[7]: <27}|")
    print(f"| {actions[8]: <27}|")
    print(f"| {actions[9]: <27}|")
    print(f"| {actions[10]: <27}|")
    print("-"*30)


def display_books(library):
    print("\nDisplaying Books...\n")

    books = read_collection(library)

    for count,book in enumerate(books,1):
        print(count)
        print("- Title: ",book['title'])
        print("- Author: ",book['author'])
        print("- Genre: ",book['genre'])
        print("- Publication Year: ",book['publication year'])
        print("- Price: ",book['price'])
        print('------------------------------')

def add_book(books):
    print("\nAdding Book...\n")
    
    while True:
        print("1. Add Book")
        print("2. Back")
        print("-----------")

        user_input = input("Enter a Number: ")

        try:
            user_input = int(user_input)
            if user_input == 1:
                data = {}

                # request data
                title = input("Enter Title: ").title()
                author = input("Enter Author: ").title()
                genre = input ("Enter Genre: ").title()
                
                # get publication year
                # we use while loop in case of value error we want to try again till we got the right value
                publish = 0
                while True:
                    try:
                        publish = int(input("Enter Publication Year: "))
                        break
                    except ValueError:
                        print("\nEnter publication year (e.g. 2022)\n")
                        continue
                # get price
                price = 0
                while True:
                    try:
                        price = float(input("Enter Price: "))
                        break
                    except ValueError:
                        print("\nEnter price (e.g. 50)\n")
                        continue
                    
                # store the entered data
                data['title'] = title
                data['author'] = author
                data['genre'] = genre
                data['publication year'] = publish
                data['price'] = price

                # display requested data
                print("\nThe Book You Want To Add is: \n")
                print("title: ",title)
                print("author: ",author)
                print("genre: ",genre)
                print("publication year: ",publish)
                print("price: ",price)
                print("---------------")

                accept = input("Do You Want to Add, Enter (yes or no): ")

                if accept.lower() == "yes":
                    with open(books,'r') as file:
                        new_file = json.load(file)
                        new_file.append(data)
                    with open(books,"w") as f:
                        json.dump(new_file,f,indent=2)
                    print("\nBook added to the collection\n")
                    break
                else:
                    print("\nBook not Added\n")
                    continue
            
            if user_input == 2:
                break
            
        except ValueError:
            print("Enter a Valid Number!")
            continue




def search_book(library):
    
    print("\nSearching By Title:\n")
    print("* To Exit enter exit\n")
    
    books = read_collection(library)

    # while loop to do multiple search 
    while True:
        user_input = input("Enter a Title: ")
        if user_input.lower() == 'exit':
            break

        find = [book for book in books if  book['title'].lower() == user_input.lower()]
        if find:
            for text in list(find):
                print()
                print("Title: ",text['title'])
                print("Author: ",text['author'])
                print("Genre: ",text['genre'])
                print("Publication Year: ",text['publication year'])
                print("Price: ",text['price'])
                print()
                continue
        else:
            print("\nNot Found ......\n")
            continue


def sort_books(library):
    print("\nSorting Books By Title...\n")
    books = read_collection(library)
    sorted_books = sorted(books,key=lambda book:book.get("title",""))
    for count,book in enumerate(sorted_books,1):
        print(f"{count:02}. ",book['title'])
        


def find_newest(library):
    print("\nFinding Newest Book by Publication Year...\n")

    books = read_collection(library)
    sorted_books = sorted(books,key=lambda book:book.get("publication year",""),reverse=True)
    print("sort_books ",type(sorted_books))
    recent_year = sorted_books[0]['publication year']
    newest_books = list(filter(lambda book:book['publication year'] == recent_year,sorted_books))
    for count,book in enumerate(newest_books,1):
        print(count)
        print("- Title: ",book['title'])
        print("- Author: ",book['author'])
        print("- Genre: ",book['genre'])
        print("- Publication Year: ",book['publication year'])
        print("- Price: ",book['price'])
        print('------------------------------')

def find_oldest(library):
    print("\nFinding Oldest Book by Publication Year...\n")

    books = read_collection(library)
    sorted_books = sorted(books,key=lambda book:book.get("publication year",""))
    oldest_year = sorted_books[0]['publication year']
    oldest_books = list(filter(lambda book:book['publication year'] == oldest_year,sorted_books))
    for count,book in enumerate(oldest_books,1):
        print(count)
        print("- Title: ",book['title'])
        print("- Author: ",book['author'])
        print("- Genre: ",book['genre'])
        print("- Publication Year: ",book['publication year'])
        print("- Price: ",book['price'])
        print('------------------------------')


def export_titles(library):
    print("\nExporting Titles...\n")

    # initalize the file name
    titles = "titles.csv"

    # get books
    books = read_collection(library)

    # write titles to acsv file
    try:
        with open(titles,'w') as file:
            header = ["Number","Title"]
            writer = csv.writer(file)
            writer.writerow(header)
            for count,book in enumerate(books,1):
                writer.writerow([count,book["title"]])
            print(f"Titles successfully exported to {titles}\n")
    except IOError as e:
            print(f"Error while writing to file: {e}\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")
    


def export_years(library):
    print("\nExporting Years...\n")
    publication_years = "publication_years.csv"

    books = read_collection(library)

    # write titles to acsv file
    try:
        with open(publication_years,'w') as file:
            header = ["Number","Publication Year"]
            writer = csv.writer(file)
            writer.writerow(header)
            for count,book in enumerate(books,1):
                writer.writerow([count,book["publication year"]])
            print(f"Publication Years successfully exported to {publication_years}\n")
    except IOError as e:
            print(f"Error while writing to file: {e}\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")

def count_titles(library):
    print("\nCounting Titles by Author...\n")
    print("* To Exit enter exit \n")

    while True:
        books = read_collection(library)
        user_input = input("Enter Author Name: ").lower()
        if user_input == "exit":
            break
        auther_books = [book for book in books if book['author'].lower() == user_input ]
        if not auther_books:
            print(f"\nThere is no book by {user_input}")
        for count,book in enumerate(auther_books,1):
            print(f"\n{count}. {book["title"]}")
        print()
            



while True:
    # checking the collection
    if not read_collection(collection):
        break

    main()
    user_input = input("\nEnter a Number: ")

    
    try:
        user_input = int(user_input)
        if user_input == 1:
            display_books(collection)
        elif user_input == 2:
            add_book(collection)
        elif user_input == 3:
            search_book(collection)
        elif user_input == 4:
            sort_books(collection)
        elif user_input == 5:
            find_newest(collection) 
        elif user_input == 6:
              find_oldest(collection)
        elif user_input == 7:
            export_titles(collection)
        elif user_input == 8:
            export_years(collection)
        elif user_input == 9:
            count_titles(collection)
        elif user_input == 10:
            print("\nExiting...\n")
            break
        else:
            print("\nEnter a Valid Number! ")
            continue
    except ValueError:
        print("\nEnter a Valid Number!")
        continue