from abc import ABC , abstractmethod
class Model(ABC):
  @abstractmethod
  def save(self):
    pass

class User(Model):
  def save(self):
    print("saving in the DB...")

class Sesion(Model):

  def save(self):
    print("Save in file....")

def save(entities):
    for entity in entities:
      entity.save()

user = User()
sesion = Sesion()
save([sesion,user]) #polymorphism