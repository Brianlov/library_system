#-------------------------------------------------------------------------------
# Name:        borrow
# Purpose:
#
# Author:      Ang Wei Ding
#
# Created:     10/06/2024
# Copyright:   (c) Ang Wei Ding 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------




def pinjam():
    res = []
    cont = "y"

    while cont == "y":

        print ("books available:\n")

        books_available = open ("testingbook.txt", "r")
        l = books_available.readlines()
        books_available.close()

        number = 1
        for x in l:
            print (number , ". ", x)
            number += 1

        boolean=False

        while boolean==False:

            choose = int(input("Choose a book you want to borrow: "))

            if 0 < choose <= len(l):


                borrowing = l.pop(choose-1)
                print("\nYou have choosen: ", borrowing)


                while True:
                    borrow_days = int(input("How long do you wish to borrow this book (max 5 days): "))
                    if 1 <= borrow_days <= 5:
                        break
                    else:
                        print("Invalid input. Please enter a number between 1 and 5.")

                from datetime import datetime, date, timedelta
                today = date.today()
                print("Please return your book by", today + timedelta(days=borrow_days))
                boolean = True

            else:
                print("Please enter a relevent book\n")
                boolean = False

        books_borrowed = open ("record.txt", "a")
        record = str(borrowing).strip() + " " + str(today + timedelta(days=borrow_days)) + "\n"
        books_borrowed.write (record)
        books_borrowed.close()

        books_available = open ("testingbook.txt", "w")
        for x in l:
            books_available.write(x)

        books_available.close()



        res.append (str(borrowing).strip() + " " + str(today + timedelta(days=borrow_days)))


        cont = str(input("Do you wish to continue? y/n\n"))
    return res





if __name__ == '__main__':
    pinjam()