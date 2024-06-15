#define class Library,attributes
from datetime import datetime, date, timedelta
import borrow

class Library:
    def __init__(self,book):
        #listofbooks
        self.books=book
        #issue the book_have been borrowed
        self.issue_book={}
        
        
    def displayAvailableBooks(self):
        
        for book in self.books:
            print(book)
        else:
            pass
        print('\n')
        
    def borrowed_books(self,books,name):
        for e in books:
            book,d=e.split()
            
            if book in self.books: 
                self.books.remove(book)
                self.issue_book[book]={"borrow_date": d,"borrower_name": name}
                print('borrow successfully')
                
            else:
                continue
       
        
    def return_book(self,books):
        if books is None:
            books = []  
        for e in books:
            self.books.append(e)
            del self.issue_book[e]
            print('returned successfully!')
        

        
    def total_admin(self,admin):
        for i in admin :
            print(admin)
    
    
    def borrow_receipt(self,borrower_name,book_title, borrow_date,return_date):
        if book_title not in self.books:
            self.issue_book[book_title] = {"borrower_name": borrower_name, "borrow_date": borrow_date}
        
            borrow_date = self.issue_book[book_title]["borrow_date"]
            max_return_date = datetime.strptime(borrow_date, "%Y-%m-%d").date() + timedelta(days=5)  # I assume the max borrow period is 2 weeks for now. You can change it later if you want la
            if return_date > max_return_date:
                penalty = (return_date - max_return_date).days * 0.8 # I put a basic formula for now to see if the calculation works
            else:
                penalty = 0
            print("Receipt:")
            print(f"Book Title: {book_title}")
            print(f"Borrower Name: {self.issue_book[book_title]['borrower_name']}")
            print(f"Borrow Date: {borrow_date}") # strftime will change the date and time to a string 
            print(f"Return Date: {return_date}") # %d-%m-%Y is the date and time format date/month/year
            print(f"Penalty: RM{penalty:.2f}")
        else:
            print('Book not available')
            
    def return_receipt(self,borrower_name,book_title,borrow_date,return_date):
        if book_title in self.issue_book:
            borrow_date = self.issue_book[book_title]["borrow_date"]
            max_return_date = datetime.strptime(borrow_date, "%Y-%m-%d").date() + timedelta(days=5)
            if return_date > max_return_date:
                penalty = (return_date - max_return_date).days * 0.8 # I put a basic formula for now to see if the calculation works
            else:
                penalty = 0
            print("Receipt:")
            print(f"Book Title: {book_title}")
            print(f"Borrower Name: {self.issue_book[book_title]['borrower_name']}")
            print(f"Borrow Date: {borrow_date}") # strftime will change the date and time to a string 
            print(f"Return Date: {return_date}") # %d-%m-%Y is the date and time format date/month/year
            print(f"Penalty: RM{penalty:.2f}")
        else:
            print('Book not available')
        
    def __str__(self):
        return ('Thank you')
        
            
       
        
class Student():
    def __init__(self,name):
        self.name=name
            
    def request_book(self):
        book=borrow.pinjam()
        return book
    def return_book(self,book_with_date):
        print('Return book')
        books=[]
        dates=[]
        book_copy=book_with_date.copy()
        for book in book_copy:
                s,d=book.split()
                books.append(s)
                dates.append(d)
        from returned import returned_book
        print('Your book available are: ')
            
        for i in range(len(books)):
            print(f'{i+1}. {books[i]}')
        number=get_int('Enter book number for returned: ')
        returned_book(book_with_date,number-1)
        return_book=[]
        return_book.append(books[i])
        print(return_book)
        return return_book
        
        
        
        
     
        
        
            
         
        
class Admin(Student):
    def __init__ (self,name,password):
        Student.__init__(self,name)
        self.password=password
        
    def check_record(self):
        records=load_books_from_file('record.txt')
        print(records)
            
    def display_bookNumber(self):
        dict1={}
        listofbook=load_books_from_file('testingbook.txt')
        for e in listofbook:
                
                dict1[e]=listofbook.count(e)
        return dict1
    
    def calc_penalty(self):
        pass
    
    


def load_books_from_file(filename):
        with open(filename, 'r') as file:
            books = [line.strip() for line in file.readlines()]
        return books
    

def get_int(prompt):
        while(True):
            try:
                return int(input(prompt))
            except ValueError:
                pass
        
def get_yes(prompt):
        while True:
            response = input(prompt)
            if response in ["y","yes","ok","n","no"]:
                return response
            else:
                pass
        


        
       
            
            
        
        







