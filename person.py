from random import randint

class Person:
  anoAtual = 2022
  
  @staticmethod
  def gerarId():
    rand = randint(10000, 19999)
    return rand
    
  def __init__(self, name, idade, comendo = False, falando = False):
    self.id = self.gerarId()
    self.name = name
    self.idade = idade
    self.comendo = comendo
    self.falando = falando
    
  @classmethod
  def porAnoDeNascimento(cls, name, anoNascimento):
    idade = cls.anoAtual - anoNascimento
    return cls(name, idade)
  
  def comer(self, alimento):
    if self.comendo:
      print(f"{self.name} ja esta comendo")
      return
    
    print(f"{self.name} esta comendo {alimento}")
    self.comendo = True
    
  def pararComer(self):
    if not self.comendo:
      print(f"{self.name} nao esta comendo")
      return
    
    self.comendo = False
    print(f"{self.name} parou de comer")