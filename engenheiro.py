from typing import Type
from interfaces.formas import FormasInterface

class Engenheiro:

  def __init__(self, nome: str) -> None:
      self.nome = nome
  # Para modicar estes metodos, teremos que passar elementos que tenham
  # a forma da interface. O engenheiro se associa a qualquer elemento
  # que implemente a interface (quadrado ou retangulo), não importando
  # qual tipo de terreno, deve somente estar de acordo com a interface
  # Portanto, tenho certeza de que a medição das formas é a correta.
  # Assim, posso criar outros elementos (classes) de formas geometricas 
  # e o engenheiro poderá utiliza-las
  # Agora posso dizer que o elemento que irá entrar neste metodo tem uma forma
  # (uma interface), pq a partir dessa interface eu garanto que a implementacao
  # de seus metodos foram feitas
  def medir_perimetro(self, terreno: Type[FormasInterface]):
    perimetro = terreno.get_perimetro()
    print(f"{self.nome} mediu o perimetro: {perimetro} m")
    return perimetro

  def medir_area(self, terreno: Type[FormasInterface]):
    area = terreno.get_area()
    print(f"{self.nome} mediu a area: {area} m2")
    return area