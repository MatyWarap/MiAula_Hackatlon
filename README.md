# 📚 Mi Aula

> **Una aplicación web para potenciar el aprendizaje y la organización estudiantil.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Status](https://img.shields.io/badge/Status-En%20Desarrollo-orange)

## 📖 Descripción

**Mi Aula** es una aplicación web desarrollada con **Flask** diseñada para ayudar a los alumnos a gestionar sus materias, organizar sus tareas y mejorar su rendimiento académico.

Este proyecto nació como parte de un **Hackathon**, con el objetivo de brindar una solución tecnológica, simple y efectiva a los desafíos cotidianos de la vida estudiantil.

## 🚀 Características Principales

* **Gestión de Materias**: Agrega y organiza las asignaturas que estás cursando.
* **Organizador de Tareas**: Mantén un registro de entregas y exámenes importantes.
* **Interfaz Intuitiva**: Diseño simple y fácil de usar, pensado para estudiantes.
* **Acceso Rápido**: Toda la información de tus clases centralizada en un solo lugar.

## 🖼️ Capturas de pantalla

### Página de inicio
![Home](/static/img/screenshots/home.png)

### Inicio docente
![Dashboard_docente](/static/img/screenshots/dashboard_docente.png)

### Inicio alumno
![Dashboard_alumno](/static/img/screenshots/dashboard_alumno.png)

### Trivia
![Trivia](/static/img/screenshots/trivia.png)

### Editar preguntas
![Edit_question](/static/img/screenshots/edit.png)

## 🛠️ Tecnologías Utilizadas

* **Backend**: [Python](https://www.python.org/) y [Flask](https://flask.palletsprojects.com/).
* **Frontend**: HTML5, CSS3.
* **Base de Datos**: MySQL.

## 🔧 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

### 1. Clonar el repositorio

```bash
git clone [https://github.com/MatyWarap/MiAula_Hackatlon.git](https://github.com/MatyWarap/MiAula_Hackatlon.git)
cd MiAula_Hackatlon
```

### 2. Crear un entorno virtual

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

Asegúrate de tener el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto si es necesario. Ejemplo de contenido:

```env
MYSQL_USER=XXXX
MYSQL_PASSWORD=XXXX
MYSQL_HOST=XXXX
MYSQL_DATABASE=XXXX
MYSQL_PORT=XXXX
JWT_SECRET=XXXX
```

### 5. Ejecutar la aplicación

```bash
flask run
```

La aplicación estará disponible en `http://127.0.0.1:5000`.

## ✒️ Integrantes

* **MatyWarap** - [Perfil de GitHub](https://github.com/MatyWarap)
* **EnzoER16** - [Perfil de GitHub](https://github.com/EnzoER16)
* **LautaroVidelaa** - [Perfil de GitHub](https://github.com/LautaroVidelaa)
* **Gusdeveloperrr** - [Perfil de GitHub](https://github.com/Gusdeveloperrr)