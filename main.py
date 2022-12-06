
heroes_data = requests.get('https://akabab.github.io/superhero-api/api/all.json').json

heroes = list(filter(lambda hero: hero['name'] in ['Hulk', 'Captain America', 'Thanos'], heroes_data))

int_dict = {hero['name']:hero['powerstats']['intelligence'] for hero in heroes}

print(max(int_dict, key=int_dict.get))
