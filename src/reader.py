import csv

import stat

class database(object):
  def __init__(self,filename):
    self.pokemon_info=[]
    with open(filename) as csvfile:
      csvreader= csv.reader(csvfile,delimiter=',')
      for row in csvreader:
         self.pokemon_info.append(row)

  def get_info(pokemon_id):
    id_from_file = 0
    #Some pokemon have multiple entries with same pokemon ids,
    #eg, Charizard, Mega evolution charizard all have
    #pokemon id of 6.So row number in file doesn't always match
    #the pokemon id number
    while(id_from_file!=pokemon_id)
      info = self.pokemon_info[pokemon_id]
      id_from_file = info[0]
      pokemon_id += 1


    info = self.pokemon_info[pokemon_id]
    return(info)

  def print_info(self,pokemon_id):
    print(self.pokemon_info[pokemon_id])
