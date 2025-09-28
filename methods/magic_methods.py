# # Magic methods = Dunder methods (double underscore)  __init__, __str__, __eq__ 
# #     They are automatically called by many of Python's built-in operations.
# #     They allow developers to define or customize the behavior of objects

# class Student:
#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa

#     def __str__(self):
#         return f"Name: {self.name}, GPA: {self.gpa}"

#     def __eq__(self, other):
#         return self.name == other.name

#     def __gt__(self, other):
#         return self.gpa > other.gpa

# student1 = Student("Spongebob", 3.2)
# student2 = Student("Patrick", 2.0)

# print(student1)
# print(student2)
# print(student1 == student2)
# print(student1 > student2)


class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __len__(self):
        return self.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        # return self.title if key == "title" else self.author
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return None
        
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("1984", "George Orwell", 328)

# print(book1 < book2)
# print(book1 + book2)
# print("Gatsby" in book1)
# print("Orwell" in book1)
# print(book1["num_pages"])