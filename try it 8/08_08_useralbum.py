def make_album(artist, title):
    return {
        "artist": artist,
        "title": title
    }

while True:
    print("\nEnter the album details (or type 'quit' to exit):")

    artist = input("Artist name: ")
    if artist.lower() == 'quit':
        break

    title = input("Album title: ")
    if title.lower() == 'quit':
        break

    album = make_album(artist, title)
    print(f"\nAlbum created: {album}")