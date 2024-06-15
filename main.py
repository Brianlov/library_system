from newlibrary import *
from borrow import *
from datetime import date, timedelta

def admin():
    
    
    admin={}

    passkey='librarysystem'
    y=input("passkey: ")
    if y==passkey:
        username=input('Username: ')
        password=input('Password: ')
        admin1=Admin(username,password)
        admin[username]=password

        print('Welcome!!\nEnter your choice: \n1. Checking the number of books in library  \n2. borrowing_record')
        response=get_int('\nEnter your response from 1:checking 2:Record: ')
        if response == 1:
            dict1=admin1.display_bookNumber()
            for key, value in dict1.items():
                print(f'{key}:{value}')

        elif response == 2:
            record=admin1.check_record()
            print(record)


def main():

    #borrow condition
    print('**************************************************************\n                     Library System\n**************************************************************')
    student=Student(input("Welcome !\nEnter your student_id:"))
    books = load_books_from_file('testingbook.txt')
    print(books)
    library1 = Library(books)
    res=[]

    while(True):
        print("welcome to library system")
        print("What to do you prefer to do?")
        print("1.Borrow a book")
        print("2.Return a book")
        print("3.Read a book")
        print("4.access admin system")
        print("5.Print receipt")

        #done
        choice = input("Enter your choice from 1 to 5: ")
        if choice == "1":
            # code for borrowing a book
            print("You chose to borrow a book.")
            #return sample['nogizaka46 2001-08-08']
            res=student.request_book()
            books=res.copy()
            #append book name into it
            library1.borrowed_books(books,student.name)

            
            S_choice=input("Do you want to continue using this library system?Choose only with y or n")
            if S_choice != "y":
                print("Thank you! Please come again (-v-)")
                break

        elif choice == "2":
            # code for returning a book
            print("You chose to return a book.")
            res1=res.copy()
            #the book sample-['nogizaka46']
            bookreturned=student.return_book(res)
            #the book have been borrowed-'sample:KakiHaruka 2001-08-08
            #book-book title,d-borrow_date
            for e in res1:
                booked,d=e.split()
                #if Nogizaka46==Nogizaka46
                if booked==bookreturned[0]:
                    #time return book if the time return is larger than 5,there will have penalty
                    return_day=(datetime.strptime(d, "%Y-%m-%d")+timedelta(days=6)).date()
                    print(student.name,booked,d,return_day)
                    library1.return_receipt(student.name,booked,date.today(),return_day)
                else:
                    continue
            #append the book into the library
            library1.return_book(bookreturned)
            
            S_choice=input("Do you want to continue using this library system?Choose only with y or n")
            if S_choice != "y":
                print("Thank you! Please come again (-v-)")
                break

        elif choice == "3":
            # code for display all book
            print("You chose to display a book.")
            library1.displayAvailableBooks()
            S_choice=input("Do you want to continue using this library system?Choose only with y or n")
            if S_choice != "y":
                print("Thank you! Please come again (-v-)")
                break

        #done
        elif choice == "4":
            # code for admin t
            print("admin login")
            admin()
            S_choice=input("Do you want to continue using this library system?Choose only with y or n")
            if S_choice != "y":
                print("Thank you! Please come again (-v-)")
                break


        elif choice == "5":
            #code for printing resit
            print("Printing resit.....,please wait patiently(v)")
            res1=res.copy()

            for e in res1:
                book,d=e.split()
                name=student.name
                return_day=(datetime.strptime(d, "%Y-%m-%d")+timedelta(days=6)).date()
                library1.borrow_receipt(name,book,d,return_day)
            print('\n')



        else:
            print("Invalid choice. Please enter according the choice given")
            S_choice=input("Do you want to continue using this library system?Choose only with y or n")
            if S_choice != "y":
                print("Thank you! Please come again (-v-)")
                break





main()