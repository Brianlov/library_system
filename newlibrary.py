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
    def return_book(self,book_with_date):
        res=int(input('Enter your choice: \n1. check your book\n2. return your book\n3. checking penalty\n4. exit'))
        books=[]
        dates=[]
        book_copy=book_with_date.copy()
        for book in book_copy:
                s,d=book.split()
                books.append(s)
                dates.append(d)
        if res==1:
            print('Your have borrowed {}'.format(books))
            return
        elif res==2:
            from returned import returned_book
            returned_book(book_with_date)
            return
        elif res==3:
            from datetime import datetime, date, timedelta
            #change the string to time-format
            due_date = datetime.strptime('2024-6-10', "%Y-%m-%d").date()
            p = []

            for d in dates:
                d_date = datetime.strptime(d, "%Y-%m-%d").date()  # Convert 'd' from string to datetime.date
                delta_days = (d_date - due_date).days  # Calculate the difference in days
                #check whether 
                if delta_days>=1:
                    p.append(delta_days * 0.8)  # Calculate penalty
                else:
                    p.append(0)

            
            penalty={}
            for i in range(len(books)):
                penalty[books[i]]=p[i]
            print(penalty)
        elif res==4:
            return 0
            
         
        
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
        
        
       
            
            
        
        







