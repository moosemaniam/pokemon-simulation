csvidx= {"pokeid":0,
               "name":1,
               "type1":2,
               "type2":3,
               "total":4,
               "hp":5,
               "attack":6,
               "defense":7,
               "special_attack":8,
               "special_defines":9,
               "speed":10,
               "generation":11,
               "legendary":12
               }

class stat_class(object):

    global pokedb
    def __init__(self,pokeid):
      self.pokeid = pokeid
      info_string = pokedb.get_info(pokeid)
      self.name=str(info_string[csvidx['name']])
      self.type1=str(info_string[csvidx['type1']])
      self.type2=str(info_string[csvidx['type2']])
      self.total=int(info_string[csvidx['total']])
      self.hp=int(info_string[csvidx['hp']])
      self.attack=int(info_string[csvidx['attack']])
      self.defense=int(info_string[csvidx['defense']])
      self.special_attack=int(info_string[csvidx['special_attack']])
      self.special_defense=int(info_string[csvidx['special_defense']])
      self.speed=int(info_string[csvidx['speed']])
      self.generation=bool(info_string[csvidx['legendary']])
