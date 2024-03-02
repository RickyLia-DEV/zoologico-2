class Animal:
    def __init__(self, nombre_cientifico, nombre_comun, region, jaula):
        self.nombre_cientifico = nombre_cientifico
        self.nombre_comun = nombre_comun
        self.region = region
        self.jaula = jaula

    def mostrar_info(self):
        print(f"Nombre científico: {self.nombre_cientifico}")
        print(f"Nombre común: {self.nombre_comun}")
        print(f"Región: {self.region}")
        print(f"Jaula: {self.jaula}")

class Mamifero(Animal):
    def __init__(self, nombre_cientifico, nombre_comun, region, jaula, periodo_gestacion):
        super().__init__(nombre_cientifico, nombre_comun, region, jaula)
        self.periodo_gestacion = periodo_gestacion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Período de gestación: {self.periodo_gestacion}")

class Zoo:
    def __init__(self):
        self.lista_animales = []

    def agregar_animal(self, animal):
        self.lista_animales.append(animal)

    def mostrar_animales(self):
        for animal in self.lista_animales:
            animal.mostrar_info()
            print("")

    def buscar_animal(self, nombre_cientifico):
        for animal in self.lista_animales:
            if animal.nombre_cientifico == nombre_cientifico:
                return animal
        return None

    def editar_animal(self, nombre_cientifico, nuevo_nombre_comun, nueva_region, nueva_jaula):
        animal = self.buscar_animal(nombre_cientifico)
        if animal:
            animal.nombre_comun = nuevo_nombre_comun
            animal.region = nueva_region
            animal.jaula = nueva_jaula
            print("Animal editado correctamente.")
        else:
            print("Animal no encontrado.")

    def eliminar_animal(self, nombre_cientifico):
        animal = self.buscar_animal(nombre_cientifico)
        if animal:
            self.lista_animales.remove(animal)
            print("Animal eliminado correctamente.")
        else:
            print("Animal no encontrado.")

# Programa principal
zoo = Zoo()

while True:
    print("1. Agregar animal")
    print("2. Mostrar todos los animales")
    print("3. Buscar animal")
    print("4. Editar animal")
    print("5. Eliminar animal")
    print("6. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre_cientifico = input("Ingrese el nombre científico del animal: ")
        nombre_comun = input("Ingrese el nombre común del animal: ")
        region = input("Ingrese la región de procedencia del animal: ")
        jaula = input("Ingrese la jaula en la que se encuentra el animal: ")
        periodo_gestacion = input("Ingrese el período de gestación (si aplica): ")

        mamifero = Mamifero(nombre_cientifico, nombre_comun, region, jaula, periodo_gestacion)
        zoo.agregar_animal(mamifero)
        print("Animal agregado correctamente.")

    elif opcion == "2":
        zoo.mostrar_animales()

    elif opcion == "3":
        nombre_cientifico = input("Ingrese el nombre científico del animal a buscar: ")
        animal_encontrado = zoo.buscar_animal(nombre_cientifico)
        if animal_encontrado:
            animal_encontrado.mostrar_info()
        else:
            print("Animal no encontrado.")

    elif opcion == "4":
        nombre_cientifico = input("Ingrese el nombre científico del animal a editar: ")
        nuevo_nombre_comun = input("Ingrese el nuevo nombre común: ")
        nueva_region = input("Ingrese la nueva región: ")
        nueva_jaula = input("Ingrese la nueva jaula: ")
        zoo.editar_animal(nombre_cientifico, nuevo_nombre_comun, nueva_region, nueva_jaula)

    elif opcion == "5":
        nombre_cientifico = input("Ingrese el nombre científico del animal a eliminar: ")
        zoo.eliminar_animal(nombre_cientifico)

    elif opcion == "6":
        break

    else:
        print("Opción no válida. Inténtelo de nuevo.")
