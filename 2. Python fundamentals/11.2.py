friends = ["Rolf", "ruth", "charlie", "jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = set([f.lower() for f in friends])

present_friends = [
    name.title() for name in guests if name.lower() in friends_lower
]
print(present_friends)