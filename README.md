
# 🍔 Fast Food Menu - Scroll Infinito con HTMX y Flask

## 📋 Descripción
Aplicación web que implementa un scroll infinito para mostrar productos de comida rápida utilizando **HTMX** para la funcionalidad de carga dinámica y **Flask** como backend.

## ✨ Características
- **Scroll Infinito**: Los productos se cargan automáticamente al hacer scroll
- **HTMX**: Sin JavaScript complejo, solo atributos HTML
- **Responsive**: Diseño adaptativo para móviles y desktop
- **API Externa**: Consume datos de una API de productos de comida rápida
- **Paginación Inteligente**: 8 productos por página con detección automática de finalización

## 🚀 Tecnologías Utilizadas
- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Interactividad**: HTMX (Hypertext Markup Language)
- **API**: REST API externa

## 📁 Estructura del Proyecto
```
scroll-infinito-con-HTMX-Python-Flask/
├── app.py                          # Aplicación Flask principal
├── requirements.txt                # Dependencias de Python
├── static/
│   └── home.css                   # Estilos personalizados
├── templates/
│   ├── index.html                 # Página principal
│   └── _products_only.html        # Template de productos
└── docs/
    └── scroll-infinito-htmx.md    # Documentación técnica
```

## 🛠️ Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd scroll-infinito-con-HTMX-Python-Flask
```

### 2. Crear entorno virtual
```bash
python -m venv env
env\Scripts\activate  # Windows
# source env/bin/activate  # Linux/Mac
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
python app.py
```

### 5. Abrir en el navegador
```
http://localhost:5000
```

## 🔧 Cómo Funciona el Scroll Infinito

### Arquitectura
1. **Página Inicial** (`/`): Carga los primeros 8 productos
2. **Load More** (`/load-more`): Endpoint HTMX para cargar más productos
3. **Trigger Automático**: Se activa cuando el usuario hace scroll hacia abajo

### Flujo de Datos
```
Usuario hace scroll → HTMX detecta "revealed" → 
Petición a /load-more → Nuevos productos se insertan → 
Nuevo trigger se crea para la siguiente página
```

### Atributos HTMX Utilizados
- `hx-get`: URL del endpoint para cargar más productos
- `hx-trigger="revealed"`: Se activa cuando el elemento es visible
- `hx-swap="beforeend"`: Inserta el contenido al final del contenedor
- `hx-target="#product-list"`: Contenedor donde se insertan los productos

## 📊 API y Datos

### Endpoint Principal
- **URL**: `https://devsapihub.com/api-fast-food`
- **Método**: GET
- **Respuesta**: Lista de productos en formato JSON

### Estructura de Producto
```json
{
  "id": 1,
  "name": "Nombre del Producto",
  "category": "Categoría",
  "price": 9.99,
  "image": "URL de la imagen"
}
```

### Paginación
- **Productos por página**: 8
- **Cálculo automático**: Total de páginas basado en productos disponibles
- **Detección de finalización**: Automática cuando no hay más productos

## 🎨 Personalización

### Cambiar Productos por Página
Modifica la variable `per_page` en `app.py`:
```python
per_page = 12  # Cambiar de 8 a 12 productos por página
```

### Cambiar la API
Modifica la variable `API_URL` en `app.py`:
```python
API_URL = "https://tu-api.com/productos"
```

### Personalizar Estilos
Los estilos están en `static/home.css` y pueden ser modificados para cambiar:
- Colores de las tarjetas
- Animaciones de hover
- Tamaños de imágenes
- Responsive breakpoints

## 🐛 Solución de Problemas

### Los productos no se cargan
1. Verifica que la API esté funcionando
2. Revisa la consola del navegador para errores
3. Confirma que HTMX esté cargado correctamente

### Scroll infinito no funciona
1. Verifica que el trigger tenga `hx-trigger="revealed"`
2. Confirma que `hx-swap="beforeend"` esté configurado
3. Revisa que el contenedor objetivo exista

### Problemas de rendimiento
1. Reduce el número de productos por página
2. Implementa cache en el servidor
3. Optimiza las imágenes de los productos

## 🔍 Debug y Monitoreo

### Endpoint de Debug
```
http://localhost:5000/debug
```
Muestra información sobre la API y los datos cargados.

### Logs del Servidor
La aplicación imprime logs detallados en la consola:
- 📊 Información de paginación
- 🔄 Cargas de productos
- 🏁 Finalización del scroll infinito

## 📱 Responsive Design
- **Desktop**: 4 productos por fila
- **Tablet**: 3 productos por fila
- **Mobile**: 2 productos por fila
- **Small Mobile**: 1 producto por fila

## 🚀 Mejoras Futuras
- [ ] Cache de productos en el servidor
- [ ] Filtros por categoría
- [ ] Búsqueda de productos
- [ ] Lazy loading de imágenes
- [ ] Animaciones más suaves
- [ ] Modo offline con Service Workers

## 📄 Licencia
Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🤝 Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para sugerencias y mejoras.

---

**Desarrollado con ❤️ usando HTMX y Flask**
