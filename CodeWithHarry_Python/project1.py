import os

class Library:
    numberOfBooks = 0
    file1 = "project1_file1.txt"
    file2 = "project1_file2.txt"

    @staticmethod
    def GetLibraryDirectory():
        ''' returns the directory of assets folder where the files are saved'''
        return "D:/Coding Stuff, Editing/Visual Studio Python Codings/CodeWithHarry_Python/assets"
    
    @staticmethod
    def PrintBook(args):
        '''
        method to print the bok, needs to pass a list as an arguement, list should be of length 3
        '''
        l = ""
        if len(args)==4:
            l += "Book name : "+ args[1]
            l += " -- Author : "+ args[2]
            l += " -- Publisher : "+ args[3]
        elif len(args)==2:
            l += "Book name : "+ args[1]
            l += " -- Author : [NONE]"
            l += " -- Publisher : [NONE]"
        else:
            l = "[Book in unknown format]"
        print(l,end = "")
    
    def GetNumberOfBooksInLibrary(self):
        '''returns the number of books currently present in the library'''
        number = 0
        with open(os.path.join(self.GetLibraryDirectory(),self.file1)) as fp:
            for _ in fp: # donno how to solve this warning from occuring
                number +=1
        return number

    def DisplayBooks(self):
        '''
        method to display all books currently available in the library
        '''
        print("-".center(80,"-"))
        print("Displaying all the books in the LIBRARY".center(80,"-"))
        print("-".center(80,"-"))
        with open(os.path.join(self.GetLibraryDirectory(),self.file1)) as fp:
            for line in fp:
                self.PrintBook(line.split("-----"))
        print("\n"+"-".center(80,"-"))

    def AddBook(self, book_name, book_author, book_publisher):
        '''
        adds a book to the library list of books. Takes 3 arguements - book name, author and publisher
        '''
        self.numberOfBooks = self.GetNumberOfBooksInLibrary()+1
        try:
            fp = open(os.path.join(self.GetLibraryDirectory(),self.file1), 'a')
            fp.write("\n"+str(self.numberOfBooks)+"-----"+book_name+"-----"+book_author+"-----"+book_publisher)
            fp.close()
            print("Book added successfully")
        except:
            print("[Error in file open] Book could not be saved")

    def LendBook(self, bookName, name, age):
        try:
            fp1 = open(os.path.join(self.GetLibraryDirectory(),self.file1), 'r')
            for line in fp1:
                if bookName in line:
                    l = line.split("-----")
                    print("-".center(80,"-"))
                    print(f"Book: '{l[1]}', Author: '{l[2]}', Publisher: '{l[3]}'\n----- has been lent to '{name}' of age {age}. -----")
                    print("-".center(80,"-"))
                    #print("working 1")

                    from datetime import datetime
                    date = datetime.now().strftime("%H:%M%p %d/%m/%Y")

                    #print("working 2")
                    try:
                        #print("working 2.33")
                        fp2 = open(os.path.join(self.GetLibraryDirectory(),self.file2), 'a')
                        fp2.write(f"Book Issue Date: {date}-----{name}_{age}-----{l[1]}-----{l[2]}-----{l[3]}\n")
                        fp2.close()
                        #print("working 2.5")
                        print("[Book Registry Updated]".center(80, "-"))
                        #print("working 2.67")
                    except:
                        print("[ERROR: Book Registry directory not found / Error in format]")
                    
                    print("Book lent successfully")
                    #print("working 3")
                    break
            fp1.close()
        except:
            print("Library directory unknown")

    def ReturnBook(self, bookName):
        try:
            fp1 = open(os.path.join(self.GetLibraryDirectory(),self.file1), 'r')
            for line in fp1:
                if bookName in line:
                    l = line.split("-----")
                    print("-".center(80,"-"))
                    print(f"Book: '{l[1]}', Author: '{l[2]}', Publisher: '{l[3]}'\n----- has been returned to the library. -----")
                    print("-".center(80,"-"))
                    #print("working 1")

                    from datetime import datetime
                    date = datetime.now().strftime("%H:%M%p %d/%m/%Y")

                    #print("working 2")
                    try:
                        #print("working 2.33")
                        fp2 = open(os.path.join(self.GetLibraryDirectory(),self.file2), 'a')
                        fp2.write(f"Book Return Date: {date}-----{l[1]}-----{l[2]}-----{l[3]}\n")
                        fp2.close()
                        #print("working 2.5")
                        print("[Book Registry Updated]".center(80, "-"))
                        #print("working 2.67")
                    except:
                        print("[ERROR: Book Registry directory not found / Error in format]")
                    
                    print("Book Returned successfully")
                    #print("working 3")
                    break
            fp1.close()
        except:
            print("Library directory unknown")

indianLibrary = Library()
indianLibrary.DisplayBooks()
# indianLibrary.AddBook("some name", "some author", "some publications")

indianLibrary.LendBook("Charlotte's Web", "Ravi", 34)
indianLibrary.ReturnBook("Charlotte's Web")
#indianLibrary.AddBook("Harry Potter","some author","some publisher")