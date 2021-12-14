from terrenos.quadrado import TerrenoQuadrado
from terrenos.retangular import TerrenoRetangular
from engenheiro import Engenheiro

egenheiro = Engenheiro("Geraldo")
terreno_quadrado = TerrenoQuadrado(4)
terreno_retangular = TerrenoRetangular(3, 2)

egenheiro.medir_area(terreno_quadrado)
egenheiro.medir_area(terreno_retangular)
egenheiro.medir_perimetro(terreno_retangular)
egenheiro.medir_perimetro(terreno_quadrado)
