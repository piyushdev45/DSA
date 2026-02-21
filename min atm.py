class pnb:
  def __init__(self,name,kharcha):
    self.name=name
    self.__kharcha=kharcha
  def deposit(self,rokda):
    self.__kharcha=self.__kharcha+rokda
    print(f"your new balance is {self.__kharcha}")

  def withdraw(self,rokda):
    if rokda<=self.__kharcha:
      self.__kharcha-= rokda

    else:
      print("paise jama kar phle")

  def display_kharcha(self):
    print("kharcha:",self.__kharcha)

acc= pnb("marco",145)
print(acc.name)
acc.deposit(3)
acc.withdraw(45)
acc.display_kharcha()