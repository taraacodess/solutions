class Book:

    def __init__(self,name, author):
        self.name=name
        self.author=author

    def full_name(self):
        return "it is a good deal"   

fav_book=Book("thug","jenny")
print(fav_book.name) 
print(fav_book.full_name())   