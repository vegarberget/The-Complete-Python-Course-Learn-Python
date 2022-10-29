name = input("Fornavn: ")
surname = input("Etternavn: ")

greeting = name or f"Mr. {surname}"
print("Hello " + greeting + "!")