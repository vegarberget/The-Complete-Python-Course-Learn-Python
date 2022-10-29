art_friends = {"Rolf", "Anne", "Jen"}
Science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(Science_friends)
science_but_not_art = Science_friends.difference(art_friends)

print(art_but_not_science)
print(science_but_not_art)