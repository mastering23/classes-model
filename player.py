class Player():

  def Magic(self):
    print("Magic Attack !")

  def Sword(self):
    print("Sword Attack")

  def Block(self):
    print("Block")


player1 = Player()

player2= Player()


print(f"player 1 :")
player1.Sword()
print(f"player 2 :")
player2.Block()
print(f"player 2 :")
player2.Magic()
print(f"player 1 :")
player1.Block()
print(f"player 1 :")
player1.Magic()

