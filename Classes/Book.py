class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages= pages
    
    def get_info(self): 
        return f'A book titled {self.title} by {self.author} with {self.pages} pages '
               