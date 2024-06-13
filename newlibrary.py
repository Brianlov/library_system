#define class Library,attributes
from datetime import datetime, date, timedelta

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
            print('Book not available')
        print('\n')

        
    def total_admin(self,admin):
        for i in admin :
            print(admin)
    
    
    def print_receipt(self,borrower_name,book_title, borrow_date,return_date):
        if book_title in self.books:
            self.books.remove(book_title)
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
        
    def __str__(self):
        return ('Thank you')
        
            
       
        
class Student():
    def __init__(self,name):
        self.name=name
            
    def request_book(self):
        book=input("What book do u want to borrow")
        return book
    def return_book(self,book_with_date):
        res=get_int('Enter your choice: \n1. check your book\n2. return your book\n3. checking penalty\n4. exit')
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
        records=load_books_from_file('record.txt')
        for i in records:
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
        


        
       
            
            
        
        







