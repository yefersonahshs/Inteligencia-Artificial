Para ejecutar el archivo Python que contiene el código del sistema de transporte inteligente, puedes seguir estos pasos:

1. Crear el archivo Python
Abre tu editor de texto preferido (puede ser Visual Studio Code, Sublime Text, o un simple Bloc de Notas).
Copia el código proporcionado y pégalo en el editor.
Guarda el archivo con la extensión .py, por ejemplo, sistema_transporte_inteligente.py.
2. Instalar Python
Asegúrate de tener Python instalado en tu sistema. Puedes verificar si Python está instalado ejecutando el siguiente comando en tu terminal o consola:

bash
Copiar código
python --version
Si Python no está instalado, puedes descargarlo desde python.org.

3. Ejecutar el archivo
Para ejecutar el archivo que has creado, abre una terminal (en Windows, puedes usar el "Símbolo del sistema" o "PowerShell"; en macOS o Linux, puedes usar la terminal).

Navega a la ubicación donde guardaste el archivo sistema_transporte_inteligente.py usando el comando cd:

bash
Copiar código
cd ruta/donde/guardaste/el/archivo
Una vez que estés en la carpeta correcta, ejecuta el siguiente comando:

bash
Copiar código
python sistema_transporte_inteligente.py
4. Ver el resultado
El sistema imprimirá en la terminal la mejor ruta y su costo total basado en las reglas definidas. Si la ruta no es válida o no se encuentra una ruta que cumpla con las reglas, el sistema lo indicará.

Por ejemplo, los resultados esperados son:

less
Copiar código
Mejor ruta: ['A', 'B', 'D', 'E'] con un costo total de 15
Mejor ruta: ['A', 'B', 'D', 'E'] con un costo total de 15
Mejor ruta: ['A', 'B', 'D'] con un costo total de 12
Estos resultados muestran las mejores rutas posibles desde el punto A a los destinos solicitados, cumpliendo con las reglas definidas (como el costo máximo).
