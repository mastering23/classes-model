from abc import ABC,abstractmethod

#abc mean absctract class

class Model(ABC):
  @property
  @abstractmethod
  def table(self):
    pass

  def save (self):
    print(F"saving {self.table} en BD")

  def  searchById(self,__id):
      print(f"Search by id : {__id}")

class User(Model):
  table = "user"

#model = model()
user = User()
user.save()
user.searchById("121")
