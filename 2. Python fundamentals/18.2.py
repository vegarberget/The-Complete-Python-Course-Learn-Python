# når python definerer en funksjon så låser den variabelen satt i funksjonen.
default_y = 3

def add(x, y=default_y):
    total = x + y
    print(total)
    
add(2)

# default_y = 4 gir dremdeles samme verdi på default_y som tidligere satt inni funksjonen.