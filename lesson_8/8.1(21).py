class Player:

  def __init__(self, name, score=0):
    self.name = name
  def get_score(self, score):
    return int(input())

  def set_score(self, score):
    return score


player_1 = Player("Алиса")


# Не удаляйте этот код, он нужен для проверки

print(player_1.name, player_1.get_score())
player_1.set_score(200)
print(player_1.name, player_1.get_score())
player_1.set_score(500)
print(player_1.name, player_1.get_score())