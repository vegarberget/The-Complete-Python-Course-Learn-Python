friends = ["Rolf", "ruth", "charlie", "jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

print(friends_lower.intersection(guests_lower))