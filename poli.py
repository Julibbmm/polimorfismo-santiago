# HERENCIA, POLIMORFISMO, ENCAPSULAMIENTO,
# PROPIEDADES Y ABSTRACCIÓN

from abc import ABC, abstractmethod



class Personaje(ABC):

    def __init__(self, nombre, vidas):
        self.__nombre = nombre
        self.__vidas = vidas


    
    @property
    def nombre(self):
        return self.__nombre


    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre != "":
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("El nombre no puede estar vacío")


   
    @property
    def vidas(self):
        return self.__vidas


    
    @vidas.setter
    def vidas(self, nuevas_vidas):
        if nuevas_vidas >= 0:
            self.__vidas = nuevas_vidas
        else:
            raise ValueError("Las vidas no pueden ser negativas")


    
    @abstractmethod
    def atacar(self):
        pass



class Zombie(Personaje):

    
    def atacar(self):
        return 1



class Dragon(Personaje):

    
    def atacar(self):
        return 2



class Esqueleto(Personaje):

   
    def atacar(self):
        return 1



class Avatar(Personaje):

    
    def atacar(self):
        return 1


    def recibir_ataque(self, enemigo):

        daño = enemigo.atacar()

        self.vidas -= daño

        print(enemigo.nombre, "atacó al avatar")
        print("Daño recibido:", daño)
        print("Vidas restantes:", self.vidas)
        print()


# CREAR EL AVATAR
avatar = Avatar("Héroe", 5)


# CREAR LOS ENEMIGOS
zombie = Zombie("Zombie", 1)

dragon = Dragon("Dragón", 3)

esqueleto = Esqueleto("Esqueleto", 2)


# ATAQUES
avatar.recibir_ataque(zombie)

avatar.recibir_ataque(dragon)

avatar.recibir_ataque(esqueleto)


# PROBAR GETTERS
print("Nombre del avatar:", avatar.nombre)
print("Vidas del avatar:", avatar.vidas)


# PROBAR SETTER
avatar.vidas = 5

print("Nuevas vidas:", avatar.vidas)


# PROBAR MENSAJE DE ERROR
avatar.vidas = -3
