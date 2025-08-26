# Importamos Flask y la función para renderizar templates
from flask import Flask, render_template

# Creamos la instancia de la aplicación Flask
app = Flask(__name__)


# Esta lista simula una base de datos o fuente de datos
ITEMS = [f"Item {i}" for i in range(1, 101)]

# RUTA PRINCIPAL: Muestra la página de inicio
@app.route("/")
def index():
    # Renderiza el template index.html (página principal)
    return render_template("index.html")

# RUTA PARA CARGAR ELEMENTOS: /load-items/<start> donde <start> es la posición de inicio
@app.route("/load-items/<int:start>")
def load_items(start):
    # LIMITE: Número de elementos que se cargan en cada petición
    limit = 5
    # Calculamos la posición final (start + 5)
    end = start + limit
    # Obtenemos los elementos desde la posición start hasta end
    items = ITEMS[start:end]
    # Verificamos si hay más elementos después de esta carga
    has_more = end < len(ITEMS)
    # Calculamos el total de elementos cargados hasta ahora
    total_cargados = start + len(items)
    # Renderizamos el template items.html pasando:
    # - items: lista de elementos a mostrar
    # - next_start: posición de inicio para la siguiente carga
    # - has_more: booleano que indica si hay más elementos
    # - total_cargados: total de elementos cargados hasta el momento
    return render_template("items.html", items=items, next_start=end, has_more=has_more, total_cargados=total_cargados)


# Ejecutar la app
if __name__ == "__main__":
    # Ejecuta la aplicación en modo debug (útil para desarrollo)
    app.run(debug=True)
