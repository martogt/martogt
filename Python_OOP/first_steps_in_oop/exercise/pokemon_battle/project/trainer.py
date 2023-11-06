from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name in [pok.name for pok in self.pokemons]:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for p in self.pokemons:
            if p == pokemon_name:
                self.pokemons.remove(p)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        info = [f"Pokemon trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for p in self.pokemons:
            info.append(f"- {p.pokemon_details()}")
        return "\n".join(info)