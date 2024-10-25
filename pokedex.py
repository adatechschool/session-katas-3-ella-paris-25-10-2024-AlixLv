# lire le fichier : le programme accèe au fichier json + le programme charge le contenu du fichier dans sa mémoire
import json

def main():
    # Open and read the JSON file. Mode r = read mode: 
    with open('mock.json', 'r') as file:
        # loading the content of the file as a python dictionary:
        data = json.load(file)

    # Print the data from the JSON file:
    # print(data)

    # looping other data dictionary and creating a list in the list pokemonList, because data dictionary is composed of on only key and a list of values:
    for key, value in data.items():
        pokemonList = []
        pokemonList.append(value)
        # print(f'POKEMON: {pokemonList}')

    # looping with the function to get all the pokemons in a single list:
    pokemons = simpleListOfPokemons(pokemonList)
    print("\n -------------------------------------- \n")
    print(pokemons)

    # nombre de pokemons dans la liste pokemons :
    numberOfPokemons = getNumberOfPokemons(pokemons)
    print(f'Il y a {numberOfPokemons} pokemons dans la liste')

    # poids de tous les pokemons sous forme d'une liste contenant des dictionnaires : 
    weightPokemonList = getWeight(pokemons)
    print("⏺", weightPokemonList)
    print("\n -------------------------------------- \n")

    # liste nettoyée : suppression de "kg" et typage de la valeur en float:
    cleanedWeightPokemonList = getCleanedWeigthList(weightPokemonList)
    print("♻️", cleanedWeightPokemonList)
    print("\n -------------------------------------- \n")

    # # liste contenant uniquement les pokemons de plus de 10kg
    heavyPokemonList = getHeavyPokemon(cleanedWeightPokemonList)
    print("⭕️", heavyPokemonList)
    print("\n -------------------------------------- \n")

    # liste ordonnée par poids :
    orderheavypokemon = getByWeightOrderPokemon(heavyPokemonList)
    print("✅", orderheavypokemon)
    print("\n -------------------------------------- \n")

    # getByWeightOrderPokemon(heavyPokemonList)

#  ------------------------------------------------ FUNCTIONS ---------------------------------------------------

# creating a function to get a simple list of pokemons dictionaries: 
def simpleListOfPokemons(list):
    for item in list:
        getListOfPokemons(list)
    print(item)
    return item

def getListOfPokemons(pokemonList):
# looping on pokemonList nested in big list to get the dictionaries nested in the list:
    for list in pokemonList:
        for items in list:
            return items

 # nombre de pokemons dans la liste:
def getNumberOfPokemons(list):
    return len(list)

# liste de dictionnaires {pokemon : poids} pour tous les pokemons:
def getWeight(list):
    weightList = []
    for dictionaries in list:
        dict = {}
        for key, value in dictionaries.items():
            if key == "weight":
                print(dictionaries['name'], value)       
                dict.update({"name" : dictionaries['name'], "weight" : value})
                weightList.append(dict)
    return weightList            

# liste nettoyée avec un typage float pour la value et suppression de "kg":
def getCleanedWeigthList(list):
    newList = []
    for dictionaries in list:
        for key, value in dictionaries.items():
            if "kg" in value:
                newValue = value.replace("kg", "")
                dictionaries.update({key : float(newValue)})
                newList.append(dictionaries)
    return newList    


# obtenir uniquement les pokemons dont le poids est supérieur à 10kg : 
def getHeavyPokemon(list):
    newList = []

    for dictionaries in list:
        for key, value in dictionaries.items():
            if key == "weight" and value >= 10.0:
                newList.append(dictionaries)           
    return newList


# classer par ordre croissant de poids:
def getByWeightOrderPokemon(list):
    newList = list

    # using index in the list to compare dictionary at index with dictionary at index + 1: 
    for i in range(len(list)):
            for j in range(i + 1, len(list)):
                if newList[i]['weight'] > newList[j]['weight']:
                    newList[i], newList[j] = newList[j], newList[i]

    # autre manière avec méthode sorted() et paramètre key pour itérer sur une liste complexe contenant des dictionnaires
    # key=lambda est une fonction anonyme permettant d'indiquer qu'est-ce qu'on veut trier spécifiquement
    # newList = sorted(list, key=lambda dictionary: dictionary['weight'])             
    return newList
   

main()