import random

from combat import Combat

COLORS = ['yellow', 'red', 'blue', 'green']

# For parent class, pass in object to work in Python 2 and 3
class Monster(Combat):
  min_hit_points = 1
  max_hit_points = 1
  min_experience = 1
  max_experience = 1
  weapon = 'sword'
  sound = 'roar'
  
  def __init__(self, **kwargs):
    self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
    self.experience = random.randint(self.min_experience, self.max_experience)
    self.color = random.choice(COLORS)

    # Override default attributes: input Monster(color='newcolor', etc..)
    for key, value in kwargs.items():
      setattr(self, key, value)   
      
      
  def __str__(self):
    return '{} {}, HP: {}, XP: {}'.format(self.color.title(), 
                                          self.__class__.__name__, 
                                          self.hit_points, 
                                          self.experience)
  
  def battlecry(self):
    return self.sound.upper()
  
# Subclass of Monster  
class Goblin(Monster):
  max_hit_points = 3
  max_experience = 2
  sound = 'squeak'
  
# Subclass of Monster  
class Troll(Monster):
  min_hit_poitns = 3
  max_hit_points = 5
  min_experience = 2
  max_experience = 6
  sound = 'growl'
  
# Subclass of Monster  
class Dragon(Monster):
  min_hit_points = 5
  max_hit_points = 10
  min_experience = 6
  max_experience = 10
  sound = 'raaaaaaaaar'
  
  
