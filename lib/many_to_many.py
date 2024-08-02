class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        self.contracts_list = []
        Book.all_books.append(self)

    def contracts(self):
        return self.contracts_list

    def authors(self):
        return [contract.author for contract in self.contracts_list]


class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        self.contracts_list = []
        Author.all_authors.append(self)

    def contracts(self):
        return self.contracts_list

    def books(self):
        return [contract.book for contract in self.contracts_list]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts_list)


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all_contracts.append(self)
        author.contracts_list.append(self)
        book.contracts_list.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]


# Example usage:
# Create an author and a book
author1 = Author("Jane Doe")
book1 = Book("My First Book")

# Sign a contract
contract1 = author1.sign_contract(book1, "2023-08-01", 15)

# Get the author's contracts
print(author1.contracts())  # [contract1]

# Get the author's books
print(author1.books())  # [book1]

# Get the author's total royalties
print(author1.total_royalties())  # 15

# Get contracts by date
print(Contract.contracts_by_date("2023-08-01"))  # [contract1]

# Get the book's contracts
print(book1.contracts())  # [contract1]

# Get the book's authors
print(book1.authors())  # [author1]


