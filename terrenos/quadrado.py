from interfaces.formas import FormasInterface

class TerrenoQuadrado(FormasInterface):

  def __init__(self, lado: int) -> None:
      self.lado = lado
  
  def get_perimetro(self) -> int:
      return self.lado * 4
  
  def get_area(self) -> int:
      return self.lado * self.lado 