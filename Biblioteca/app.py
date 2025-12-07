from database import Session
from models import Libro
from sqlalchemy.exc import SQLAlchemyError


def agregar_libro():
    session = Session()
    try:
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género: ")
        leido = input("¿Leído? (si/no): ").lower()

        libro = Libro(titulo=titulo, autor=autor, genero=genero, leido=leido)
        session.add(libro)
        session.commit()

        print("\n✔ Libro agregado correctamente.\n")
    except SQLAlchemyError as e:
        print(" Error al agregar libro:", e)
        session.rollback()
    finally:
        session.close()


def actualizar_libro():
    session = Session()
    try:
        ver_libros()
        id_libro = input("ID del libro a actualizar: ")

        libro = session.query(Libro).filter_by(id=id_libro).first()

        if not libro:
            print("\n Libro no encontrado.\n")
            return

        libro.titulo = input("Nuevo título: ")
        libro.autor = input("Nuevo autor: ")
        libro.genero = input("Nuevo género: ")
        libro.leido = input("¿Leído? (si/no): ").lower()

        session.commit()
        print("\n Libro actualizado.\n")

    except SQLAlchemyError as e:
        print(" Error al actualizar:", e)
        session.rollback()
    finally:
        session.close()


def eliminar_libro():
    session = Session()
    try:
        ver_libros()
        id_libro = input("ID del libro a eliminar: ")

        libro = session.query(Libro).filter_by(id=id_libro).first()

        if not libro:
            print("\n Libro no encontrado.\n")
            return

        session.delete(libro)
        session.commit()

        print("\n✔ Libro eliminado.\n")

    except SQLAlchemyError as e:
        print(" Error al eliminar libro:", e)
        session.rollback()
    finally:
        session.close()


def ver_libros():
    session = Session()
    libros = session.query(Libro).all()

    print("\n LISTADO DE LIBROS")
    print("-" * 40)

    for libro in libros:
        print(f"ID: {libro.id}")
        print(f"Título: {libro.titulo}")
        print(f"Autor: {libro.autor}")
        print(f"Género: {libro.genero}")
        print(f"Leído: {libro.leido}")
        print("-" * 40)

    print()
    session.close()


def buscar_libros():
    session = Session()
    print("\nBuscar por:")
    print("1. Título")
    print("2. Autor")
    print("3. Género")

    opcion = input("Elige una opción: ")

    campo = { "1": "titulo", "2": "autor", "3": "genero" }.get(opcion)

    if not campo:
        print("\n Opción inválida\n")
        return

    valor = input(f"Introduce {campo}: ")

    resultados = session.query(Libro).filter(getattr(Libro, campo).like(f"%{valor}%")).all()

    print("\n Resultados:")
    print("-" * 40)
    for libro in resultados:
        print(f"{libro.id} - {libro.titulo} - {libro.autor} - {libro.genero} - {libro.leido}")
    print()

    session.close()


def menu():
    while True:
        print(" MENÚ BIBLIOTECA (MariaDB + ORM)")
        print("1. Agregar libro")
        print("2. Actualizar libro")
        print("3. Eliminar libro")
        print("4. Ver libros")
        print("5. Buscar libros")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            actualizar_libro()
        elif opcion == "3":
            eliminar_libro()
        elif opcion == "4":
            ver_libros()
        elif opcion == "5":
            buscar_libros()
        elif opcion == "6":
            print("\n Saliendo…")
            break
        else:
            print("\n Opción no válida\n")


if __name__ == "__main__":
    menu()
