class Book():
    def __init__(self,title,author,ISBN,total_copies,available_copies):
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self.total_copies=total_copies
        self.available_copies=available_copies

    def borrow(self):
        if self.available_copies>0:
            self.available_copies-=1
            return f'You can borrow the book available copies={self.available_copies}.'
        else:
            return f'Sorry the book with name is "{self.title}" not available.)'
    
    def return_book(self):
        if self.available_copies<self.total_copies:
            self.available_copies+=1
            return f'You have return {self.title} with ISBN {self.ISBN}.'
        else:
            return f'All copies of the book {self.title} is already available.'
        
    def isavailable(self):
        return self.available_copies>0
    
    def book_detail(self):
        return{
            'book_name':self.title,
            'author':self.author,
            'ISBN':self.ISBN,
            'total_copies':self.total_copies,
            'available_copies':self.available_copies
        }
    
obj=Book("Muna madan","Devkota","978-9937942003",18,0)

print(obj.borrow())
print(obj.return_book())
print(obj.isavailable())
print(obj.book_detail())