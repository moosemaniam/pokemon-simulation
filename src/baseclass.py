from random import randint

from status import stat_class

class pokemon(object):
  def __init__(self,pokeid):
    self.stat = stat_class(pokeid)

  def print_info():
    print(self.stat)
    #Read a csv file containing info and fill these

