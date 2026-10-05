# Sistema de Gestión de Vehículos (Simulador de Alquiler)

Este proyecto es una aplicación de consola desarrollada en Python aplicando los principios fundamentales de la **Programación Orientada a Objetos (POO)**.

## 🛠️ Características y Conceptos Implementados
- **Clase Base y Derivadas (Herencia):** Implementación de la clase `Vehiculo` y sus clases hijas `Coche` y `Moto`.
- **Encapsulamiento:** Control de acceso a atributos privados (`_encendido`, `_disponible`) mediante decoradores `@property`.
- **Polimorfismo:** Sobrescritura del método `calcular_alquiler()` y `mostrar_info()` según el tipo de vehículo.
- **Métodos de Clase y Estáticos:** Uso de `@classmethod` para métricas globales e instancias alternativas, y `@staticmethod` para validaciones.
- **Control de Excepciones:** Manejo de entradas inválidas del usuario y reglas de negocio.

## 📁 Estructura del Proyecto
```text
simulador_vehiculos/
│
├── clases/
│   └── vehiculos.py    # Definición de clases y lógica POO
├── main.py             # Menú interactivo y flujo principal
└── README.md           # Documentación del repositorio
