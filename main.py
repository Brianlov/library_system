from newlibrary import * 
from borrow import *

def main():
    books = load_books_from_file('testingbook.txt')
    print(books)
    library1 = Library(books)
    print(library1)
    
    res=pinjam()
    student=Student('ang')
    student.return_book(res)
    
    
    admin={}
    response=5
    username='Brian'
    password='okok'
    
    while True :
        if response==5:
            passkey='okok'
            y=input("passkey: ")
            if y==passkey:
                    
                        admin[username]=password
                        admin=Admin(username,password)
                        print('Welcome!!\nEnter your choice: \n1. Checking the book  \n2. Record')
                        response=int(input('\nEnter your choice: '))
                        if response == 1:
                            dict1=admin.display_bookNumber()
                            for key, value in dict1.items():
                                    print(f'{key}:{value}')
                            
                        if response == 2:
                            admin.check_record()
            
                    
                
        
    
 
    
    
    

        
            
    
            
if __name__ == "__main__":
    main()
    