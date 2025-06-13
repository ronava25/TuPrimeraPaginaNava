# 🐍 PyShare

## Descripción

**PyShare** es una red social para desarrolladores Python. Permite compartir proyectos, aplicaciones e ideas con descripciones enriquecidas e imágenes. Cada usuario puede registrarse, editar su perfil, publicar proyectos y enviar mensajes privados.

---

## Instrucciones de instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/pyshare.git
cd pyshare
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

---

## Funcionalidades principales

- `/` → Página principal
- `/accounts/signup/` → Registro de usuario
- `/accounts/login/` → Iniciar sesión
- `/accounts/profile/` → Ver y editar perfil
- `/pages/` → Lista de proyectos compartidos
- `/pages/create/` → Crear nuevo proyecto
- `/messages/` → Bandeja de entrada
- `/messages/send/` → Enviar mensaje
- `/about/` → Acerca de PyShare

---

## Tecnologías utilizadas

- Python 3.13
- Django 5.x
- SQLite
- Bootstrap 5
- Pillow
- CKEditor

---

## Autoría

Desarrollado por **Rocío Nava** como proyecto final del curso de Python - Coderhouse.

