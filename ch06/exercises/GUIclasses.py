class Player:
  def __init__(self, pnum):
    self.player_num = 1
    self.lives = 3
    self.can_jump = True

class Mushroom:
  def __init__(self, pnum):
    self.is_small = True
    self.can_die = True
    self.num = 2
    
class Mario:
  def __init__(self, pnum):
    self.can_run = True
    self.color = "red"
    self.is_large = True