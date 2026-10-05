"""
Módulo de Clases para el Sistema de Gestión de Vehículos.
Define la jerarquía de clases: Vehiculo (base), Coche y Moto (derivadas).
"""

from datetime import datetime


class Vehiculo:
    """Clase base que representa un vehículo genérico en el sistema de alquiler."""

    _contador_vehiculos: int = 0

    def __init__(self, marca: str, modelo: str, año: int, precio_base: float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio_base = precio_base
        self._encendido: bool = False
        self._disponible: bool = True

        Vehiculo._contador_vehiculos += 1
        print(f"🚗 Vehículo registrado: {self.marca} {self.modelo} ({self.año})")

    def __del__(self) -> None:
        Vehiculo._contador_vehiculos -= 1
        print(f"🗑️ {self.marca} {self.modelo} ha sido dado de baja.")

    @property
    def encendido(self) -> bool:
        return self._encendido

    @property
    def disponible(self) -> bool:
        return self._disponible

    def encender(self) -> None:
        if not self._encendido:
            self._encendido = True
            print(f"🔑 {self.marca} {self.modelo}: Motor encendido.")
        else:
            print(f"⚠️ {self.marca} {self.modelo}: El motor ya está encendido.")

    def apagar(self) -> None:
        if self._encendido:
            self._encendido = False
            print(f"🔒 {self.marca} {self.modelo}: Motor apagado.")
        else:
            print(f"⚠️ {self.marca} {self.modelo}: El motor ya está apagado.")

    def calcular_alquiler(self, tiempo: float) -> float:
        return self.precio_base * tiempo

    def mostrar_info(self) -> None:
        estado_motor = "Encendido" if self._encendido else "Apagado"
        estado_disp = "Disponible" if self._disponible else "Alquilado"
        print(f"\n--- {self.marca} {self.modelo} ---")
        print(f"  Año: {self.año}")
        print(f"  Precio Base: ${self.precio_base:.2f}")
        print(f"  Motor: {estado_motor}")
        print(f"  Estado: {estado_disp}")

    def alquilar(self) -> None:
        if not self._disponible:
            raise ValueError(f"El vehículo {self.marca} {self.modelo} ya está alquilado.")
        self._disponible = False
        print(f"✅ {self.marca} {self.modelo} ha sido alquilado exitosamente.")

    def devolver(self) -> None:
        if self._disponible:
            raise ValueError(f"El vehículo {self.marca} {self.modelo} no estaba alquilado.")
        self._disponible = True
        print(f"✅ {self.marca} {self.modelo} ha sido devuelto a la flota.")

    @classmethod
    def total_vehiculos(cls) -> int:
        return cls._contador_vehiculos

    @classmethod
    def crear_desde_diccionario(cls, datos: dict):
        return cls(
            marca=datos["marca"],
            modelo=datos["modelo"],
            año=int(datos["año"]),
            precio_base=float(datos["precio_base"]),
        )

    @staticmethod
    def validar_año(año: int) -> bool:
        año_actual = datetime.now().year
        return 1900 < año <= año_actual

    @staticmethod
    def validar_precio(precio: float) -> bool:
        return precio > 0


class Coche(Vehiculo):
    """Clase derivada que representa un automóvil (se alquila por día)."""

    def __init__(self, marca: str, modelo: str, año: int, precio_base: float, num_puertas: int) -> None:
        super().__init__(marca, modelo, año, precio_base)
        self.num_puertas = num_puertas

    def calcular_alquiler(self, dias: float) -> float:
        return (self.precio_base * dias) + (self.num_puertas * 10)

    def mostrar_info(self) -> None:
        super().mostrar_info()
        print(f"  Tipo: Coche | Puertas: {self.num_puertas}")

    def abrir_maletero(self) -> None:
        print(f"🧳 {self.marca} {self.modelo}: Maletero abierto.")


class Moto(Vehiculo):
    """Clase derivada que representa una motocicleta (se alquila por hora)."""

    def __init__(self, marca: str, modelo: str, año: int, precio_base: float, cilindrada: int) -> None:
        super().__init__(marca, modelo, año, precio_base)
        self.cilindrada = cilindrada

    def calcular_alquiler(self, horas: float) -> float:
        return (self.precio_base * horas) + (self.cilindrada * 0.5)

    def mostrar_info(self) -> None:
        super().mostrar_info()
        print(f"  Tipo: Moto | Cilindrada: {self.cilindrada} cc")

    def hacer_caballito(self) -> None:
        print(f"🏍️ {self.marca} {self.modelo}: ¡Haciendo caballito!")