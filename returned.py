def returned_book(n):

    with open("testingbook.txt", "a") as books_available:
        for book in n:
            s,d=book.split()
            books_available.write( s )
            

        with open("record.txt", 'r+') as record_current:
            lines = record_current.readlines()
            record_current.seek(0)
            record_current.truncate()
            for line in lines:
                if line.strip() not in n:
                    record_current.write(line)
                    
    print('Thank you from returning the book safely!')
            
            
            
        

       