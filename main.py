"""
Programa principal con menú interactivo en consola para la gestión de flota.
"""

from clases.vehiculos import Coche, Moto, Vehiculo


def leer_entero_positivo(mensaje: str) -> int:
    """Solicita un número entero positivo con captura de excepciones."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("❌ Debe ingresar un entero positivo mayor a cero.")
                continue
            return valor
        except ValueError:
            print("❌ Entrada inválida. Debe ingresar un número entero.")


def leer_flotante_positivo(mensaje: str) -> float:
    """Solicita un número flotante positivo con captura de excepciones."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("❌ Debe ingresar un valor numérico positivo mayor a cero.")
                continue
            return valor
        except ValueError:
            print("❌ Entrada inválida. Debe ingresar un número válido.")


def seleccionar_vehiculo(flota: list) -> int:
    """Muestra los vehículos disponibles en una lista numerada y lee el índice."""
    if not flota:
        print("⚠️ No hay vehículos registrados en la flota.")
        return -1

    print("\n--- Lista de Vehículos ---")
    for idx, v in enumerate(flota):
        tipo = "Coche" if isinstance(v, Coche) else "Moto"
        print(f"[{idx}] {tipo} - {v.marca} {v.modelo} ({v.año})")

    while True:
        try:
            opcion = int(input("\nSeleccione el número de índice del vehículo: "))
            if 0 <= opcion < len(flota):
                return opcion
            print(f"❌ Índice fuera de rango. Seleccione entre 0 y {len(flota) - 1}.")
        except ValueError:
            print("❌ Por favor, ingrese un número de índice entero válido.")


def registrar_coche(flota: list) -> None:
    """Solicita datos e instancia un objeto Coche."""
    print("\n--- Registrar Nuevo Coche ---")
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()

    while True:
        año = leer_entero_positivo("Año: ")
        if Vehiculo.validar_año(año):
            break
        print("❌ Año fuera de rango permitido (debe ser mayor a 1900 y no futuro).")

    while True:
        precio_base = leer_flotante_positivo("Precio base por día: $")
        if Vehiculo.validar_precio(precio_base):
            break
        print("❌ El precio debe ser un valor positivo.")

    num_puertas = leer_entero_positivo("Número de puertas: ")

    coche = Coche(marca, modelo, año, precio_base, num_puertas)
    flota.append(coche)


def registrar_moto(flota: list) -> None:
    """Solicita datos e instancia un objeto Moto."""
    print("\n--- Registrar Nueva Moto ---")
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()

    while True:
        año = leer_entero_positivo("Año: ")
        if Vehiculo.validar_año(año):
            break
        print("❌ Año fuera de rango permitido (debe ser mayor a 1900 y no futuro).")

    while True:
        precio_base = leer_flotante_positivo("Precio base por hora: $")
        if Vehiculo.validar_precio(precio_base):
            break
        print("❌ El precio debe ser un valor positivo.")

    cilindrada = leer_entero_positivo("Cilindrada (cc): ")

    moto = Moto(marca, modelo, año, precio_base, cilindrada)
    flota.append(moto)


def mostrar_flota(flota: list) -> None:
    """Aplica polimorfismo invocando mostrar_info() en cada elemento."""
    if not flota:
        print("\n⚠️ La flota se encuentra vacía.")
        return

    print("\n=== INFORMACIÓN DE LA FLOTA ===")
    for v in flota:
        v.mostrar_info()


def cambiar_estado_motor(flota: list) -> None:
    """Permite encender o apagar el motor de un vehículo seleccionado."""
    idx = seleccionar_vehiculo(flota)
    if idx == -1:
        return

    vehiculo = flota[idx]
    print(f"\nVehículo seleccionado: {vehiculo.marca} {vehiculo.modelo}")
    print("1. Encender motor")
    print("2. Apagar motor")
    opc = input("Seleccione una opción: ").strip()

    if opc == "1":
        vehiculo.encender()
    elif opc == "2":
        vehiculo.apagar()
    else:
        print("❌ Opción no válida.")


def calcular_alquiler_flota(flota: list) -> None:
    """Calcula el monto total de alquiler según las reglas de negocio."""
    idx = seleccionar_vehiculo(flota)
    if idx == -1:
        return

    vehiculo = flota[idx]

    if not vehiculo.disponible:
        print(f"❌ No se puede calcular el alquiler: {vehiculo.marca} {vehiculo.modelo} ya está alquilado.")
        return

    if isinstance(vehiculo, Coche):
        tiempo = leer_flotante_positivo("Ingrese el número de DÍAS de alquiler: ")
        costo = vehiculo.calcular_alquiler(tiempo)
        print(f"💵 Costo total de alquiler ({tiempo} días): ${costo:.2f}")
    elif isinstance(vehiculo, Moto):
        tiempo = leer_flotante_positivo("Ingrese el número de HORAS de alquiler: ")
        costo = vehiculo.calcular_alquiler(tiempo)
        print(f"💵 Costo total de alquiler ({tiempo} horas): ${costo:.2f}")


def alquilar_vehiculo(flota: list) -> None:
    """Procesa el alquiler de un vehículo."""
    idx = seleccionar_vehiculo(flota)
    if idx == -1:
        return

    try:
        flota[idx].alquilar()
    except ValueError as e:
        print(f"❌ Error: {e}")


def devolver_vehiculo(flota: list) -> None:
    """Procesa la devolución de un vehículo."""
    idx = seleccionar_vehiculo(flota)
    if idx == -1:
        return

    try:
        flota[idx].devolver()
    except ValueError as e:
        print(f"❌ Error: {e}")


def ver_estadisticas(flota: list) -> None:
    """Muestra recuentos e métricas generales sobre la flota."""
    total_creados = Vehiculo.total_vehiculos()
    activos_en_lista = len(flota)
    encendidos = sum(1 for v in flota if v.encendido)
    coches = sum(1 for v in flota if isinstance(v, Coche))
    motos = sum(1 for v in flota if isinstance(v, Moto))

    print("\n========================================")
    print("        📊 ESTADÍSTICAS DE LA FLOTA      ")
    print("========================================")
    print(f"Total de vehículos creados (Histórico/Activos): {total_creados}")
    print(f"Vehículos en inventario actual: {activos_en_lista}")
    print(f"Vehículos con motor encendido: {encendidos}")
    print(f"Total de Coches: {coches}")
    print(f"Total de Motos: {motos}")
    print("========================================")


def dar_de_baja_vehiculo(flota: list) -> None:
    """Elimina el vehículo de la lista y activa el destructor __del__."""
    idx = seleccionar_vehiculo(flota)
    if idx == -1:
        return

    vehiculo_eliminado = flota.pop(idx)
    del vehiculo_eliminado


def main():
    flota = []

    while True:
        print("\n========================================")
        print("  🚗 SISTEMA DE GESTIÓN DE VEHÍCULOS 🏍️  ")
        print("========================================")
        print("1. Registrar coche")
        print("2. Registrar moto")
        print("3. Mostrar flota")
        print("4. Encender/Apagar vehículo")
        print("5. Calcular alquiler")
        print("6. Alquilar vehículo")
        print("7. Devolver vehículo")
        print("8. Ver estadísticas")
        print("9. Dar de baja vehículo")
        print("10. Salir")
        print("========================================")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_coche(flota)
        elif opcion == "2":
            registrar_moto(flota)
        elif opcion == "3":
            mostrar_flota(flota)
        elif opcion == "4":
            cambiar_estado_motor(flota)
        elif opcion == "5":
            calcular_alquiler_flota(flota)
        elif opcion == "6":
            alquilar_vehiculo(flota)
        elif opcion == "7":
            devolver_vehiculo(flota)
        elif opcion == "8":
            ver_estadisticas(flota)
        elif opcion == "9":
            dar_de_baja_vehiculo(flota)
        elif opcion == "10":
            print("\n👋 Saliendo del sistema. ¡Gracias por utilizar la aplicación!")
            break
        else:
            print("❌ Opción inválida. Seleccione un número entre 1 y 10.")


if __name__ == "__main__":
    main()