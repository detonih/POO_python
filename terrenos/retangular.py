from interfaces.formas import FormasInterface

class TerrenoRetangular(FormasInterface):

  def __init__(self, largura: int, comprimento: int) -> None:
      self.largura = largura
      self.comprimento = comprimento
  
  def get_perimetro(self) -> int:
      return (self.comprimento * 2) + (self.largura * 2)
  
  def get_area(self) -> int:
      return self.comprimento * self.largura 