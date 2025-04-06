from random import choice
from experta import *


class Dis(Fact):
  "Dişleri fırçalarken kanama olması"
  "-Dişleri fırçalarken uzun süreli kanama olması"
  "-Diş eti çekilmesi varlığı ve diş kökünün görünmesi"
  "-Yiyecek ve içeceklerden dişlerde renk değişimi görülmesi"
  "-Yeni diş çıkarken dişetinde morarma görülmesi"
  "-Ağrı yapmayan çürük varlığı"
  "-İleri derecede çürük varlığı"
  pass

class DisTedavisi(KnowledgeEngine):
  @Rule(Dis(diseti="kanama"))
  def kanama(self):
    print("diş hastalığı vardır ve diş hekimine başvur")

  @Rule(Dis(diseti="uzun süreli kanama"))
  def uzunkanama(self):
    print("Diş eti çekilmesi vardır ve diş hekimine başvur")

  @Rule(Dis(diseti="diş eti çekilmesi ve kök görünmesi"))
  def dolgu(self):
    print("Dolgu yaptır")

  @Rule(Dis(diseti="renk değişimi"))
  def temizle(self):
    print("Dişleri temizle")

  @Rule(Dis(diseti="yeni diş çıkarken morarma varsa"))
  def morarma(self):
    print("diş hekimine başvur")

  @Rule(Dis(diseti="Ağrı yapmayan çürük"))
  def curuk(self):
    print("dolgu yaptır")

  @Rule(Dis(diseti="ileri derece çürük"))
  def kanal(self):
    print("Kanal tedavisi ve dolgu yaptır")

  
uzman = DisTedavisi()
uzman.reset()
uzman.declare(Dis(diseti=choice(["kanama","uzun süreli kanama","diş eti çekilmesi ve kök görünmesi","renk değişimi","yeni diş çıkarken morarma varsa","ağrı yapmayan çürük","ileri derece çürük"])))
uzman.run()