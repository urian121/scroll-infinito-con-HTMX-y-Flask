# Scroll Infinito con Python + Flask + HTMX

## 🎯 ¿Qué hace este proyecto?

Este proyecto demuestra cómo crear un **scroll infinito** (carga automática de contenido al hacer scroll) usando **HTMX** (HyperText Markup Language eXtended) y **Python Flask**. Es una implementación moderna y eficiente que no requiere JavaScript complejo.

### Resultado Final 😲
![Resultado Final](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/refs/heads/master/scroll-infinito-con-Python-Flask-y-HTMX.gif)

## ✨ Características principales

- 🚀 **Scroll infinito automático**: El contenido se carga automáticamente mientras haces scroll
- 💻 **Sin JavaScript complejo**: Utiliza HTMX para funcionalidades avanzadas
- 🎨 **Interfaz moderna**: Diseño limpio con Bootstrap 5
- ⚡ **Carga eficiente**: Solo carga 20 elementos a la vez
- 🔄 **Indicador de carga**: Muestra un spinner mientras carga nuevo contenido
- 📱 **Responsive**: Funciona perfectamente en dispositivos móviles y de escritorio

## 🏗️ Estructura del proyecto

```
scroll-infinito-con-HTMX-Python-Flask/
├── app.py                 # Aplicación principal de Flask
├── requirements.txt       # Dependencias de Python
├── static/
│   └── home.css         # Estilos personalizados
├── templates/
│   ├── index.html       # Página principal
│   └── items.html       # Template para los elementos
└── README.md            # Este archivo
```

## 🚀 Cómo funciona

### 1. **Página inicial** (`index.html`)
- Muestra un título y un contenedor vacío para los elementos
- Incluye un "sentinel" inicial que se activa al cargar la página
- El sentinel hace una petición HTMX a `/load-items/0` para cargar los primeros 20 elementos

### 2. **Carga de elementos** (`/load-items/<start>`)
- Flask recibe la petición y devuelve 20 elementos desde la posición especificada
- Los elementos se renderizan usando el template `items.html`
- Se incluye un nuevo sentinel para la siguiente carga

### 3. **Scroll infinito**
- Cuando el usuario hace scroll y el sentinel se hace visible
- HTMX automáticamente hace una nueva petición para cargar más elementos
- El proceso se repite hasta que no hay más elementos

## 🚀 Instalación y ejecución

### 1. **Clonar o descargar el proyecto**
```bash
git clone <https://github.com/urian121/scroll-infinito-con-HTMX-y-Flask.git>
cd scroll-infinito-con-HTMX-y-Flask
```

### 2. **Crear un entorno virtual** (recomendado)
```bash
python -m venv env
```

### 3. **Activar el entorno virtual**

**En Windows:**
```bash
env\Scripts\activate
```

**En macOS/Linux:**
```bash
source env/bin/activate
```

### 4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

### 5. **Ejecutar la aplicación**
```bash
python app.py
```

### 6. **Abrir en el navegador**
Ve a `http://localhost:5000` en tu navegador

## 🔧 Cómo personalizar

### **Cambiar el número de elementos por carga**
En `app.py`, modifica la variable `limit`:
```python
limit = 20  # Cambia este número
```

### **Agregar más elementos**
En `app.py`, modifica la lista `ITEMS`:
```python
ITEMS = [f"Item {i}" for i in range(1, 101)]  # 100 elementos en lugar de 50
```

### **Modificar el diseño de las tarjetas**
Edita `templates/items.html` para cambiar cómo se muestran los elementos.


## 🔍 Conceptos clave explicados

### **¿Qué es HTMX?**
HTMX es una biblioteca que permite hacer peticiones HTTP directamente desde HTML, sin necesidad de escribir JavaScript. Es perfecta para crear aplicaciones web interactivas de manera simple.

### **¿Qué es un "sentinel"?**
Un sentinel es un elemento HTML que actúa como "detector" para saber cuándo cargar más contenido. En este proyecto, cuando el sentinel se hace visible (al hacer scroll), HTMX automáticamente hace una nueva petición.

### **¿Cómo funciona el scroll infinito?**
1. Se cargan los primeros elementos
2. Se coloca un sentinel al final
3. Al hacer scroll, el sentinel se hace visible
4. HTMX detecta esto y carga más elementos
5. Se coloca un nuevo sentinel
6. El proceso se repite


## 📚 Recursos adicionales

- [Documentación oficial de HTMX](https://htmx.org/docs/)
- [Documentación de scroll infinito con HTMX](https://htmx.org/examples/infinite-scroll/)


## 🙌 Cómo puedes apoyar 📢:
✨ **Comparte este proyecto** con otros desarrolladores para que puedan beneficiarse 📢.
☕ **Invítame un café o una cerveza 🍺**:
   - [Paypal](https://www.paypal.me/iamdeveloper86) (`iamdeveloper86@gmail.com`).

### ⚡ ¡No olvides SUSCRIBIRTE a la [Comunidad WebDeveloper](https://www.youtube.com/WebDeveloperUrianViera?sub_confirmation=1)!

#### ⭐ **Déjanos una estrella en GitHub**:
   - Dicen que trae buena suerte 🍀.
**Gracias por tu apoyo 🤓.**

