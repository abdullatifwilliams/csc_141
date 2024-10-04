favorite_languages = {
    'abdul': 'Python',
    'mike': 'JavaScript',
    'karima': 'C++',
    'jier': 'Python'
}

people_to_poll = ['abdul', 'mike', 'karima', 'jier', 'dev', 'Zoe']


for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person}, for responding to the poll!")
    else:
        print(f"Hi {person}, we invite you to take the favorite languages poll!")