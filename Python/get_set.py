class Goods:
  def __init__(self, name, price):
    self.__data = {"name":name, "price":price}

  @property
  def name(self):
    return self.__data["name"]

  @name.setter  # impossible to declare before @property
  def name(self, value):
    self.__data["name"] = value

  @property
  def price(self):
    price = self.__data["price"]
    price_str = f"{price} yen"
    return price_str
