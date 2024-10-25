def make_album(artist, title):
    return {
        "artist": artist,
        "title": title
    }

# Create three dictionaries representing different albums
album1 = make_album("The Weeknd", "After Hours")
album2 = make_album("Taylor Swift", "Folklore")
album3 = make_album("Adele", "30")

# Print each album dictionary to show the stored information
print(album1)
print(album2)
print(album3)