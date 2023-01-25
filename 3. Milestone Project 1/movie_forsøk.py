MENU_PROMPT = "\nPress 'a' for for å legge til en film, 'l' for å se filmen, 'f' for å søke ettert film tittel, eller 'q' for å avslutte: "
movies = []

def add_movie():
    title = input("Skriv film titellen: ")
    director = input("Skriv navnet på film skaper: ")
    year = input("Skriv årstallet filmen ble gitt ut: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show_movies():
    for movie in movies:
        print_movie(movie)
        
        
def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")

def find_movie():
    search_title = input("Enter movie title you are looking for: ")

    
    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)
        
        
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'a':        
            add_movie()
        elif selection == 'l':
            show_movies()
        elif selection == 'f':
            find_movie()
        else:
            print ("ukjent kommando. Forsøk igjen.")
        
        selection = input(MENU_PROMPT)


menu()