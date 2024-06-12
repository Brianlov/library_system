from newlibrary import * 
from borrow import *

def main():
    books = load_books_from_file('testingbook.txt')
    print(books)
    library1 = Library(books)
    print(library1)
    
    
    
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
            
                    
                
        
    
    #res=pinjam()
    
    #returned_book(res)
    
    
    
def returned_book(n):
    # with open("record.txt", 'r') as record:
    #     records = record.readlines()
    #     print(records)

    # updated_records = []
    # for record in records:
    #     print(book_name)
    #     if book_name not in n:
    #         updated_records.append(record)
    with open("testingbook.txt", "a") as books_available:
        for book in n:
            s,d=book.split()
            print(s)
            books_available.write( s )
            
        print(n)

        with open("record.txt", 'r+') as record_current:
            lines = record_current.readlines()
            record_current.seek(0)
            record_current.truncate()
            for line in lines:
                if line.strip() not in n:
                    record_current.write(line)
            
            
            
        

        # with open("record.txt", 'w') as record_delete:
        #     for e in updated_content:
        #         update_record.write(e)
   
        
            
    
            
if __name__ == "__main__":
    main()
    