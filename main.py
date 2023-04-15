import requests


class SuperheroesInfo:
    
    base_url = 'https://akabab.github.io/superhero-api/api'

    def __init__ (self, *heroes_names):    
        self.superheroes = requests.get(SuperheroesInfo.base_url + '/all.json').json()
        # self.selected_heroes = []
        self.selected_heroes_ids = {}
        for superhero in self.superheroes:
            if superhero['name'] in heroes_names:
                # Получена вся информацию обо всех супергероях
                # Можно было бы осуществлять получение характеристик нужных героев по ней
                # Но для тренировки работы с запросами будем получать информацию о способностях героя по его id
                # self.selected_heroes.append(superhero)
                self.selected_heroes_ids[superhero['name']] = superhero['id']
    
    def get_max_intelligence_hero(self):
        heroes_intelligence = {}
        for hero_name, hero_id in self.selected_heroes_ids.items():
            res = requests.get(SuperheroesInfo.base_url + f'/powerstats/{hero_id}.json').json()
            heroes_intelligence[hero_name] = res['intelligence']
        max_int_hero = max(heroes_intelligence.items(), key= lambda x: x[1])
        return max_int_hero[0]


super_heroes = SuperheroesInfo('Hulk', 'Captain America', 'Thanos')
print(f'The most intelligence superhero (from selected superheroes) is {super_heroes.get_max_intelligence_hero()}')
