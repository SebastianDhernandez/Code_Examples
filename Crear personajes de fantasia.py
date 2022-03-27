# Programa que crea personajes de fantasia para un juegode rol, con estadisticas, habilidades y propiedades

import random
import time
from abc import ABC, abstractmethod
from os import system


class Personaje(ABC):  # Clase padre abstracta
    @abstractmethod
    def __init__(self, nombre="Desconocido", raza="Descnocida", *args):
        self._nombre = nombre  # El nombre y la raza seran privados, para que no sean modificados fuera de las clases
        self._raza = raza
        self.fuerza = 0
        self.vida = 0
        self.magia = 0
        self.resistencia = 0
        self.skills = args

    def random_name(self):
        razas_list = ["Elfo", "Humano", "Orco", "Vampiro", "Enano", "Gigante", "Fantasma", "Duende", "Hombre lobo",
                      "Infectado", "Ser de luz", "Semi dios"]
        nombres_list = ["Gnar", "Don", "Krieg", "Luffy", "Kroll", "Damura", "Helios", "Gromm", "Astarot", "Will",
                        "Tzukamat", "Juan", "Timi"]
        nombres_list2 = ["Tralsafar", "Di marco", "Sasaki", "D. rogger", "Muhami", "Tsata", "II Aurelion", "Urff"]
        apodos_list = ["El drestructor", "Del viento", "Guerrero del norte", "El maquinista", "El maestro sombra",
                       "El maldito", "El pirata", "El asesino", "El hereje"]
        self._raza = random.choice(razas_list)
        self._nombre = random.choice(nombres_list) + " " + random.choice(nombres_list2) + " " \
                        + random.choice(apodos_list)

    def random_stats(self):
        self.fuerza = random.randint(50, 150)
        self.magia = random.randint(50, 150)
        self.vida = random.randint(50, 150)
        self.resistencia = random.randint(50, 150)

    def informacion(self):
        print("Nombre => ", self._nombre)
        print("Raza => ", self._raza)
        print("Estadisticas: ")
        print("Fuerza => ", self.fuerza)
        print("Vida => ", self.vida)
        print("magia => ", self.magia)
        print("Resistencia => ", self.resistencia)
        if len(self.skills) != 0:
            print("Habilidades: ")
            for i in self.skills:
                print("=> ", i)

    def getname(self):
        return self._nombre  # Para obtener el nombre, cree esta funcion interna de la clase padre

    @abstractmethod
    def powerup(self):
        print("El personaje ", self._nombre, " ha mejorado sus estadisticas")


class Guerrero(Personaje):  # Clase hija, es la unica que puede atacar
    def __init__(self, nombre="Desconocido", raza="Desconocida", *args):
        super().__init__(nombre, raza, *args)
        self.fuerza = 130

    def atacar(self, objetivo):
        print("El guerrero ", self._nombre, " ataco a ", objetivo.getname())
        damage = self.fuerza - objetivo.resistencia
        if damage > 0:
            print(objetivo.getname(), " perdio ", self.fuerza - objetivo.resistencia, " puntos de vida")
            objetivo.vida -= damage
        else:
            print(objetivo.getname(), " resistio el ataque de ", self._nombre)

    def powerup(self):
        super().powerup()
        self.fuerza += 10
        self.vida += 10


class Clerigo(Personaje):  # Clase hija, es la unica que puede curar
    def __init__(self, nombre="Desconocido", raza="Desconocida", *args):
        super().__init__(nombre, raza, *args)
        self.magia = 130

    def curar(self, objetivo):
        print("El clerigo ", self._nombre, " curo a ", objetivo.getname())
        curacion = self.magia * random.random()  # Su curacion tiene una potencia entre 0 a 100% de su magia
        curacion = round(curacion, 1)
        objetivo.vida += curacion
        print(objetivo.getname(), " recupero ", curacion, " puntos de vida")

    def powerup(self):
        super().powerup()
        self.magia += 10
        self.vida += 10


class Mago(Personaje):  # Clase hija, es la unica que puede conjurar
    def __init__(self, nombre="Desconocido", raza="Desconocida", *args):
        super().__init__(nombre, raza, *args)
        self.magia = 130

    def conjurar(self, objetivo):
        print("El mago ", self._nombre, " conjuro a ", objetivo.getname())
        conjuro = self.magia * random.uniform(0, 0.5)  # Me gusta que sea random la potencia de su conjuro
        conjuro = round(conjuro, 1)                    # entre 0 y 50% de su magia
        objetivo.fuerza += conjuro
        print(objetivo.getname(), " aumento su fuerza ", conjuro, " puntos")

    def powerup(self):
        super().powerup()
        self.magia += 10
        self.vida += 10


class Tanque(Personaje):  # Clase hija, es la unica que puede conjurar
    def __init__(self, nombre="Desconocido", raza="Desconocida", *args):
        super().__init__(nombre, raza, *args)
        self.vida = 130
        self.resistencia = 100

    def resistir(self):
        resistir = self.resistencia * random.random()  # La mejora en su resistencia es aleatoria, entre 0 a 100%
        resistir = round(resistir, 1)                        # de su resistencia anterior
        self.resistencia += resistir
        print(self.getname(), " aumento su resistencia ", resistir, " puntos")

    def powerup(self):
        super().powerup()
        self.resistencia += 10
        self.vida += 10


# Este es un ejemplo, donde un tanque (Pj1) es atacado ferozmente por un guerrero (Pj2), luego es curado por un clerigo
# (Pj3) y luego es conjurado por un mago (Pj4), al final, el tanque obtiene un powerup por su feroz batalla
Pj1 = Tanque("Gordrick el macizo", "Gigante", "Resistir", "Voluntad de hierro")
Pj1.random_name()
Pj1.informacion()
time.sleep(5)
system("cls")
Pj2 = Guerrero("Adam warlock", "Humano", "Rayo estelar", "Patada en la cabeza")
Pj2.random_stats()
Pj2.informacion()
time.sleep(5)
system("cls")
Pj3 = Clerigo()
Pj3.random_stats()
Pj3.random_name()
Pj3.informacion()
time.sleep(5)
system("cls")
Pj4 = Mago()
Pj4.random_stats()
Pj4.informacion()
time.sleep(5)
system("cls")
Pj2.atacar(Pj1)
time.sleep(5)
system("cls")
Pj3.curar(Pj1)
time.sleep(5)
system("cls")
Pj4.conjurar(Pj1)
time.sleep(5)
system("cls")
Pj1.resistir()
Pj1.powerup()
Pj1.informacion()
