#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     12/06/2024
# Copyright:   (c) User 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from yuyuanclasslib import *
from borrow import *


def admin():

    admin={}
    username='Brian'
    password='okok'
    passkey='okok'
    y=input("passkey: ")
    if y==passkey:

        admin1=Admin(username,password)
        admin[username]=password

        print('Welcome!!\nEnter your choice: \n1. Checking the book  \n2. Record')
        response=int(input('\nEnter your response from 1:checking 2:Record: '))
        if response == 1:
            dict1=admin1.display_bookNumber()
            for key, value in dict1.items():
                print(f'{key}:{value}')

        elif response == 2:
            record=admin1.check_record()
            print(record)


def main():

    #borrow condition

    student=Student(input("name:"))
    books = load_books_from_file('testingbook.txt')
    print(books)
    library1 = Library(books)
    res=[]

    while(True):
        print("welcome to library system")
        print("What to do you prefer to do?")
        options = ("1.Borrow a book", "2.Return a book", "3.Read a book", "4.Access admin system","5.Printing receipt")

        for option in options:
            print(option)

        #done
        choice = input("Enter your choice from 1 to 5 : ")
        if choice == "1":
            # code for borrowing a book
            print("You chose to borrow a book.")
            res=student.request_book()
            books=[]
            for i in res:
                b, d = i.split()  # Split each element into 'b' and 'd'
                books.append(b)
            library1.borrowed_books(books)

            S_choice=input("Do you want to continue using this library system?Choose only with y or n:")
            if S_choice != "y":
                print("Thank you! Please come again (-v-)")
                break

        elif choice == "2":
            # code for returning a book
            print("You chose to return a book.")
            books=[]
            books=student.return_book(res)
            library1.return_book(books)
            print("return succesfully (^V^) ")
            S_choice=input("Do you want to continue using this library system?Choose only with y or n:")
            if S_choice != "y":
                print("Thank you! Please come again (-v-)")
                break

        elif choice == "3":
            # code for display all book
            print("You chose to display a book.")
            library1.displayAvailableBooks()
            S_choice=input("Do you want to continue using this library system?Choose only with y or n:")
            if S_choice != "y":
                print("Thank you! Please come again (-v-)")
                break

        #done
        elif choice == "4":
            # code for admin t
            print("admin login")
            admin()
            S_choice=input("Do you want to continue using this library system?Choose only with y or n:")
            if S_choice != "y":
                print("Thank you! Please come again (-v-)")
                break


        elif choice == "5":
            #code for printing receipt
            print("Printing receipt.....,please wait patiently(v)")
            return_day=date.today()
            res1=res.copy()

            for e in res1:
                book,d=e.split()
                name=student.name
                library1.print_receipt(name,book,d,return_day)
            print('\n')



        else:
            print("Invalid choice. Please enter according the choice given")
            S_choice=input("Do you want to continue using this library system?Choose only with y or n: ")
            if S_choice != "y":
                print("Thank you! Please come again (-v-)")
                break




if __name__ == '__main__':
    main()