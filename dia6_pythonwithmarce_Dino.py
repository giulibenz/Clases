""" class Dino:
    # cola, dientes, color, size 
    def __init__(self,nombre):
        print("Hola soy un dinosario, me llamo", nombre)

pepito = Dino("Pepe") 
type(pepito) 
 """
#Agregarle una propiedad color a la clase Dino, y que salude diciendo 
#de que color es el dinosaurio

""" class Dino:
    # cola, dientes, color, size 
    def __init__(self,nombre,color):
        print("Hola soy un dinosario, me llamo", nombre, "tengo la piel", color)

pepito = Dino("Pepe", "azul") 
type(pepito)  """

class Dino:
    # cola, dientes, color, size 
    def __init__(self,un_nombre="",un_color="verde"):
        self.nombre = un_nombre
        self.color = un_color
        print("Hola soy un dinosario, me llamo", self.nombre, "tengo la piel color", self.color)

pepito = Dino("Pepe", "azul") 
pepita = Dino("Pepa", "rojo")
pepite = Dino("Pepx")
pepiti = Dino("Pxpx", "lila")
pepo = Dino(un_color="rosa",un_nombre="")
pepu = Dino(un_color="Pink",un_nombre="Jorge")

#Aca se ordena, por self Dino, luego pepe que tiene que ver con el parametro que
#le pusiste que seria un_nombre y luego el segundo parametro un_color.

#Crear una carpeta que se llame clases y adentro poner los 
#archivos dino.py persona.py 

#se puede trabajar en conjunto al mismo tiempo con git y github que 
#sistema de control de versiones vcs / version control sytems
#el creador de git, fue el que creo linux tambien 
#creo para poder manejar lo que era el kernell de linux y para que se 
#pueda desarrollar entre un millon de personas en un proyecto, 
#desde muchas partes del mundo. 

#otro ejemplo es gitlab.com




