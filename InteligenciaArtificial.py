class SistemaTransporteInteligente:
    def __init__(self):
        self.rutas = {}
        self.reglas = []

    # Añadir rutas entre estaciones
    def agregar_ruta(self, estacion_a, estacion_b, costo):
        if estacion_a not in self.rutas:
            self.rutas[estacion_a] = {}
        self.rutas[estacion_a][estacion_b] = costo

    # Definir reglas lógicas para la búsqueda de rutas
    def agregar_regla(self, regla):
        self.reglas.append(regla)

    # Evaluar si una ruta cumple con las reglas
    def cumple_reglas(self, ruta, costo_total):
        for regla in self.reglas:
            if not regla(ruta, costo_total):
                return False
        return True

    # Buscar la mejor ruta aplicando reglas
    def mejor_ruta(self, inicio, destino):
        visitados = []
        por_visitar = [(inicio, [inicio], 0)]  # (nodo_actual, ruta_actual, costo_total)

        while por_visitar:
            estacion_actual, ruta, costo = por_visitar.pop(0)

            if estacion_actual == destino and self.cumple_reglas(ruta, costo):
                return ruta, costo

            if estacion_actual not in visitados:
                visitados.append(estacion_actual)
                for vecina, costo_vecina in self.rutas.get(estacion_actual, {}).items():
                    nueva_ruta = ruta + [vecina]
                    nuevo_costo = costo + costo_vecina
                    if self.cumple_reglas(nueva_ruta, nuevo_costo):
                        por_visitar.append((vecina, nueva_ruta, nuevo_costo))

        return None, float('inf')  # En caso de que no haya ruta
    
    # Regla que dice que el costo total no debe superar 15
def regla_costo_maximo(ruta, costo_total):
    return costo_total <= 15


# Crear el sistema de transporte inteligente
sistema = SistemaTransporteInteligente()

# Agregar rutas
sistema.agregar_ruta('A', 'B', 5)
sistema.agregar_ruta('A', 'C', 10)
sistema.agregar_ruta('B', 'C', 3)
sistema.agregar_ruta('B', 'D', 7)
sistema.agregar_ruta('C', 'D', 2)
sistema.agregar_ruta('D', 'E', 3)

# Agregar reglas al sistema
sistema.agregar_regla(regla_costo_maximo)

# Encontrar la mejor ruta entre dos puntos
ruta, costo_total = sistema.mejor_ruta('A', 'E')

print(f"Mejor ruta: {ruta} con un costo total de {costo_total}")

# Encontrar la mejor ruta entre A y E
ruta, costo_total = sistema.mejor_ruta('A', 'E')
print(f"Mejor ruta: {ruta} con un costo total de {costo_total}")


# Encontrar la mejor ruta entre A y D (sin conexión directa)
ruta, costo_total = sistema.mejor_ruta('A', 'D')
print(f"Mejor ruta: {ruta} con un costo total de {costo_total}")  # Esperamos None y costo infinito
