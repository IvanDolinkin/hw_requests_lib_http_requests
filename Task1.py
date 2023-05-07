import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)
data = resp.json()


def most_clever(all_heroes, names):
    heroes_dict = {}
    for hero in all_heroes:
        if hero['name'] in names:
            heroes_dict[hero['name']] = hero['powerstats']['intelligence']
    heroes_dict_sorted = sorted(heroes_dict.items(), key=lambda x: x[1], reverse=True)
    result = {'name': heroes_dict_sorted[0][0], 'intelligence': heroes_dict_sorted[0][1]}
    return result


compare_list = ['Hulk', 'Captain America', 'Thanos']

print(f'The most clever hero is {most_clever(data, compare_list)["name"]} '
      f'with intelligence {most_clever(data, compare_list)["intelligence"]} points')
