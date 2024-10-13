from datetime import datetime

class Bicycle:
  def __init__(self, colour, model):
    self._colour = colour
    self._model  = model
    self._created = datetime.now()

  @property
  def colour(self):
    return self._colour

  @colour.setter
  def colour(self, value: str) -> None:
    self._colour = value

  @property
  def model(self):
    return self._model

  @model.setter
  def model(self, value: str) -> None:
    self._model = value

  @property
  def createdDate(self):
    return self._created



Bike = Bicycle('Blue', 'Mountain')

print(f'I have a {Bike.colour} {Bike.model} bike that I bought on {Bike.createdDate}')
