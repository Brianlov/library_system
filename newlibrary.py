#define class Library,attributes

class Library:
    def __init__(self,book):
        self.books=book
        self.issue_book={}
        
        
    def displayAvailableBooks(self):
        
        for book in self.books:
            print(book)
        print('\n')
            
            
    def issue_book(self,book,student):
        if book in self.books:
            self.books.remove(book)
            self.issued_books[book]=student
        else:
            print('Book not available')
            
    
    
    def borrowBook(self):
        book=input("What book do u want to borrow")
        if book not in self.books:
            print("Book not available")
        else:
            self.books.remove(book)
            print('Thank you for borrowing the book!')
            
    def returnBook(self):
        name=input("What is the book u want to return?")
        
    def total_admin(self,admin):
        for i in admin :
            print(admin)
    
        
    def __str__(self):
        return ('Thank you')
        
            
       
        
class Student():
    def __init__(self,name):
        self.name=name
            
    def request_book(self):
        book=input("What book do u want to borrow")
        return book
    def return_book(self):
        book=input("Please enter the book u want to retun")
        return book
        
class Admin(Student):
    def __init__ (self,name,password):
        Student.__init__(self,name)
        self.password=password
        
    def check_record(self):
        with open("record.txt", 'r') as record:
            records = [line.strip() for line in record.readlines()]
            print(records)
            
    def display_bookNumber(self):
        dict1={}
        with open("testingbook.txt",'r') as books:
            listofbook=[line.strip() for line in books.readlines()]
            for e in listofbook:
                
                dict1[e]=listofbook.count(e)
        return dict1
    
    

                
        
def track():
    def __init__(self,book):
        self.book=book


def load_books_from_file(filename):
        with open(filename, 'r') as file:
            books = [line.strip() for line in file.readlines()]
        return books
        
        
       
            
            
        
        







