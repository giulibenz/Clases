#Crear una clase Persona() en el archivo persona.py que tenga como atributos 
#nombre, edad y profesion.
#Al instanciar la clase tiene que saludar igual que el dino diciendo sus atributos.

class Persona:
    def __init__(self,un_nombre="",una_edad="",una_profesion="profesor"):
        self.nombre = un_nombre
        self.edad = una_edad
        self.profesion = una_profesion
        print("Hola soy una persona y me llamo", self.nombre, "tengo", self.edad, "soy", self.profesion)

usuario1 = Persona("Marce", "32", "programador") 
usuario2 = Persona("Sol", "22", "design")
usuario4 = Persona(una_profesion="profesor",un_nombre="Brian")
usuario100 = Persona(una_profesion="programadora",un_nombre="Lore")
usuario421 = Persona(un_nombre="Willy", una_edad="21", una_profesion="estudiante")

#para acceder a los atributos o caracteristicas, coloco en la terminal 
#el nombre del objeto, en este caso usuario1 y luego .(elnombredelacaracteristicaquequierosaber)
#ejemplo usuario1.edad