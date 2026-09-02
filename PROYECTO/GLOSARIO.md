# Glosario de Funciones y Métodos del Proyecto

Guía técnica de referencia sobre las funciones, métodos y librerías utilizadas para la conexión con Google Sheets, autenticación y manejo de lógica en Python.

---

## Métodos de Google Sheets (gspread)

* **append_row(lista):** Agrega una fila nueva al final de la hoja. Recibe una lista con los valores en orden (por ejemplo: `[fecha, categoria, descripcion, monto, metodo]`).
* **get_all_records():** Lee todas las filas de la hoja y las devuelve como una lista de diccionarios en Python, usando los encabezados de la primera fila como las llaves de cada dato.
* **col_values(numero_columna):** Obtiene todos los valores de una columna específica en forma de lista. Se usa con el valor `1` para extraer todas las categorías registradas en la columna A.
* **row_values(numero_fila):** Devuelve todos los valores presentes en una fila específica.
* **update_cell(fila, columna, nuevo_valor):** Modifica el valor de una celda puntual especificando su posición por fila y columna, permitiendo actualizar datos sin alterar el resto del registro.
* **delete_rows(numero_fila):** Elimina completamente una fila de la hoja de cálculo a partir de su número de índice.
* **worksheet("NombrePestaña"):** Permite seleccionar y operar sobre una pestaña específica dentro del mismo archivo de Google Sheets.

---

## Métodos de Autenticación y Sistema (google-auth / os)

* **InstalledAppFlow.from_client_secrets_file(archivo, scopes):** Carga el archivo `credentials.json` y configura el flujo de autenticación OAuth 2.0 con los permisos solicitados.
* **flow.run_local_server(port=0):** Abre automáticamente una pestaña en el navegador web para realizar el inicio de sesión y conceder los permisos a la aplicación.
* **Credentials.from_authorized_user_file(archivo, scopes):** Carga la sesión previamente guardada en `token.json` para conectarse de forma directa sin requerir autenticación en el navegador en cada ejecución.
* **creds.refresh(Request()):** Renueva automáticamente el token de acceso cuando este ha expirado, manteniendo la sesión activa sin interrupciones.
* **os.path.exists(ruta):** Comprueba si un archivo o ruta existe en el sistema local; se utiliza para verificar la presencia previa de `token.json`.

---

## Funciones y Métodos Nativos de Python

* **strip():** Remueve espacios en blanco innecesarios al inicio y al final de una cadena de texto ingresada por consola.
* **isdigit():** Valida si un string contiene exclusivamente caracteres numéricos, empleado para verificar la validez de las opciones del menú.
* **lower():** Transforma el texto ingresado a minúsculas para estandarizar respuestas del usuario (por ejemplo, aceptar indistintamente `'s'` o `'S'`).
* **enumerate(iterable, start=1):** Itera sobre una lista generando de forma automática pares de índice y elemento, utilizado para listar menús numerados en la consola.
* **datetime.now().strftime("%Y-%m-%d"):** Obtiene la fecha actual del sistema y le aplica el formato estándar de año-mes-día.
* **try / except ValueError:** Estructura de control de excepciones que evita la detención abrupta del programa al intentar convertir cadenas no numéricas mediante `float()`.