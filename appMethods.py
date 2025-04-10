class Model():
  table = False
  def __init__(self):
    if not self.table:
      print("Error, Table has not been define ")

  def save (self):
    print(F"saving {self.table} en BD")

  def  searchById(self,__id):
      print(f"Search by id : {__id}")

class User(Model):
  table = "user"

user = User()
user.save()
user.searchById("121")
