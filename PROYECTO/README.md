# Control de Gastos Personales con Google Sheets

Aplicación de consola hecha en Python para llevar el control de las cuentas, registrar gastos del día a día, organizarlos por categorías y tener todo sincronizado en tiempo real en una hoja de Google Sheets mediante OAuth 2.0.

---

## Funcionalidades principales

* Registro de gastos: Guarda la fecha, la categoría, el detalle del gasto, la plata gastada y el medio de pago.
* Manejo dinámico de categorías: Menú numérico para elegir la categoría o para crear, cambiar de nombre o borrar categorías cuando haga falta.
* Modificar y borrar: Si se anota algo mal o con un valor equivocado, se puede corregir o eliminar directamente desde la consola.
* Sumatoria total: Calcula y muestra de una cuánto se ha gastado en total.
* Todo en la nube: La información queda guardada al instante en dos pestañas de Google Sheets (Gastos y Categorias).
* Conexión segura: Usa OAuth 2.0 y guarda la sesión en un archivo de token para no pedir permisos a cada rato.

---

## Estructura del proyecto

```text
PROYECTO/
│
├── .venv/               # Entorno virtual de Python
├── __pycache__/         # Archivos temporales de Python
├── .gitignore           # Archivos que no se suben a Git
├── cloudg.py            # Funciones de conexión, menús y lógica con Google Sheets
├── credentials.json     # Llave descargada de Google Cloud
├── token.json           # Token que guarda el inicio de sesión
├── main.py              # Archivo principal para arrancar la app
└── README.md            # Documentación del proyecto
```
---

## Requisitos

* Python 3.10 o superior instalado.
* Cuenta de Google para entrar a Google Cloud Console y Google Sheets.

---

## Instalación y puesta en marcha

### 1. Activar el entorno virtual

* En PowerShell:
  .\.venv\Scripts\Activate.ps1

* En Git Bash:
  source .venv/Scripts/activate

### 2. Instalar las librerías

pip install gspread google-auth google-auth-oauthlib

---

## Configurar el archivo de Google Sheets

1. Crear una hoja nueva en Google Sheets con el nombre exacto: ControlGastos.
2. Crear dos pestañas en el archivo:
   * Pestaña 1: Gastos
     Encabezados en la fila 1: Fecha | Categoria | Descripción | Monto | MetodoPago
   * Pestaña 2: Categorias
     Encabezado en la celda A1: Nombre
     (Abajo se pueden poner las primeras opciones como Comida, Transporte, Servicios, Salidas).

---

## Configurar Google Cloud

1. Entrar a Google Cloud Console, armar un proyecto y activar las APIs de Google Sheets y Google Drive.
2. En la pantalla de consentimiento de OAuth, marcarla como Externa y agregar el correo propio en la lista de usuarios de prueba.
3. En la sección de Credenciales, crear un ID de cliente OAuth tipo Aplicación de escritorio.
4. Descargar el archivo JSON, pegarlo en la carpeta del proyecto y renombrarlo como credentials.json.

---

## Seguridad (.gitignore)

Para no compartir las claves ni la sesión por accidente, el archivo .gitignore debe tener:
```
__pycache__/
.venv/
env/
venv/
credentials.json
token.json
GLOSARIO.md
```
---

## Cómo correr el programa

Para iniciar la aplicación, ejecutar en la terminal:

python main.py

Nota: La primera vez que se corra va a abrir una pestaña en el navegador pidiendo autorización. Una vez aceptados los permisos, se genera el archivo token.json y las siguientes veces entra directo sin volver a pedir acceso.