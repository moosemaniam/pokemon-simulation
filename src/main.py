from baseclass import pokemon
from reader import database

global pokedb
pokedb=None
pokedb = database('Pokemon.csv')

for i in range(1,10):
  pokedb.print_info(i)

#first_pokemon = pokemon(1)
#first_pokemon.print_info()
