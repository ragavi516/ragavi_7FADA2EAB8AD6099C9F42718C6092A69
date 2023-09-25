#define the base class player
class player:
  def play(self):
    print("The player is playing cricket:")
#define the derived class bastman
class Batsman(player):
  def play(self):
     print("The batsman is batting")
  #define the derived class bowler
class Bowler(player):
 def play(self):
    print("The bowler is bowling")
player=player()
batsman=Batsman()
bowler=Bowler()

player.play()
batsman.play()
bowler.play()