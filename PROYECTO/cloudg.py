from datetime import datetime
import os
import gspread
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

NOMBRE_HOJA = "ControlGastos"


# ==========================================
# 1. CONEXIÓN Y ACCESO A PESTAÑAS
# ==========================================
from google.auth.exceptions import RefreshError

# ... (resto de tus imports)


def autenticar_google():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except RefreshError:
                # Si el token caducó o fue revocado, lo eliminamos y pedimos login de nuevo
                os.remove("token.json")
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    cliente = gspread.authorize(creds)
    archivo = cliente.open(NOMBRE_HOJA)
    return archivo.worksheet("Gastos"), archivo.worksheet("Categorias")


# ==========================================
# 2. GESTIÓN DE CATEGORÍAS
# ==========================================
def obtener_lista_categorias(hoja_cat):
    """Devuelve la lista de categorías ignorando el encabezado."""
    valores = hoja_cat.col_values(1)
    if len(valores) > 1:
        return valores[1:]  # Ignora la celda A1 ('Nombre')
    return []


def seleccionar_o_administrar_categoria(hoja_cat):
    """Muestra el menú numerado de categorías y permite elegir o gestionar."""
    while True:
        categorias = obtener_lista_categorias(hoja_cat)

        print("\n--- SELECCIONA UNA CATEGORÍA ---")
        for i, cat in enumerate(categorias, start=1):
            print(f"{i}. {cat}")

        opcion_admin = len(categorias) + 1
        print(f"{opcion_admin}. [Añadir, Eliminar o Modificar Categoría]")

        seleccion = input(
            f"Elige una opción (1-{opcion_admin}): "
        ).strip()

        if seleccion.isdigit():
            idx = int(seleccion)
            if 1 <= idx <= len(categorias):
                return categorias[idx - 1]  # Retorna la categoría seleccionada
            elif idx == opcion_admin:
                menu_administrar_categorias(hoja_cat)
            else:
                print("Número fuera de rango.")
        else:
            print("Por favor, ingresa un número válido.")


def menu_administrar_categorias(hoja_cat):
    """Submenú a/b/c para gestionar categorías."""
    while True:
        print("\n--- GESTIÓN DE CATEGORÍAS ---")
        print("a. Añadir categoría")
        print("b. Eliminar categoría")
        print("c. Modificar categoría")
        print("v. Volver al menú de selección")

        op = input("Elige una opción (a/b/c/v): ").strip().lower()

        categorias = obtener_lista_categorias(hoja_cat)

        if op == "a":
            nueva = input("Nombre de la nueva categoría: ").strip()
            if nueva and nueva not in categorias:
                hoja_cat.append_row([nueva])
                print(f" Categoría '{nueva}' añadida.")
            else:
                print("Nombre inválido o ya existente.")

        elif op == "b":
            print("\nCategorías disponibles para eliminar:")
            for i, cat in enumerate(categorias, start=1):
                print(f"{i}. {cat}")
            num = input("Número de categoría a eliminar: ").strip()
            if num.isdigit() and 1 <= int(num) <= len(categorias):
                fila_eliminar = int(num) + 1  # +1 por el encabezado
                categoria_eliminada = categorias[int(num) - 1]
                hoja_cat.delete_rows(fila_eliminar)
                print(f" Categoría '{categoria_eliminada}' eliminada.")
            else:
                print("Selección inválida.")

        elif op == "c":
            print("\nCategorías disponibles para modificar:")
            for i, cat in enumerate(categorias, start=1):
                print(f"{i}. {cat}")
            num = input("Número de categoría a modificar: ").strip()
            if num.isdigit() and 1 <= int(num) <= len(categorias):
                fila_modificar = int(num) + 1
                nombre_actual = categorias[int(num) - 1]
                nuevo_nombre = input(
                    f"Nuevo nombre para '{nombre_actual}': "
                ).strip()
                if nuevo_nombre:
                    hoja_cat.update_cell(fila_modificar, 1, nuevo_nombre)
                    print(
                        f" Categoría cambiada a '{nuevo_nombre}'."
                    )
            else:
                print("Selección inválida.")

        elif op == "v":
            break
        else:
            print("Opción inválida.")


# ==========================================
# 3. GESTIÓN DE GASTOS (CRUD)
# ==========================================
def registrar_gasto(hoja_gastos, hoja_cat):
    print("\n--- REGISTRAR NUEVO GASTO ---")
    fecha = datetime.now().strftime("%Y-%m-%d")

    categoria = seleccionar_o_administrar_categoria(hoja_cat)
    descripcion = input("Descripción del gasto: ").strip()

    while True:
        try:
            monto = float(input("Monto gastado: ").strip())
            if monto <= 0:
                print("El monto debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Monto inválido.")

    metodo = input("Método de pago (Efectivo/Tarjeta/Transferencia): ").strip()

    nueva_fila = [fecha, categoria, descripcion, monto, metodo]
    hoja_gastos.append_row(nueva_fila)
    print(f" Gasto de ${monto:,.2f} registrado en '{categoria}'.\n")


def listar_gastos(hoja_gastos):
    print("\n--- HISTORIAL DE GASTOS ---")
    registros = hoja_gastos.get_all_records()

    if not registros:
        print("No hay gastos registrados.\n")
        return []

    total = 0.0
    for i, fila in enumerate(registros, start=1):
        monto = float(fila.get("Monto", 0))
        total += monto
        print(
            f"[{i}] {fila.get('Fecha')} | {fila.get('Categoria')} | {fila.get('Descripción')} | ${monto:,.2f} | {fila.get('MetodoPago')}"
        )

    print(f"\n TOTAL GASTADO: ${total:,.2f}\n")
    return registros


def modificar_gasto(hoja_gastos, hoja_cat):
    registros = listar_gastos(hoja_gastos)
    if not registros:
        return

    num = input(
        "Ingresa el número [#] del gasto que deseas modificar: "
    ).strip()
    if not num.isdigit() or not (1 <= int(num) <= len(registros)):
        print("Selección inválida.")
        return

    fila_sheet = int(num) + 1  # +1 por encabezado
    gasto_actual = registros[int(num) - 1]

    print(f"\nModificando gasto: {gasto_actual.get('Descripción')}")
    print("Deja el campo vacío si no deseas cambiarlo.")

    # 1. Categoría
    cambiar_cat = (
        input("¿Deseas cambiar la categoría? (s/n): ").strip().lower()
    )
    if cambiar_cat == "s":
        nueva_cat = seleccionar_o_administrar_categoria(hoja_cat)
        hoja_gastos.update_cell(fila_sheet, 2, nueva_cat)

    # 2. Descripción
    nueva_desc = input(
        f"Nueva descripción [{gasto_actual.get('Descripción')}]: "
    ).strip()
    if nueva_desc:
        hoja_gastos.update_cell(fila_sheet, 3, nueva_desc)

    # 3. Monto
    nuevo_monto = input(f"Nuevo monto [{gasto_actual.get('Monto')}]: ").strip()
    if nuevo_monto:
        try:
            hoja_gastos.update_cell(fila_sheet, 4, float(nuevo_monto))
        except ValueError:
            print("Monto inválido, no se modificó.")

    # 4. Método de pago
    nuevo_metodo = input(
        f"Nuevo método de pago [{gasto_actual.get('MetodoPago')}]: "
    ).strip()
    if nuevo_metodo:
        hoja_gastos.update_cell(fila_sheet, 5, nuevo_metodo)

    print(" Gasto actualizado correctamente.\n")


def eliminar_gasto(hoja_gastos):
    registros = listar_gastos(hoja_gastos)
    if not registros:
        return

    num = input(
        "Ingresa el número [#] del gasto que deseas ELIMINAR: "
    ).strip()
    if not num.isdigit() or not (1 <= int(num) <= len(registros)):
        print("Selección inválida.")
        return

    fila_sheet = int(num) + 1
    confirmar = (
        input("¿Estás seguro de eliminar este registro? (s/n): ").strip().lower()
    )
    if confirmar == "s":
        hoja_gastos.delete_rows(fila_sheet)
        print(" Registro eliminado con éxito.\n")
    else:
        print("Operación cancelada.\n")


# ==========================================
# 4. BUCLE PRINCIPAL
# ==========================================
def iniciar_aplicacion():
    print("Conectando con Google Sheets...")
    hoja_gastos, hoja_categorias = autenticar_google()
    print(" Conexión establecida.\n")

    while True:
        print("=== GESTOR DE GASTOS PERSONALES ===")
        print("1. Registrar nuevo gasto")
        print("2. Ver todos los gastos y total")
        print("3. Modificar un gasto")
        print("4. Eliminar un gasto")
        print("5. Administrar Categorías")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ").strip()

        if opcion == "1":
            registrar_gasto(hoja_gastos, hoja_categorias)
        elif opcion == "2":
            listar_gastos(hoja_gastos)
        elif opcion == "3":
            modificar_gasto(hoja_gastos, hoja_categorias)
        elif opcion == "4":
            eliminar_gasto(hoja_gastos)
        elif opcion == "5":
            menu_administrar_categorias(hoja_categorias)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")