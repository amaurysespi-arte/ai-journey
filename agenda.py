import json
import os

ARCHIVO = "contactos.json"


def cargar_contactos():
    """Carga los contactos desde el archivo JSON."""
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except Exception:
            return {}
    return {}


def guardar_contactos(contactos):
    """Guarda los contactos en el archivo JSON."""
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(contactos, archivo, indent=4, ensure_ascii=False)


def agregar_contacto(contactos):
    """Agrega un nuevo contacto."""
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Correo electrónico: ")

    contactos[nombre] = {
        "telefono": telefono,
        "email": email
    }

    guardar_contactos(contactos)
    print("\n✅ Contacto agregado correctamente.")


def buscar_contacto(contactos):
    """Busca un contacto por nombre."""
    nombre = input("Ingrese el nombre a buscar: ")

    if nombre in contactos:
        print("\n📞 Contacto encontrado")
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {contactos[nombre]['telefono']}")
        print(f"Correo: {contactos[nombre]['email']}")
    else:
        print("\n❌ Contacto no encontrado.")


def eliminar_contacto(contactos):
    """Elimina un contacto."""
    nombre = input("Ingrese el nombre a eliminar: ")

    if nombre in contactos:
        del contactos[nombre]
        guardar_contactos(contactos)
        print("\n✅ Contacto eliminado correctamente.")
    else:
        print("\n❌ Contacto no encontrado.")


def listar_contactos(contactos):
    """Muestra todos los contactos."""
    if not contactos:
        print("\n📭 No hay contactos registrados.")
        return

    print("\n📋 LISTA DE CONTACTOS")
    print("-" * 40)

    for nombre, datos in contactos.items():
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {datos['telefono']}")
        print(f"Correo: {datos['email']}")
        print("-" * 40)


def menu():
    """Menú principal."""
    contactos = cargar_contactos()

    while True:
        print("\n===== AGENDA DE CONTACTOS =====")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Listar contactos")
        print("5. Salir")

        try:
            opcion = int(input("\nSeleccione una opción: "))

            if opcion == 1:
                agregar_contacto(contactos)

            elif opcion == 2:
                buscar_contacto(contactos)

            elif opcion == 3:
                eliminar_contacto(contactos)

            elif opcion == 4:
                listar_contactos(contactos)

            elif opcion == 5:
                print("\n👋 Hasta luego.")
                break

            else:
                print("\n⚠️ Opción inválida. Intente nuevamente.")

        except ValueError:
            print("\n⚠️ Debe introducir un número.")


menu()