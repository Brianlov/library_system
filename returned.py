def returned_book(n,number):
    print(n)
    new_p=[]
    with open("testingbook.txt", "a") as books_available:
        for i in range(len(n)):
            if i==number:
                s,d=n[i].split()
                books_available.write(s)
                new_p.append(n[i])
                n.pop(i)
                break
    
            

    # Open the file in read mode to read the lines
    with open("record.txt", 'r') as record_current:
        lines = record_current.readlines()

    # Filter out the lines that contain strings in 'n'
    filtered_lines = [line for line in lines if line.strip() not in new_p]

    # Open the file in write mode to overwrite with the filtered lines
    with open("record.txt", 'w') as record_current:
        record_current.writelines(filtered_lines)
                
                    
    print('Thank you from returning the book safely!')
    
   
            
            
            
        

       